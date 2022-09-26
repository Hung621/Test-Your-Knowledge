def adder(good, bad, ugly):
     a = good, bad, ugly
     return a

good = {"a": 5, "b": 6}
bad = 5
ugly = [1,3,3]
print(adder(good, bad, ugly))



def adder(**args): print(args.keys())

adder(ugly=1, good=2)
