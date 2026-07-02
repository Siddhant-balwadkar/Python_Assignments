###############################################################
#   Write a program which accepts one number and prints its factors.
#   Input : 12
#   Output : 1 2 3 4 6 12
############################################################### 

##############################################################
#
#  Function Name :     CheckFactors
#  Description :       Find Factors of given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def CheckFactors(No):
    factors = []

    for i in range(1, No + 1):
        if No % i == 0:
            factors.append(i)

    return factors


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def main():
    
    print("Enter a number : ")
    iNo = int(input())

    Ret = CheckFactors(iNo)

    print("Factors of",iNo,"are",Ret)


if __name__ == "__main__":
    main()

##############################################
#   OUTPUT :
#
#   Enter a number :
#   12
#   Factors of 12 are [1, 2, 3, 4, 6, 12]
#
# ##############################################