def copyDict(dict):
    x = dict.keys()
    return x
        
print(copyDict({1:8, 2:9, 3:10}))

def addDict(dict1, dict2):
    d = dict(dict1)
    d.update(dict2)
    return d

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(addDict(dict1,dict2))
