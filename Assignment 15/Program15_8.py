############################################################################################
#   Write a lambda function using filter() which accepts a list of numbers and returns a list 
#   of numbers divisible by both 3 and 5.
#   Input : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 30]
#   Output : [15, 30]
############################################################################################
from functools import reduce

##############################################################
#
#  Lambda Function Name :   Divisible
#  Description :            Returns the numbers divisible by both 3 and 5 from a list using filter() function
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
Divisible = lambda No: list(filter(lambda x: (x % 3 == 0) and (x % 5 == 0), No))


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

    Ret = Divisible(Value1)

    print(f"The numbers divisible by both 3 and 5 are : {Ret}")

if __name__ == "__main__":
    main()