L = [5,6,8,9,11,20,25,88]
X = 9
found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i+1
if found:
    print('at index', i)
else:
    print(X, 'not found')



if X in L:
    print('at index', L.index(X))
else:
    print(X, 'not found')
