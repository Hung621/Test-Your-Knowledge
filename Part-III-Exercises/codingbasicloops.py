s = "0NBAD79FG"
t = 0
l = []
for i in s:
    print("{0} -> {1}".format(i, ord(i)))
    t += ord(i)
    l.append(ord(i))
print(t)
print(l)


[ord(c) for c in s] # Có tương tự. 
