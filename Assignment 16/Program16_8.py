############################################################################################
#   Write a program which accepts number from user and print that number of "*" on screen.
#   Input :  5
#   Output : *   *   *   *   *
############################################################################################


##############################################################
#
#  Function Name :          PrintStars
#  Description :            Prints a specified number of stars
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
def PrintStars(No):
    while(No > 0):
        print("*",end="\t")
        No = No - 1   


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              06/07/2026
#
##############################################################
def main():
    Value1 = int(input("Enter the number : "))

    PrintStars(Value1)

if __name__ == "__main__":
    main()