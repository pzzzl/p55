import os

def confirm_processing(path):
    print('\nAre you sure you want to extract all files from the folder "' + path + '" into a single folder "extracted"?')
    
    print("0. No")
    print("1. Yes")

    answer = input("Option: ")
    
    while(answer != "1" and answer != "0"):
        print("The given option " + answer + " is invalid")
        answer = input("Option: ")

    if(answer == "0"):
        exit()

def check_structure(path):
    extracted = path + '/extracted'

    if(not os.path.isdir(extracted)):
        try:
            os.mkdir(extracted)
        except:
            print("Could not create folder " + extracted)
            exit()