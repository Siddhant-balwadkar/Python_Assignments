############################################################################################
#   Write a lambda function using map() which accepts a list of numbers and returns
#   a list of squares of each number.
#   Input : [1, 2, 3, 4, 5]
#   Output : [1, 4, 9, 16, 25]
############################################################################################

##############################################################
#
#  Lambda Function Name :    Square
#  Description :            Returns the square of a list of numbers using map() function
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
Square = lambda No: list(map(lambda X: X ** 2,No))


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
    Value1 = list(map(int, input("Enter the numbers : ").split(",")))      #.split(",") is used to split the input string 
                                                                           # into a list of numbers based on the comma separator.


    Ret = Square(Value1)

    print(f"The squares is : {Ret}")

if __name__ == "__main__":
    main()