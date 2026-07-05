############################################################################################
#   Write a lambda function which accepts two numbers and returns multiplication.
#   Input : 25, 15
#   Output : 375
############################################################################################

##############################################################
#
#  Lambda Function Name :    Multiplication
#  Description :            Returns the Multiplication of two numbers
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
Multiplication = lambda No1, No2: No1 * No2


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

    Ret = Multiplication(Value1, Value2)

    print(f"Multiplication of {Value1} and {Value2} is : {Ret}")

if __name__ == "__main__":
    main()