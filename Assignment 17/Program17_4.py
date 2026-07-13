############################################################################################
#   Write a program which accept one number from user and return addition of its factors.
#   Input :  12
#   Output : 16     (1+2+3+4+6)
############################################################################################


##############################################################
#
#  Function Name :          AddFactors
#  Description :            Adds Factors of a given number
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   13/07/2026
#
##############################################################
def AddFactors(No):
    Result = 0

    for i in range(1,No):
        if(No%i == 0):
            Result = Result + i
    
    return Result


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

    Ret = AddFactors(Value)

    print("Addition of factors is :",Ret)

if __name__ == "__main__":
    main()