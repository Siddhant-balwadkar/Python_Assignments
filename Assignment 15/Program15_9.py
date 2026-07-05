############################################################################################
#   Write a lambda function using reduce() which accepts a list of numbers and returns the product 
#   of all numbers.
#   Input : [1, 2, 3, 4, 5]
#   Output : 120
############################################################################################
from functools import reduce

##############################################################
#
#  Lambda Function Name :   ProductNumbers
#  Description :            Returns the product of all numbers in a list using reduce() function
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
ProductNumbers = lambda No: reduce(lambda x, y: x * y, No)


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

    Ret = ProductNumbers(Value1)

    print(f"The product of all numbers is : {Ret}")

if __name__ == "__main__":
    main()