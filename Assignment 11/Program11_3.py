##############################################################################################
#   Write a program which accepts one number and prints sum of digits.
#   Input : 123
#   Output : 6
##############################################################################################

##############################################################
#
#  Function Name :     SumOfDigits
#  Description :       Calculates the sum of digits in the given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def SumOfDigits(No):
    Sum = 0

    while(No != 0):
        Digits = No%10              # 123 -> 3 -> 2 -> 1
        Sum = Sum + Digits          # 3 -> 3 + 2 -> 5 + 1 -> 6   
        No = No // 10               # 123 -> 12 -> 1 -> 0

    return Sum

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def main():
    
    print("Enter a number : ")
    Value = int(input())

    Ret = SumOfDigits(Value)

    print("Sum of digits is :",Ret)

if __name__ == "__main__":
    main()