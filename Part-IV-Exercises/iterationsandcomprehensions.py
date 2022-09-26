import math
ln = []
def sq(l):
    for i in l:
        squ = math.sqrt(i)
        ln.append(squ)
    print(ln)

l = [2, 4, 9, 16, 25]
sq(l)


ll = list(map(lambda x: math.sqrt(x), l))
print(ll)


a = [math.sqrt(i) for i in l]
print(a)
