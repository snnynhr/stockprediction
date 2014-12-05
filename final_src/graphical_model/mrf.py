import argparse
import codecs
import collections
import itertools
import json
import lbfgs
import multiprocessing
import random
import operator
import os
import sys
import time

import numpy as np

from stock_list import STOCK_LIST

# -1 is DOWN, 1 is UP
feature_map = {(-1, -1): 1, (-1, 1): 2, (1, -1): 3, (1, 1): 4}


def mrf_learning():
  o = A.train_file.readline()
  stock_count = len(STOCK_LIST)

  print >>sys.stderr, '{} stocks found.'.format(stock_count)
  print >>sys.stderr, 'Reading training instances...',
  # D = []
  # D_id = []
  X = np.zeros((stock_count, stock_count, 5), dtype=np.float)
  for i, line in enumerate(A.train_file):
    date, o = line.split(u'\t', 1)
    o = json.loads(o)
    # D_id.append(date)

    for s_i, s_j in itertools.product(xrange(stock_count), xrange(stock_count)):
      if s_i >= s_j: continue
      stock_i, stock_j = STOCK_LIST[s_i], STOCK_LIST[s_j]  # name of stocks (tickers), whereas s_i and s_j are indexes

      if stock_i in o and stock_j in o:
        k = feature_map[o[stock_i], o[stock_j]]
        X[s_i, s_j, k] += 1
      #end if
    #end for
    # print X_d
    # D.append(X_d)
    print >>sys.stderr, date,
    # if i == 100: break
  #end for
  print >>sys.stderr
  # N = len(D)

  pool = multiprocessing.Pool(processes=8)
  worker_results = []
  last_s_i = None
  for s_i, s_j in itertools.product(xrange(stock_count), xrange(stock_count)):
    if s_i >= s_j: continue
    if last_s_i != s_i:
      print >>sys.stderr, 'Computing pairwise potentials for {}...'.format(STOCK_LIST[s_i])
      last_s_i = s_i
    #end if

    feature_counts = X[s_i, s_j, :]  # note: feature_counts[0] is ignored!
    assert feature_counts.size == 5

    r = pool.apply_async(learn_clique, args=(feature_counts, (STOCK_LIST[s_i], STOCK_LIST[s_j])))
    worker_results.append((s_i, s_j, r))
  #end for
  pool.close()

  model = {'stock_list': STOCK_LIST, 'l2': A.l2}
  for (s_i, s_j, r) in worker_results:
    x_result = r.get()
    x_max = x_result.max()
    probs = np.exp(x_result - x_max) / np.sum(np.exp(x_result - x_max))
    print >>sys.stderr, 'Potentials for {} x {}:'.format(STOCK_LIST[s_i], STOCK_LIST[s_j]), '[' + u', '.join(map(u'{:.2f}'.format, probs)) + ']'
    model[STOCK_LIST[s_i] + u':' + STOCK_LIST[s_j]] = {'weights': list(x_result), 'probs': list(probs), 'e_counts': list(feature_counts[1:])}
  #end for

  json.dump(model, A.model_file, indent=2)
#end def


