import os
import sys
from shutil import move

arguments_len = len(sys.argv)

if(arguments_len < 2):
    print('\n"PATH" needs to be specified.\nCommand structure: python extract.py "C:/path_to_the_extractable_folder"')
    exit()
elif(arguments_len > 2):
    print('\nOnly ONE argument is required: "PATH"\nCommand structure: python extract.py "C:/path_to_the_extractable_folder"')
    exit()
elif(arguments_len == 2):
    path = sys.argv[1]
else:
    print("\nIncorrect arguments structure.\nRead full documentation at https://github.com/pzzzl/py-extract")
    exit()

print("https://github.com/pzzzl/py-extract")

if(not os.path.isdir(path)):
    print("PATH doesn't exists")
    exit()

print('\nAre you sure you want to extract all files from the folder "' + path + '" into a single folder "extracted"?')
print("\n0. No\n1. Yes")
answer = input("Option: ")

while(answer != "1" and answer != "0"):
    print("The given option " + answer + " is invalid")
    answer = input("Option: ")

if(answer == "0"):
    print("\nFinishing script...")
    exit()

extracted = path + '/extracted'

if(not os.path.isdir(extracted)):
    try:
        print("Creating folder " + extracted)
        os.mkdir(extracted)
    except:
        print("Error creating the specified folder. Finishing script...")
        exit()
else:
    print("The folder " + extracted + " already exists")

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