############################################################################################
#   Write a program which contains one function named as ChkNum() which accept one parameter
#   as number. If number is even then it should display "Even Number" otherwise display "Odd Number"
#   on console
#   Input :  11
#   Output : Odd Number
#   Input :  8
#   Output : Even Number
############################################################################################


##############################################################
#
#  Function Name :          ChkNum
#  Description :            Displays Hello from Fun on console
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
def ChkNum(No):
    if(No % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              06/07/2026
#
##############################################################
def main():
    Value1 = int(input("Enter the Number : "))

    ChkNum(Value1)

if __name__ == "__main__":
    main()