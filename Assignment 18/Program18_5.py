############################################################################################
#   Write a program which accept N number from user and store it into List. Return addition of
#   all prime numbers from that list. Main python file accepts N number from user and pass
#   each number to ChkPrime() function which is part of our user-defined module named as 
#   MarvellousNum. Name of the function from main python file should be ListPrime()
#   Input :  Number of elements : 11
#   Input Elements : 13   5   45  7  4  56  10  34  2  5  8
#   Output : 32(13+5+7+2+5)
#
############################################################################################
import MarvellousNum

##############################################################
#
#  Function Name :          ListPrime
#  Description :            Find frequency of that number from List
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   14/07/2026
#
##############################################################
def ListPrime(Data):
    Sum = 0

    for Value in Data:
        if MarvellousNum.ChkPrime(Value):
            Sum = Sum + Value

    return Sum


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              14/07/2026
#
##############################################################
def main():
    Arr = []

    Size = int(input("Enter number of elements : "))

    for i in range(1,Size+1):
        No = int(input(f"Enter the elements {i} : "))
        Arr.append(No)

    Ret = ListPrime(Arr)

    print("Addition of prime numbers is :",Ret)

if __name__ == "__main__":
    main()