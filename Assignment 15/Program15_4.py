############################################################################################
#   Write a lambda function using reduce() which accepts a list of numbers and returns
#   the addition of all elements.
#   Input : [1, 2, 3, 4, 5]
#   Output : 15
############################################################################################
from functools import reduce

##############################################################
#
#  Lambda Function Name :   AddNumbers
#  Description :            Returns the sum of all numbers in a list using reduce() function
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
AddNumbers = lambda No: reduce(lambda x, y: x + y, No)


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
    Value1 = list(map(int, input("Enter the numbers : ").split(",")))   # map() is important to convert the input
                                                                        # string into a list of integers.

    Ret = AddNumbers(Value1)

    print(f"The sum of all numbers is : {Ret}")

if __name__ == "__main__":
    main()