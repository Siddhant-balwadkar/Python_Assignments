############################################################################################
#   Write a program which contains one lambda function which accepts one parameters and return
#   power of two.
#   Input :  4
#   Output : 16
#   Input : 6
#   Output : 64
#
############################################################################################


##############################################################
#
#  lambda Function Name :   Power
#  Description :            Returns power of two of given number
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   18/07/2026
#
##############################################################
Power = lambda No: 2 ** No


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def main():
    Value = int(input("Enter the number : "))

    Ret = Power(Value)

    print(f"Power of {Value} is :",Ret)

if __name__ == "__main__":
    main()