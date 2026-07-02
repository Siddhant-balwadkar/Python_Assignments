##############################################################################################
#   Write a program which accepts one number and prints count of digits in that number.
#   Input : 7521
#   Output : 4
##############################################################################################

##############################################################
#
#  Function Name :     CountDigits
#  Description :       Counts the number of digits in the given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def CountDigits(No):
    Count = 0

    while(No != 0):
        Count = Count + 1           # 1 -> 2 -> 3 -> 4
        Digits = No%10              # 7521 -> 1 -> 2 -> 3 -> 4
        No = No // 10               # 7521 -> 752 -> 75 -> 7 -> 0

    return Count

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

    Ret = CountDigits(Value)

    print("Number of digits count is :", Ret)

if __name__ == "__main__":
    main()