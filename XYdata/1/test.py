import json

f = open("WMT.feat", 'w')
g = open("WMT.label", 'w')

for i, line in enumerate(open("WMT.json", "r").readlines()):
  o = json.loads(line)

  if not o[1]: continue

  label, featvec = o
  f.write('{}\t{}\n'.format(i, json.dumps(featvec)))
  g.write('{}\t{}\n'.format(i, label))
#end for
