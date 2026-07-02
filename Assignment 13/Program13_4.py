##############################################################################################
#   Write a program which accepts one number and prints binary equivalent.
#   Input : 13
#   Output : 1101
##############################################################################################

##############################################################
#
#  Function Name :     ConvertBinary
#  Description :       Converts a number to its binary equivalent
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/01/2026
#
##############################################################
def ConvertBinary(No):
    Binary = 0
    Multiplier = 1

    while No > 0:
        Digit = No % 2
        Binary = Binary + (Digit * Multiplier)
        Multiplier = Multiplier * 10
        No = No // 2

    return Binary

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/01/2026
#
##############################################################
def main():
    
    print("Enter a number : ")
    Value = int(input())

    Ret = ConvertBinary(Value)

    print("Binary equivalent is :", Ret)

if __name__ == "__main__":
    main()