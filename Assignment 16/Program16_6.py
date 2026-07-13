############################################################################################
#   Write a program which accepts number from user and check whether that number is positive 
#   or negative or zero.
#   Input :  11
#   Output : Positive number
#   Input :  -8
#   Output : Negative number
#   Input :  0
#   Output : Zero
############################################################################################


##############################################################
#
#  Function Name :          CheckNum
#  Description :            Checks if a number is positive, negative, or zero
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
def CheckNum(No):
    if(No > 0):
        print("Positive Number")
    elif(No < 0):
        print("Negative Number")
    else:
        print("Zero")


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              06/07/2026
#
##############################################################
def main():
    Value1 = int(input("Enter the number : "))

    CheckNum(Value1)

if __name__ == "__main__":
    main()