##############################################################################################
#   Write a program which accepts one number and checks whether it is palindrome or not.
#   Input : 121
#   Output : It is a palindrome number
##############################################################################################

##############################################################
#
#  Function Name :     CheckPalindrome
#  Description :       Checks if the given number is a palindrome
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
###############################################################
def CheckPalindrome(No):
    reverse = 0
    Original = No

    while(No != 0):
        Digits = No % 10                    # 121 -> 1 -> 2 -> 1
        reverse = (reverse * 10) + Digits   # 0 -> 1 -> 12 -> 121
        No = No // 10                       # 121 -> 12 -> 1 -> 0

    if(reverse == Original):
        return True
    else:
        return False

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

    Ret = CheckPalindrome(Value)

    if(Ret == True):
        print("It is a Palindrome Number")
    else:
        print("It is not a Palindrome Number")

if __name__ == "__main__":
    main()