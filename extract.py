import os
from shutil import move

#PATHS
dir = os.getcwd()
extracted = dir+'/extracted'

#CHECKS IF FOLDER EXISTS AND CREATES IT IF DON'T
try:
    os.chdir(extracted)
    os.chdir(dir)
except:
    os.mkdir(extracted)

#ASSIGN ARRAY <DIR NAME>, <LIST OF SUB DIRS>, <LIST OF FILES> INTO LIST
list = list(os.walk(dir))

#ASSIGN LIST SYZE TO ROOT AMOUNT AND PRINTS IT
rootAmount = len(list)
print('\nAnalyzing %s directories...' % rootAmount)

#GENERATE FOLDER STRUCTURE
for l in list:
    print('\n')

    #VARIABLE
    nextDir = l[0]
    folders = l[1]
    files = l[2]

    #LOG FOLDERS WHILE PROCESSING
    print(folders)

    #CASE IT ISN'T 'EXTRACTED', RECEIVES FILE AND DESTINATION TO FINALLY MOVE IT
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
