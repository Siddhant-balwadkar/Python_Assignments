############################################################################################
#   Q1) Count Lines in a File
#   Problem Statement :
#   Write a program which accepts a file name from the user and counts how many lines are
#   present in the file
#   Input :
#   Demo.txt
#   Expected Output :
#   Total number of lines in Demo.txt.
############################################################################################


############################################################################################
#
#  Function Name :     Count
#  Description :       Opens the specified file, iterates through its contents line by line,
#                      and prints the total line count.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def Count(FileName):
    try:
        with open(FileName,"r") as file:
            lineCount = 0
            for line in file:
                lineCount += 1
        print(f"Total Number of Lines in {FileName} are : {lineCount}")
    except FileNotFoundError:
        print(f"ERROR: The file {FileName} not found.")


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