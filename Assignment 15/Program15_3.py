############################################################################################
#   Write a lambda function using filter() which accepts a list of numbers and returns
#   a list of odd numbers.
#   Input : [1, 2, 3, 4, 5]
#   Output : [1, 3, 5]
############################################################################################

##############################################################
#
#  Lambda Function Name :   OddNumbers
#  Description :            Returns the odd numbers from a list using filter() function
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
OddNumbers = lambda No: list(filter(lambda x: x % 2 != 0, No))


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

    Ret = OddNumbers(Value1)

    print(f"The odd numbers are : {Ret}")

if __name__ == "__main__":
    main()