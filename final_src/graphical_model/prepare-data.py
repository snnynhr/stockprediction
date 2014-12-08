import argparse
import collections
import codecs
import os
import json
import sys

from stock_list import STOCK_LIST

if __name__ == '__main__':
  utf8_output_file = lambda fname: codecs.open(fname, 'w', 'utf-8')
  utf8_input_file = lambda fname: codecs.open(fname, 'r', 'utf-8')

  parser = argparse.ArgumentParser(description='Prepares data for training.')
  # parser.add_argument('y_data', type=str, metavar='dir', help='Directory containing of \"date\tup/down\" labels for each stock in a file.')
  parser.add_argument('ticker_file', type=utf8_input_file, metavar='dir', help='Directory containing of \"date\tup/down\" labels for each stock in a file.')
  A = parser.parse_args()

  sys.stdin = codecs.getreader('utf-8')(sys.stdin)
  sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
  sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

  instances = collections.defaultdict(dict)
  stock_list = set()
  # for stock_fname in os.listdir(A.y_data):
  #   stock = os.path.splitext(stock_fname)[0]
  #   stock_list.add(stock)
  #   print >>sys.stderr, 'Processing {}...'.format(stock_fname)
  #   with utf8_input_file(os.path.join(A.y_data, stock_fname)) as f:
  #     for line in f:
  #       d, r = line.split(u'\t', 1)
  #       label = 1 if r == 'r_up' else -1
  #       instances[d][stock] = label
  #     #end for
  #   #end with
  # #end for

  stock_list = STOCK_LIST
  for line in A.ticker_file:
    ticker, o = line.split('\t', 1)
    if ticker not in STOCK_LIST: continue
    o = json.loads(o)
    last_p = 0.0
    for d, p in sorted(o.iteritems()):
      instances[d][ticker] = 1 if p > last_p else -1
      last_p = p
    #end for
  #end for

  print json.dumps({'stock_list': list(stock_list), 'stock_count': len(stock_list)})
  for i, (d, instance) in enumerate(sorted(instances.iteritems())):
    print '{}\t{}'.format(d, json.dumps(instance))
    # print >>sys.stderr, 'Day {}: {} stocks'.format(i, len(instance))
  # print stock_list
  # print len(stock_list)
#end if
