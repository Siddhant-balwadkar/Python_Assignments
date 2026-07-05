############################################################################################
#   Write a lambda function which accepts two numbers and returns addition.
#   Input : 25, 15
#   Output : 40
############################################################################################

##############################################################
#
#  Lambda Function Name :    Addition
#  Description :            Returns the Addition of two numbers
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
Addition = lambda No1, No2: No1 + No2


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              05/07/2026
#
##############################################################
def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Addition(Value1, Value2)

    print(f"Addition of {Value1} and {Value2} is : {Ret}")

if __name__ == "__main__":
    main()