def learn_clique(feature_counts, (stock_i, stock_j)):
  # print >>sys.stderr, '[{}] Training pairwise potentials for {} and {}...'.format(multiprocessing.current_process().name, stock_i, stock_j),

  def f(x, g, *args):
    counts_, l2 = args[0], args[1]
    counts_sum = np.sum(counts_)
    # l2 = 0.0

    x_max = x.max()
    log_Z = x_max + np.log(np.sum(np.exp(x - x_max)))
    fx = 0.0
    log_px = x - log_Z
    for i in xrange(4):
      g[i] = l2 * x[i]
      g[i] -= (counts_[i] / counts_sum) - np.exp(log_px[i])
      fx -= ((counts_[i] / counts_sum) * log_px[i]) - (0.5 * l2 * (x[i] * x[i]))
    #end for
    # g /= np.linalg.norm(g)
    # xx = np.exp(x) / np.sum(np.exp(x))
    # print fx, x, xx, g, np.linalg.norm(g)

    return fx
  #end def

  def progress(x, g, fx, xnorm, gnorm, step, k, num_eval, *args):
    # print 'iter={}\tfx={:.4f}\tg={:.4f}'.format(k, fx, gnorm)
    x_result = args[2]
    for i in xrange(4):
      x_result[i] = x[i]
  #end def

  l = lbfgs.LBFGS()
  l.max_iterations = 10
  # l.delta = 1e-5
  # l.epsilon = 1e-5
  # l.xtol = 1e-16
  # l.ftol = 1e-4
  # l.gtol = 0.1
  # l.linesearch = 'morethuente'
  # print feature_counts[1:], feature_counts[1:] / np.sum(feature_counts[1:])
  if np.sum(feature_counts[1:]) == 0:
    return np.zeros(4, dtype=np.float)

  x_result = np.zeros(4, dtype=np.float)
  l.minimize(f, np.zeros(4, dtype=np.float), progress=progress, args=(feature_counts[1:], A.l2, x_result))
  # print feature_counts[1:], feature_counts[1:] / np.sum(feature_counts[1:]), x_result, np.exp(x_result) / np.sum(np.exp(x_result))

  return x_result
#end def


def mrf_inference(instances):
  print >>sys.stderr, 'Reading model file {}'.format(A.model_file.name)
  model = json.load(A.model_file)
  model_stock_list = model['stock_list']
  # stock_map = dict([(s, i) for i, s in enumerate(STOCK_LIST)])
  stock_count = len(model_stock_list)

  pairwise_factors = np.zeros((stock_count, stock_count, 4), dtype=np.float)
  neighbors = [[] for i in xrange(stock_count)]
  connections = 0
  for s_i, s_j in itertools.product(xrange(stock_count), xrange(stock_count)):
    if s_i >= s_j: continue
    p = np.array(model[model_stock_list[s_i] + ':' + model_stock_list[s_j]]['weights'], dtype=np.float)
    H = np.dot(np.exp(p), p)  # compute the dist entropy
    # print >>sys.stderr, '{}:{}\t{}\t{}'.format(model_stock_list[s_i], model_stock_list[s_j], p, H)

    if H < A.prune_entropy:  # prune edges, negative entropy so < instead of > (smaller here means nearer to 0 means more uniform)
      continue
    connections += 1
    pairwise_factors[s_i, s_j, :] = p
    pairwise_factors[s_j, s_i, :] = p
    neighbors[s_i].append(s_j)
    neighbors[s_j].append(s_i)
  #end for
  for s_i in xrange(stock_count): neighbors[s_i].sort()
  # sys.exit()

  print >>sys.stderr, 'iterations={}  num_threads={}  flip={}  prune_entropy={} ({:.2f})'.format(A.iterations, A.num_threads, A.flip, A.prune_entropy, float(connections) / np.sum([i + 1 for i in xrange(stock_count - 1)]))
  print >>sys.stderr, 'Using {} threads for inference...'.format(A.num_threads)
  pool = multiprocessing.Pool(processes=A.num_threads)
  worker_results = []
  start_time = time.time()
  for i, (instance_id, instance) in enumerate(instances):
    r = pool.apply_async(mh_inference, args=(instance, model_stock_list, neighbors, pairwise_factors, (A.iterations, A.flip, A.annealing)))
    worker_results.append((instance_id, r))
  #end for
  pool.close()
  print >>sys.stderr, 'Waiting for tasks to finish...'

  results = {}
  for instance_id, r in worker_results:
    state, accept_ratio, (initial_ll, final_ll) = r.get()
    results[instance_id] = state
    print >>sys.stderr, '[{}] accept_ratio={:.3f}  delta_LL={:.3f} ({:.2f}%)  time={:.2f}  up/down={}/{}'.format(instance_id, accept_ratio, (final_ll - initial_ll), abs((final_ll - initial_ll) / initial_ll * 100.0), time.time() - start_time, np.sum(state > 0), np.sum(state < 0))
  #end for
  pool.join()

  return results
