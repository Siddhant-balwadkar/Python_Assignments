############################################################################################
#   Write a lambda function which accepts one numbers and returns True if number is Odd 
#   otherwise False.
#   Input : 2
#   Output : True
############################################################################################

##############################################################
#
#  Lambda Function Name :    ChkOdd
#  Description :            Returns the True if number is Odd otherwise False
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   05/07/2026
#
##############################################################
ChkOdd = lambda No: (True if No % 2 != 0 else False)


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

    Ret = ChkOdd(Value1)

    print(f"{Value1} is Odd : {Ret}")

if __name__ == "__main__":
    main()