############################################################################################
#   Write a lambda function using filter() which accepts a list of numbers and returns the count 
#   of even numbers.
#   Input : [1, 2, 3, 4, 5]
#   Output : 2
############################################################################################
from functools import reduce

##############################################################
#
#  Lambda Function Name :   CountEvenNumbers
#  Description :            Returns the count of even numbers in a list using filter() function
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
CountEvenNumbers = lambda No: len(list(filter(lambda x: x % 2 == 0, No)))


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

    Ret = CountEvenNumbers(Value1)

    print(f"The count of even numbers is : {Ret}")

if __name__ == "__main__":
    main()