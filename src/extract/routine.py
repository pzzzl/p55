import os
from src.log import logger

def run(path):
    extracted = path + '/extracted'

    directories = list(os.walk(path))

    directories_len = len(directories)
    logger.info('Analyzing %s directories...' % directories_len)

    # STATISTICS
    EXTRACTED_FILES = 0
    DUPLICATED_FILES = 0
    duplicates = []

    for folder_structure in directories:

        current_directory = folder_structure[0]
        folders = folder_structure[1]
        files = folder_structure[2]

        logger.info("Current directory: " + str(current_directory))
        logger.info("Folders: " + str(folders))
        logger.info("Files: " + str(files))

        if folder_structure == extracted:
            pass
        else:
            for file_name in folder_structure[2]:
                file_path = current_directory + '/' + file_name
                destination = extracted + '/' + file_name
                try:
                    logger.info('Moving file "' + file_name + '"')
                    # os.replace(file_path, destination)
                    os.rename(file_path, destination)
                    EXTRACTED_FILES += 1
                except PermissionError:
                    logger.info('Failed to move file "' + file_name + '": being used by another process')
                except FileExistsError:
                    logger.info('File "' + file_name + '" already exists')
                    duplicates.append(file_path)
                    DUPLICATED_FILES += 1
                    pass

    for duplicate in duplicates:
        logger.info('DUPLICATE: "' + duplicate + '"')

    logger.info("THE SCRIPT FOUND " + str(DUPLICATED_FILES) + " DUPLICATED FILES!")
    logger.info("EXTRACTED FILES: " + str(EXTRACTED_FILES))
    logger.info("FINISHED SUCCESFULLY!")