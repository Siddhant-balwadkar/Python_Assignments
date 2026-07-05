############################################################################################
#   Write a lambda function which accepts one numbers and returns True if divisible by 5.
#   Input : 25
#   Output : True
############################################################################################

##############################################################
#
#  Lambda Function Name :    ChkDivisible
#  Description :            Returns the True if number is divisible by 5 otherwise False
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   05/07/2026
#
##############################################################
ChkDivisible = lambda No: (True if No % 5 == 0 else False)


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

    Ret = ChkDivisible(Value1)
    
    print(f"{Value1} is divisible by 5 : {Ret}")

if __name__ == "__main__":
    main()