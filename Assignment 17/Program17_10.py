############################################################################################
#   Write a program which accept number from user and return addition of digits in that number.
#   Input :  5187934
#   Output : 37
#
############################################################################################


##############################################################
#
#  Function Name :          AddDigits
#  Description :            return number of digits in that number
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   13/07/2026
#
##############################################################
def CalDigits(No):
    sum = 0
    
    while(No > 0):
        Digits = No % 10                        # 5187934 % 10 = 4 
        sum = sum + Digits                      # 0 + 4
        No = No // 10                           # 5187934 // 10 = 518793

    return sum

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              13/07/2026
#
##############################################################
def main():
    Value = int(input("Enter the number : "))

    Ret = CalDigits(Value)

    print("Addition of digits is :",Ret)

if __name__ == "__main__":
    main()