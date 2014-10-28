import json
import subprocess


# Trains a model and save it to `weights`.
def train((train_features, train_labels), weights=None, options={}, quiet=False):
    p = subprocess.Popen(['creg', '-x', train_features, '-y', train_labels] + (['-W'] if weights is None else ['--z', weights]) + [a for item in options.iteritems() for a in item if a], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, err = p.communicate()

    if p.returncode != 0:
        raise UserWarning('creg returned {}'.format(p.returncode))

    return output, err


# Train and evaluate. Does not store weights. Just returns a list of posteriors and their true labels.
def evaluate((train_features, train_labels), (test_features, test_labels), options={}):
    new_options = options
    new_options['--tx'] = test_features
    new_options['--ty'] = test_labels
    new_options['--write_test_distribution'] = ''
    weights = None
    if '--z' in options:
        weights = options['--z']
    del options['--z']

    ground_truth = {}
    with open(test_labels) as f:
        for line in f:
            key, label = line.strip('\n').split('\t')
            ground_truth[key] = label
    output, err = train((train_features, train_labels), weights=weights, options=new_options)

    posteriors = {}
    for line in output.split('\n'):
        if not line.strip():
            continue
    key, pred, posterior_json = line.strip().split('\t', 3)
    posteriors[key] = {'true_label': ground_truth[key], 'predicted_label': pred, 'posterior': json.loads(posterior_json)}

    return posteriors
