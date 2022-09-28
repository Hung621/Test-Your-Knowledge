# Find the largest Python source file in an entire directory tree
import sys, os, pprint
if sys.platform[:3] == 'win':
    dirname = r'C:\Python33\Lib'
else:
    dirname = '/usr/lib/python'
allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    for filename in filesHere:
        if filename.endswith('.py'):
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))
allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
