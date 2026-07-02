##############################################################################################
#   Write a program which accepts one number and prints factorial of that number.
#   Input : 5
#   Output : 120
##############################################################################################

##############################################################
#
#  Function Name :     Factorial
#  Description :       Gives factorial of given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              01/01/2026
#
##############################################################
def Factorial(No):
    Fact = No

    for i in range(No-1,0,-1):
        Fact = Fact * i

    return Fact


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              01/01/2026
#
##############################################################
def main():
    
    print("Enter a number : ")
    Value = int(input())

    Ret = Factorial(Value)

    print(Ret)

if __name__ == "__main__":
    main()