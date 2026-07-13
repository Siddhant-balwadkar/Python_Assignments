############################################################################################
#   Write a program which display first 10 even numbers on screen.
#   Input :  Nothing
#   Output : 2   4   6   8   10  12  14  16  18  20
############################################################################################


##############################################################
#
#  Function Name :          PrintEvenNumbers
#  Description :            Prints the first 10 even numbers
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
def PrintEvenNumbers():
    No = 1
    Count = 0

    while Count < 10:
        if No % 2 == 0:
            print(No,end="\t")
            Count = Count + 1
        
        No = No + 1
    

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              06/07/2026
#
##############################################################
def main():
    PrintEvenNumbers()

if __name__ == "__main__":
    main()