############################################################################################
#   Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#   for subtraction, Mul() for multiplication and Div() for division. All functions accepts two
#   parameters as number and performs the operation. Write on python program which call all the
#   functions from Arithmetic module by accepting the parameters from user.
############################################################################################
from Arithmetic import *

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              13/07/2026
#
##############################################################
def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Add(Value1,Value2)
    print("Addition is :",Ret)

    Ret = Sub(Value1,Value2)
    print("Substraction is :",Ret)

    Ret = Mul(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret = Div(Value1,Value2)
    print("Division is :",Ret)


if __name__ == "__main__":
    main()