#end def


def mh_inference(instance, model_stock_list, neighbors, pairwise_factors, (iterations, flip, annealing)):
  stock_count = len(model_stock_list)
  assert len(instance) == stock_count
  state = np.zeros(stock_count, dtype=np.int32)
  unary_factors = np.zeros((stock_count, 2), dtype=np.float)
  for s_i in xrange(stock_count):
    unary_factors[s_i, 0] = annealing * np.log(instance[model_stock_list[s_i]])  # down
    unary_factors[s_i, 1] = annealing * np.log(1.0 - instance[model_stock_list[s_i]])  # up
    Z = np.sum(np.exp(unary_factors[s_i, :]))
    unary_factors[s_i, :] -= np.log(Z)
    state[s_i] = -1 if instance[model_stock_list[s_i]] > 0.5 else 1  # sets the default state
    # state[s_i] = -1 if np.random.rand() < instance[model_stock_list[s_i]] else 1  # sets the default state
  #end for

  def ll(S):
    ll = 0.0
    for s_i in xrange(stock_count):
      ll += unary_factors[s_i, S[s_i]]
      for s_j in neighbors[s_i]:
        if s_j >= s_i: break
        ll += pairwise_factors[s_j, s_i, feature_map[S[s_j], S[s_i]] - 1]
    #end for
    # print (S + 1) / 2
    return ll
  #end def

  stock_indexes = range(stock_count)
  accept_count = 0
  initial_ll = ll(state)
  new_state = np.copy(state)
  for gibbs_i in xrange(iterations):
    to_flip = random.sample(stock_indexes, flip)
    for s_i in xrange(stock_count): new_state[s_i] = state[s_i]
    for s_i in to_flip: new_state[s_i] = -state[s_i]

    old_ll = 0.0
    new_ll = 0.0

    history = set()
    for s_i in to_flip:
      state_s_i = state[s_i]
      new_state_s_i = new_state[s_i]
      old_ll += unary_factors[s_i, state_s_i]
      new_ll += unary_factors[s_i, new_state_s_i]
      for s_j in neighbors[s_i]:
        if (s_i, s_j) in history: continue

        history.add((s_j, s_i))
        history.add((s_i, s_j))
        old_ll += pairwise_factors[s_j, s_i, feature_map[state[s_j], state_s_i] - 1]
        new_ll += pairwise_factors[s_j, s_i, feature_map[new_state[s_j], new_state_s_i] - 1]
      #end for
    #end for

    if new_ll > old_ll: accept = True
    else: accept = (np.log(np.random.rand()) < (new_ll - old_ll))
    # print new_ll, old_ll, accept
    if accept:
      state = np.copy(new_state)
      accept_count += 1
    #end if
  #end for
  accept_ratio = float(accept_count) / A.iterations

  return state, accept_ratio, (initial_ll, ll(state))

  # for s_i in xrange(stock_count):
  #   unary_factors[s_i, 0] = np.log(instance[model_stock_list[s_i]])  # down
  #   unary_factors[s_i, 1] = np.log(1.0 - instance[model_stock_list[s_i]])  # up
  #   state[s_i] = -1 if np.random.rand() < instance[model_stock_list[s_i]] else 1  # sets the default state
  # #end for
  # posterior = np.zeros((stock_count, 2), dtype=np.int)
  # print ll(), time.time()
  # new_state = np.copy(state)
  # log_p = np.zeros(2, dtype=np.float)
  # for gibbs_i in xrange(100):
  #   for s_i in xrange(stock_count):
  #     log_p[:] = unary_factors[s_i, :]
  #     for s_j in xrange(stock_count):
  #       if s_i < s_j:
  #         log_p[0] += pairwise_factors[s_i, s_j, feature_map[-1, state[s_j]] - 1]
  #         log_p[1] += pairwise_factors[s_i, s_j, feature_map[1, state[s_j]] - 1]
  #       elif s_j < s_i:
  #         log_p[0] += pairwise_factors[s_j, s_i, feature_map[state[s_j], -1] - 1]
  #         log_p[1] += pairwise_factors[s_j, s_i, feature_map[state[s_j], 1] - 1]
  #       #end if
  #     #end for
  #     p = np.exp(log_p - log_p.max())
  #     if np.random.rand() * (p[0] + p[1]) < p[0]: state[s_i] = -1
  #     else: state[s_i] = 1
  #     if gibbs_i > A.burnin and (gibbs_i - A.burnin) % A.autolag == 0: posterior[s_i, state[s_i]] += 1
  #   #end for
  # #end for
  # print ll(), time.time()
