############################################################################################
#   Write a program which accept number from user and return number of digits in that number.
#   Input :  5187934
#   Output : 7
#
############################################################################################


##############################################################
#
#  Function Name :          CalDigits
#  Description :            return number of digits in that number
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   13/07/2026
#
##############################################################
def CalDigits(No):
    Digits = 0
    
    while(No != 0):
        No = No // 10
        Digits = Digits + 1

    return Digits

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

    print("Total digits are :",Ret)

if __name__ == "__main__":
    main()