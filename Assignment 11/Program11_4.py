##############################################################################################
#   Write a program which accepts one number and prints reverse of that number.
#   Input : 123
#   Output : 321
##############################################################################################

##############################################################
#
#  Function Name :     ReverseNumber
#  Description :       Reverses the given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
###############################################################
def ReverseNumber(No):
    reverse = 0

    while(No != 0):
        Digits = No % 10                    # 123 -> 3 -> 2 -> 1
        reverse = (reverse * 10) + Digits   # 0 -> 3 -> 32 -> 321
        No = No // 10                       # 123 -> 12 -> 1 -> 0

    return reverse

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

    Ret = ReverseNumber(Value)

    print("Reverse of the number is :",Ret)

if __name__ == "__main__":
    main()