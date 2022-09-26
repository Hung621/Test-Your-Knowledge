import collections
D = {'spam': 2, 'ham': 1, 'eggs': 3}
DD = collections.OrderedDict(sorted(D.items()))
for k, v in DD.items(): print(k,":",v)
