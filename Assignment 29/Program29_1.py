############################################################################################
#   Q1) Check File Exists in current Directory
#   Problem Statement :
#   Write a program which accepts a file name from the user and checks whether that file
#   exists in the current directory or not.
#   Input :
#   Demo.txt
#   Expected Output :
#   Display whether Demo.txt exists or not.
#############################################################################################
import os

############################################################################################
#
#  Function Name :     SearchFile
#  Description :       Opens the specified file, reads it line by line using a manual
#                      counter, and checks if the target word exists in the file.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def SearchFile(FileName):
    try:
        if(os.path.exists(FileName)):
            return True
        else:
            return False

    except Exception as eobj:
        print(f"There is no such file {FileName}")

############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Accepts file name and search word from
#                      the user and invokes the SearchWord function.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def main():
    File = input("Enter File Name : ")
    
    Ret = SearchFile(File)

    if(Ret == True):
        print(f"File {File} exists in the current directory.")
    else:
        print(f"File {File} does not exist in the current directory.")


############################################################################################
#
#           Starter of the main function
#
############################################################################################
if __name__ == "__main__":
    main()