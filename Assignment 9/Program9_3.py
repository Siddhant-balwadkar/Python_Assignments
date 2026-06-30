##############################################################
#
#  Function Name :     Addition
#  Description :       Gives Addition of two numbers
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def Addition(No1, No2):
    Sum = 0

    Sum = No1 + No2
            
    return Sum


##############################################################
#
#  Function Name :     Subtraction
#  Description :       Gives Subtraction of two numbers
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def Subtraction(No1, No2):
    Sum = 0

    Sum = No1 - No2
            
    return Sum


##############################################################
#
#  Function Name :     Multiplication
#  Description :       Gives Multiplication of two numbers
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def Multiplication(No1, No2):
    Sum = 0

    Sum = No1 * No2
            
    return Sum

##############################################################
#
#  Function Name :     Division
#  Description :       Gives Division of two numbers
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def Division(No1, No2):
    Sum = 0

    Sum = No1 / No2
            
    return Sum


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def main():
    
    print("Enter a first number : ")
    Value1 = int(input())

    print("Enter a second number : ")
    Value2 = int(input())

    Ret = Addition(Value1, Value2)
    print("Addition is :",Ret)

    Ret = Subtraction(Value1, Value2)
    print("Subtraction is :",Ret)

    Ret = Multiplication(Value1, Value2)
    print("Multiplication is :",Ret)

    Ret = Division(Value1, Value2)
    print("Division is :",Ret)


if __name__ == "__main__":
    main()


##############################################
#   OUTPUT :
#
#   Enter a first number :
#   10
#   Enter a second number :
#   2
#   Addition is : 12
#   Subtraction is : 8
#   Multiplication is : 20
#   Division is : 5.0
#   
##############################################