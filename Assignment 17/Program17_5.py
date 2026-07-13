############################################################################################
#   Write a program which accept one number from user and return addition of its factors.
#   Input :  12
#   Output : 16     (1+2+3+4+6)
############################################################################################


##############################################################
#
#  Function Name :          ChkPrime
#  Description :            Checks the given number is a prime number or not
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   13/07/2026
#
##############################################################
def ChkPrime(No):
    
    for i in range(2,No):
        if(No%i == 0):
            return False
    
    return True


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

    Ret = ChkPrime(Value)

    if(Ret == True):
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()