############################################################################################
#   Write a lambda function using reduce() which accepts a list of numbers and returns maximum element.
#   Input : [1, 2, 3, 4, 5]
#   Output : 5
############################################################################################
from functools import reduce

##############################################################
#
#  Lambda Function Name :   MaxNumber
#  Description :            Returns the maximum number in a list using reduce() function
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
MaxNumber = lambda No: reduce(lambda x, y: (x if x > y else y), No)


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              05/07/2026
#
##############################################################
def main():
    Value1 = []
    Value1 = list(map(int, input("Enter the numbers : ").split(",")))

    Ret = MaxNumber(Value1)

    print(f"The maximum number is : {Ret}")

if __name__ == "__main__":
    main()