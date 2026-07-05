############################################################################################
#   Write a lambda function which accepts one number and returns square of that number.
#   Input : 5
#   Output : 25
############################################################################################

##############################################################
#
#  Lambda Function Name :    SquareNum
#  Description :            Calculates the square of a number
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   05/07/2026
#
#############################################################
SquareNum = lambda No: (No*No)


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              05/07/2026
#
##############################################################
def main():
    Value1 = int(input("Enter the number : "))

    Ret = SquareNum(Value1)

    print(f"Square of {Value1} is : {Ret}")

if __name__ == "__main__":
    main()