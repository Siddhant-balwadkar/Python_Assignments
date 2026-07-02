##############################################################################################
#   Write a program which accepts one number and prints square of that number
#   Input : 5
#   Output : 25
##############################################################################################

##############################################################
#
#  Function Name :     CalculateSquare
#  Description :       Calculates the square of the given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
###############################################################
def CalculateSquare(No):
    Square = No * No
    return Square   


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def main():
    
    print("Enter first number : ")
    Values1 = int(input())


    Ret = CalculateSquare(Values1)
    print("Square is :",Ret)

if __name__ == "__main__":
    main()