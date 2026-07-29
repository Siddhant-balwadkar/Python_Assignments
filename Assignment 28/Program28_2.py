############################################################################################
#   Q2) Count Words in a File
#   Problem Statement :
#   Write a program which accepts a file name from the user and counts total number of words
#   in that file.
#   Input :
#   Demo.txt
#   Expected Output :
#   Total number of words in Demo.txt.
############################################################################################


############################################################################################
#
#  Function Name :     Count
#  Description :       Opens the specified file, reads its contents, and prints the 
#                      total word count.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def Count(FileName):
    try:
        with open(FileName,"r") as word:
            text = word.read()

        wordcount = len(text.split())

        print(f"Total Number of words in {FileName} are : {wordcount}")
    except Exception as eobj:
        print(f"An error occured : {eobj}")


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Accepts a file name input from the user
#                      and invokes the Count function.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def main():
    Value = input("Enter File Name : ")
    Count(Value)


############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()