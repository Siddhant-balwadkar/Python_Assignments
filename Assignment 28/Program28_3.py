############################################################################################
#   Q3) Display File Line by Line
#   Problem Statement :
#   Write a program which accepts a file name from the user and displays the contents of the
#   file line by line on the screen.
#   Input :
#   Demo.txt
#   Expected Output :
#   Display each line of Demo.txt one by one.
############################################################################################


############################################################################################
#
#  Function Name :     Display
#  Description :       Opens the specified file and prints its contents line by line.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def Display(FileName):
    try:
        with open(FileName,"r") as file:
            for line in file:
                print(line, end="")

    except Exception as eobj:
        print(f"An error occured : {eobj}")


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Accepts a file name input from the user
#                      and invokes the Display function.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def main():
    Value = input("Enter File Name : ")
    Display(Value)


############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()