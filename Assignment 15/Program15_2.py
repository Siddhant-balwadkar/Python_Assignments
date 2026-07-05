############################################################################################
#   Write a lambda function using filter() which accepts a list of numbers and returns
#   a list of even numbers.
#   Input : [1, 2, 3, 4, 5]
#   Output : [2, 4]
############################################################################################

##############################################################
#
#  Lambda Function Name :   EvenNumbers
#  Description :            Returns the even numbers from a list using filter() function
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
EvenNumbers = lambda No: list(filter(lambda x: x % 2 == 0, No))


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

    Ret = EvenNumbers(Value1)

    print(f"The even numbers are : {Ret}")

if __name__ == "__main__":
    main()