#end def


def test_instances():  # IMPLEMENT THIS TO RETURN THE UNARY FACTORS!
  global gold_labels

  print >>sys.stderr, 'Reading files from weights dir {} and test instances from test dir {}'.format(A.weights_dir, A.test_dir)
  instances = collections.defaultdict(dict)
  for stock in STOCK_LIST:
    print >>sys.stderr, stock
    weights_path = os.path.join(A.weights_dir, stock + '.txt')
    creg_model = {}
    with utf8_input_file(weights_path) as f:
      f.readline()  # discxard first line
      for line in f:
        label, feat, weight = line.strip().split('\t', 2)
        if label == 'r_down': creg_model[feat] = float(weight)
        elif label == 'r_up': creg_model[feat] = -float(weight)
        else: raise Exception('Unknown label')
      #end for
    #end with
    assert u'***BIAS***' in creg_model

    test_path = os.path.join(A.test_dir, stock + '.json')
    with utf8_input_file(test_path) as f:
      o = json.load(f)
    #end with

    for d, stock_info in o.iteritems():
      features = stock_info['features']
      label = stock_info['change']

      down_ll = creg_model[u'***BIAS***']
      for s, featvec in features.iteritems():
        for k, v in featvec.iteritems():
          down_ll += creg_model.get(k, 0.0) * float(v)
      #end for

      down_ll *= A.annealing
      p_down = np.exp(down_ll - np.log1p(np.exp(down_ll)))
      if p_down < 1e-12: p_down = 1e-12
      if p_down >= 1.0 - 1e-12: p_down = 1.0 - 1e-12
      # p_down = 1-1e-12 if label == 'r_down' else 1e-12
      instances[d][stock] = p_down
      gold_labels[d][stock] = -1 if label == 'r_down' else 1
    #end for
  #end for

  for i, (d, instance) in enumerate(instances.iteritems()):
    for stock in STOCK_LIST:
      if stock not in instance:
        instance[stock] = 0.5

    yield d, instance
  #end for
#end def

