############################################################################################
#   Write a lambda function using filter() which accepts a list of strings and returns a list 
#   of strings having length greater than 5.
#   Input : ["apple", "banana", "cherry", "date", "elderberry"]
#   Output : ["banana", "cherry", "elderberry"]
############################################################################################
from functools import reduce

##############################################################
#
#  Lambda Function Name :   GreaterStrings
#  Description :            Returns the strings having length greater than 5 from a list using filter() function
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
GreaterStrings = lambda No: list(filter(lambda x: len(x) > 5, No))


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
    Value1 = input("Enter the strings : ").split(",")

    Ret = GreaterStrings(Value1)

    print(f"The strings with length greater than 5 are : {Ret}")

if __name__ == "__main__":
    main()