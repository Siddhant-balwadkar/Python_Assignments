############################################################################################
#   Write a lambda function which accepts one numbers and returns True if number is Even 
#   otherwise False.
#   Input : 2
#   Output : True
############################################################################################

##############################################################
#
#  Lambda Function Name :    ChkEven
#  Description :            Returns the True if number is Even otherwise False
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   05/07/2026
#
##############################################################
ChkEven = lambda No: (True if No % 2 == 0 else False)


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

    Ret = ChkEven(Value1)

    print(f"{Value1} is Even : {Ret}")

if __name__ == "__main__":
    main()