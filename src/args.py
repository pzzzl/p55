import os
import sys

def verify_path():
    arguments_len = len(sys.argv)

    if(arguments_len < 2):
        print('\n"PATH" needs to be specified.\nCommand structure: python extract.py "C:/path_to_the_extractable_folder"')
        exit()
    elif(arguments_len > 2):
        print('\nOnly ONE argument is required: "PATH"\nCommand structure: python extract.py "C:/path_to_the_extractable_folder"')
        exit()
    elif(arguments_len == 2):
        path = sys.argv[1]
        if(not os.path.isdir(path)):
            print("The specified path doesn't exists: " + path)
            exit()
        else:
            return path
    else:
        print("\nIncorrect arguments structure.\nRead full documentation at https://github.com/pzzzl/py-extract")
        exit()