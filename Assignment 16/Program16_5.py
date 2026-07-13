############################################################################################
#   Write a program which display 10 to 1 on screen.
#   Input :  Nothing
#   Output : 10   9   8   7   6   5   4   3   2   1
############################################################################################


##############################################################
#
#  Function Name :          Display
#  Description :            Displays 10 to 1 on screen
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
def Display():
    no = 10
    
    while(no >= 1):
        print(no,end="\t")
        no = no - 1

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              06/07/2026
#
##############################################################
def main():
    Display()

if __name__ == "__main__":
    main()