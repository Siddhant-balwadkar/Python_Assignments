############################################################################################
#   Write a program which contains one function that accpets one number from user and returns
#   true if the numbers is divisible by 5 otherwise return false.
#   Input :  8
#   Output : False
#   Input :  25
#   Output : True
############################################################################################


##############################################################
#
#  Function Name :          CheckDivisibility
#  Description :            Checks if a number is divisible by 5
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
def CheckDivisibility(No):
    if(No % 5 == 0):
        return True
    else:
        return False   


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

    Ret = CheckDivisibility(Value1)

    print(Ret)

if __name__ == "__main__":
    main()