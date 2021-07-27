import os
from shutil import move
from src.log import logger

def run(path):
    dir = path
    folder = dir + '/organized'

    # ASSIGN ARRAY OF FILES IN THE CURRENT DIRECTORY
    files = os.listdir(dir)

    # WHAT REMAINS AFTER PROCESSING
    files.remove('organized')

    # MOVES FILES TO ORGANIZED FOLDER
    for f in files:
        file = dir + '/' + f
        destination = folder + '/' + f
        try:
            os.replace(file, destination)
        except PermissionError:
            logger.info('\nFailed to move file "%s": being used by another process.\n' % f)

    # FOCUS ON NEW FOLDER
    os.chdir(folder)

    # ASSIGN ARRAY OF FILES IN THE DESIGNATED DIRECTORY
    organized = os.listdir()

    #GENERATE FOLDER STRUCTURE
    for f in organized:
        # VARIABLE
        file = folder + '/' + f

        # EXTRACTS EXTENSION FROM FILE
        file, file_extension = os.path.splitext(file)

        # GENERATE FOLDER FOT CERTAIN EXTENSION IF FILE ISN'T A FOLDER
        try:
            if file_extension != '':
                os.mkdir(file_extension)
        except FileExistsError:
            os.chdir(folder)

        # MATCHES DESTINATION WITH DATA TYPE
        destination = folder + '/' + file_extension + '/'

        # FINALLY MOVES FILE TO IT'S DESTINATION
        try:
            move(folder + '/' + f, destination)
        except:
            logger.info('"%s" already exists.' % f)
        logger.info(file_extension)