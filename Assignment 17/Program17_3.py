############################################################################################
#   Write a program which accept one number from user and return its factorial.
#   Input :  5
#   Output : 120
############################################################################################


##############################################################
#
#  Function Name :          Factorial
#  Description :            Find Factorial of a given number
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   13/07/2026
#
##############################################################
def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              13/07/2026
#
##############################################################
def main():
    Value = int(input("Enter the number : "))

    Ret = Factorial(Value)

    print("Factorial is :",Ret)

if __name__ == "__main__":
    main()