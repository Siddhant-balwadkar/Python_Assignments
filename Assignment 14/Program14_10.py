############################################################################################
#   Write a lambda function which accepts three numbers and returns largest number.
#   Input : 25, 15, 30
#   Output : 30
############################################################################################

##############################################################
#
#  Lambda Function Name :    Largest
#  Description :            Returns the largest of three numbers
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
Largest = lambda No1, No2, No3: ((No1 if No1 > No2 and No1 > No3 else No3) if No1 > No2 else (No2 if No2 > No3 else No3))


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
    Value3 = int(input("Enter the third number : "))

    Ret = Largest(Value1, Value2, Value3)

    print(f"The largest of {Value1}, {Value2}, and {Value3} is : {Ret}")

if __name__ == "__main__":
    main()