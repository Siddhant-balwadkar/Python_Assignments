############################################################################################
#   Write a program which display 5 times Marvellous on screen.
#   Input :  Nothing
#   Output : Marvellous
#            Marvellous
#            Marvellous
#            Marvellous
#            Marvellous
############################################################################################


##############################################################
#
#  Function Name :          Display
#  Description :            Displays "Marvellous" 5 times
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
def Display():
    no = 1
    
    while(no <= 5):
        print("Marvellous")
        no = no + 1

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