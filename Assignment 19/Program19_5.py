############################################################################################
#   Write a program which contains filter(), map(), reduce() in it. Python application which
#   contains one list of numbers. List contains the numbers which are accepted from user. Filter
#   should filter out all prime numbers. Map function will multiply each number by 2.
#   Reduce will return Maximum number from that numbers. (You can also use normal functions
#   instead of lambda functions)
#   Input List :    [2, 70, 11, 10, 17, 23, 31, 77]
#   List after filter : [2, 11, 17, 23, 31]
#   List after map :    [4, 22, 34, 46, 62]
#   Output of reduce :  62
#
############################################################################################
from functools import reduce

##############################################################
#
#  Function Name :     ChkPrime
#  Description :       Checks Prime number from list
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def ChkPrime(No):

    if(No <= 1):
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if(No % i == 0):
            return False

    return True             


##############################################################
#
#  Function Name :     Mult
#  Description :       Multiply each number from list by 2
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def Mult(Brr):
    return Brr * 2


##############################################################
#
#  Function Name :     Max
#  Description :       gives Maximum number from list
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def Max(No1, No2):
    if(No1 > No2):
        return No1
    else:
        return No2


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def main():
    Arr = []
    Size = int(input("Enter number of elements in list : "))

    for i in range(Size):
        print(f"Enter element {i+1} : ",end=" ")
        Value = int(input())
        Arr.append(Value)

    fdata = list(filter(ChkPrime,Arr))
    print("List after filter = ",fdata)

    mdata = list(map(Mult,fdata))
    print("List after map = ",mdata)

    rdata = reduce(Max,mdata)
    print("Output of reduce is :",rdata)

if __name__ == "__main__":
    main()