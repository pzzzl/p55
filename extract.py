import os
from shutil import move

dir = os.getcwd()
extracted = dir+'/extracted'

try:
    os.chdir(extracted)
    os.chdir(dir)
except:
    os.mkdir(extracted)

list = list(os.walk(dir))

rootAmount = len(list)

print('\nAnalyzing %s directories...' % rootAmount)

for l in list:
    print('\n')
    nextDir = l[0]
    folders = l[1]
    files = l[2]
    print(files)

    if l == extracted:
        os.chdir(extracted)
        os.chdir(dir)
    else:
        for f in l[2]:
            file = nextDir+'/'+f
            destination = extracted+'/'+f
            try:
                os.replace(file, destination)
            except PermissionError:
                print('\nFailed to move file "%s": being used by another process.\n' % f)
            except FileExistsError:
                os.chdir(extracted)
                os.chdir(dir)
