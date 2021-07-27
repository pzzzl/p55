import os
from shutil import move
from src.log import logger

def run(path):
    organized_path = path + '/organized'
    files = os.listdir(path)
    logger.info("Files: " + str(files))
    files.remove('organized')

    for file in files:
        file_path = path + '/' + file
        destination = organized_path + '/' + file
        try:
            os.replace(file_path, destination)
        except PermissionError:
            logger.info('\nFailed to move file "%s": being used by another process.\n' % file)

    os.chdir(organized_path)
    organized_files = os.listdir()

    for file in organized_files:
        file_path = organized_path + '/' + file
        file_path, file_extension = os.path.splitext(file_path)

        try:
            if file_extension != '':
                os.mkdir(file_extension)
        except FileExistsError:
            os.chdir(organized_path)

        destination = organized_path + '/' + file_extension + '/'

        try:
            logger.info("Moving " + file + " to " + destination)
            move(organized_path + '/' + file, destination)
        except:
            logger.info('"%s" already exists.' % file)