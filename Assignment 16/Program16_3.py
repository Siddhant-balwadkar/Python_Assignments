############################################################################################
#   Write a program which contains one function named as Add() which accept two numbers
#   from user and return addition of that two numbers.
#   Input :  11  5
#   Output : 16
############################################################################################


##############################################################
#
#  Function Name :          Add
#  Description :            Returns the addition of two numbers 
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
def Add(No1,No2):
    Ans = No1 + No2
    return Ans


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              06/07/2026
#
##############################################################
def main():
    Value1 = int(input("Enter first Number : "))
    Value2 = int(input("Enter second Number : "))
    
    Ret = Add(Value1,Value2)

    print(f"Addition of {Value1} and {Value2} is : {Ret}")

if __name__ == "__main__":
    main()