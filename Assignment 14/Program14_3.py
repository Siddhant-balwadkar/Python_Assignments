############################################################################################
#   Write a lambda function which accepts two numbers and returns maximum number.
#   Input : 5 10
#   Output : 10
############################################################################################

##############################################################
#
#  Lambda Function Name :    MaxNum
#  Description :            Returns the maximum number
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   05/07/2026
#
##############################################################
Maxnum = lambda No1,No2: (No1 if No1 > No2 else No2)


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

    Ret = Maxnum(Value1, Value2)

    print(f"Maximum of {Value1} and {Value2} is : {Ret}")

if __name__ == "__main__":
    main()