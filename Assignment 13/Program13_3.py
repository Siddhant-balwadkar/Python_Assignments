##############################################################################################
#   Write a program which accepts one number and checks whether it is perfect number or not.
#   Input : 6
#   Output : Perfect number
##############################################################################################

##############################################################
#
#  Function Name :     CheckPerfect
#  Description :       Checks whether a number is a perfect number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def CheckPerfect(No):
    Result = 0

    for i in range(1,No):
        if(No%i == 0):
            Result = Result + i

    if(Result == No):
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

    Ret = CheckPerfect(Value)

    if(Ret == True):
        print("It is a perfect number")
    else:
        print("Its is not a perfect number")

if __name__ == "__main__":
    main()
