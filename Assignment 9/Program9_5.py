##############################################################################################
#   Write a program which accepts one number and prints cube of that number
#   Input : 15
#   Output : Divisible by 3 and 5
##############################################################################################

##############################################################
#
#  Function Name :     CheckDivisibility
#  Description :       Checks whether the given number is divisible by 3 and 5 or not
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
###############################################################
def CheckDivisibility(No):
    
    if((No % 3 == 0) and (No % 5 == 0)):
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
    
    print("Enter first number : ")
    Values1 = int(input())


    Ret = CheckDivisibility(Values1)

    if(Ret == False):
        print("Not Divisible by 3 and 5")
    else:
        print("Divisible by 3 and 5")

if __name__ == "__main__":
    main()