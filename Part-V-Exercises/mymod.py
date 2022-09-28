def countLines(name):
    file = open(name)
    return len(file.readlines())

def countChars(name):
    return len(open(name).read())

def test(name):
    return countLines(name),countChars(name)

def countLines(name):
    tot = 0
    for line in open(name): tot += 1
    return tot

def countChars(name):
    tot = 0
    for line in open(name): tot += len(line)
    return tot


def countlines(name): return sum(+1 for line in open(name))
def countchars(name): return sum(len(line) for line in open(name))

if __name__ == '__main__':
    print(test('mymod.py'))