if __name__ == '__main__':
  utf8_output_file = lambda fname: codecs.open(fname, 'w', 'utf-8')
  utf8_input_file = lambda fname: codecs.open(fname, 'r', 'utf-8', errors='ignore')

  parser = argparse.ArgumentParser(description='Train/test stock prediction ')
  subparsers = parser.add_subparsers(title='Available modes', description='Select the desired mode', help='Use <mode> -h for more usage details.', dest='mode')

  parser_inference = subparsers.add_parser('inference', help='Do inference in MRF model.')
  parser_inference.add_argument('model_file', type=utf8_input_file, metavar='model_file', help='Save model here.')
  parser_inference.add_argument('weights_dir', type=str, metavar='weights_dir', help='Directory containing CREG weights file (to compute unary factors).')
  parser_inference.add_argument('test_dir', type=str, metavar='test_dir', help='Directory containing test instances.')
  parser_inference.add_argument('--iterations', type=int, metavar='gibbs_iter', default=3000, help='No. of Gibbs iteration to run.')
  parser_inference.add_argument('--flip', type=int, metavar='flip', default=1, help='No. of states to flip in the proposal distribution.')
  parser_inference.add_argument('--prune-entropy', type=float, metavar='H', default=0, help='Prune pairwise potentials whose entropy is larger than H.')
  parser_inference.add_argument('--annealing', type=float, metavar='annealing', default=1.5, help='Sharpen/Flatten the distribution of the unary factors.')
  parser_inference.add_argument('--num-threads', type=int, metavar='num_threads', default=12, help='No. of threads to use for inference.')
  # parser_inference.add_argument('--burnin', type=int, metavar='gibbs_iter', default=500, help='No. of Gibbs iteration to run.')

  parser_learning = subparsers.add_parser('learning', help='Train MRF model.')
  parser_learning.add_argument('train_file', type=utf8_input_file, metavar='train_file', help='Training instances.')
  parser_learning.add_argument('model_file', type=utf8_output_file, metavar='model_file', help='Save model here.')
  parser_learning.add_argument('--l2', type=float, default=0.001, metavar='lambda', help='L2 regularizer')

  A = parser.parse_args()

  sys.stdin = codecs.getreader('utf-8')(sys.stdin)
  sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
  sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

  if A.mode == 'learning': mrf_learning()
  elif A.mode == 'inference':
    gold_labels = collections.defaultdict(dict)

    instances, gold_labels = json.load(utf8_input_file('unary-factors-rand.json'))
    # instances.sort()
    # instance_ids = sorted(map(operator.itemgetter(0), instances))
    # for instance_id, unary_factors in instances:
    #   i = instance_ids.index(instance_id)
    #   if i > 0:
    #     assert instances[i][0] == instance_id
    #     for stock in STOCK_LIST:
    #       instances[i][1][stock] *= 1 if gold_labels[instance_ids[i - 1]][stock] == -1 else 0.5
    #   #edn if
    # end for
    # instances = random.sample(instances, 100)
    # instances = list(test_instances())
    # with utf8_output_file('unary-factors-rand.json') as f:
    #   print >>f, json.dumps([instances, gold_labels], indent=2)
    # sys.exit()
    results = mrf_inference(instances)
    # results = {}
    # instance_ids = sorted(map(operator.itemgetter(0), instances))
    # for instance_id, unary_factors in instances:
      # results[instance_id] = [(-1 if unary_factors[stock] > 0.5 else 1) for stock in STOCK_LIST]
      # i = instance_ids.index(instance_id)
      # if i > 0: results[instance_id] = [-gold_labels[instance_ids[i - 1]][stock] for stock in STOCK_LIST]
      # else: results[instance_id] = [1 for stock in STOCK_LIST]
      # #edn if
    #end for

    stock_count = len(STOCK_LIST)
    scores = np.zeros(len(results), dtype=np.float)
    confusion = np.zeros((len(results), 2), dtype=np.float)
    for i, (instance_id, state) in enumerate(sorted(results.iteritems())):
      correct, total = 0, 0
      down_correct, down_total = 0, 0
      for s_i in xrange(stock_count):
        if STOCK_LIST[s_i] not in gold_labels[instance_id]: continue
        if state[s_i] == gold_labels[instance_id][STOCK_LIST[s_i]]:
          correct += 1
          if state[s_i] == -1: down_correct += 1
        #end if
        if gold_labels[instance_id][STOCK_LIST[s_i]] == -1: down_total += 1
        total += 1
      #end for
      if total == 0:
        print >>sys.stderr, '{} has 0 stocks!'.format(instance_id)
        scores[i] = 1.0
      else:
        scores[i] = float(correct) / total
        if down_total > 0: confusion[i, 0] = float(down_correct) / down_total
        if total - down_total > 0: confusion[i, 1] = float(correct - down_correct) / (total - down_total)
      #end if
      print >>sys.stderr, '[{}] {}/{} = {:.4f}'.format(instance_id, correct, total, scores[i])
    #end for
    print >>sys.stderr, 'Average: {:.4f}, Down: {:.4f}, Up: {:.4f}'.format(np.mean(scores), np.mean(confusion[:, 0]), np.mean(confusion[:, 1]))
#end if
