############################################################################################
#   Write a program which contains one lambda function which accepts two parameters and return
#   its multiplication.
#   Input :  4  3
#   Output : 12
#   Input : 6   3
#   Output : 18
#
############################################################################################


##############################################################
#
#  lambda Function Name :   Multi
#  Description :            Returns multiplication of given two number
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   18/07/2026
#
##############################################################
Multi = lambda No1, No2: No1 * No2 


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Multi(Value1, Value2)

    print(f"Multiplication of {Value1} and {Value2} is :",Ret)

if __name__ == "__main__":
    main()