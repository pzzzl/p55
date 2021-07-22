import os

def run(path):
    extracted = path + '/extracted'

    directories = list(os.walk(path))

    directories_len = len(directories)
    print('Analyzing %s directories...' % directories_len)

    # STATISTICS
    EXTRACTED_FILES = 0
    DUPLICATED_FILES = 0
    duplicates = []

    for folder_structure in directories:

        current_directory = folder_structure[0]
        folders = folder_structure[1]
        files = folder_structure[2]

        print("\nCurrent directory: " + str(current_directory))
        print("Folders: " + str(folders))
        print("Files: " + str(files))

        if folder_structure == extracted:
            pass
        else:
            for file_name in folder_structure[2]:
                file_path = current_directory + '/' + file_name
                destination = extracted + '/' + file_name
                try:
                    print('Moving file "' + file_name + '"')
                    # os.replace(file_path, destination)
                    os.rename(file_path, destination)
                    EXTRACTED_FILES += 1
                except PermissionError:
                    print('Failed to move file "' + file_name + '": being used by another process')
                except FileExistsError:
                    print('File "' + file_name + '" already exists')
                    duplicates.append(file_path)
                    DUPLICATED_FILES += 1
                    pass

    print("\n")
    for duplicate in duplicates:
        print('DUPLICATE: "' + duplicate + '"')

    print("\nTHE SCRIPT FOUND " + str(DUPLICATED_FILES) + " DUPLICATED FILES!")
    print("EXTRACTED FILES: " + str(EXTRACTED_FILES))
    print("FINISHED SUCCESFULLY!")
    input("\nPress ENTER to continue...")