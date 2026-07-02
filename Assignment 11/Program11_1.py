##############################################################################################
#   Write a program which accepts one number and checks whether it is prime or not.
#   Input : 11
#   Output : Prime Number
##############################################################################################

##############################################################
#
#  Function Name :     CheckPrime
#  Description :       Checks whether the given number is prime or not
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def CheckPrime(No):
    if(No<=1):
        return False
    
    result = No ** 0.5
    for i in range(2,int(result)+1):
        if(No%i == 0):
            return False
    
    return True


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

    Ret = CheckPrime(Value)

    if(Ret == True):
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

if __name__ == "__main__":
    main()