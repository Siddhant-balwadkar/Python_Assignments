############################################################################################
#   Write a program which contains filter(), map(), reduce() in it. Python application which
#   contains one list of numbers. List contains the numbers which are accepted from user. Filter
#   should filter out all such numbers which are even. Map function will calculate its square.
#   Reduce will return addition of that numbers.
#   Input List :    [5,2,3,4,3,4,1,2,8,10]
#   List after filter : [2,4,4,2,8,10]
#   List after map :    [4,16,16,4,64,100]
#   Output of reduce :  204
#
############################################################################################
from functools import reduce

##############################################################
#
#  Function Name :     ChkEven
#  Description :       Checks even number from list
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def ChkEven(Brr):
    return Brr % 2 == 0

##############################################################
#
#  Function Name :     CalSquare
#  Description :       Calculate square of number from list
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def CalSquare(Brr):
    return Brr ** 2


##############################################################
#
#  Function Name :     Addition
#  Description :       gives addition of given list
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def Addition(No1, No2):
    return No1 + No2


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

    fdata = list(filter(ChkEven,Arr))
    print("List after filter = ",fdata)

    mdata = list(map(CalSquare,fdata))
    print("List after map = ",mdata)

    rdata = reduce(Addition,mdata)
    print("Output of reduce is :",rdata)

if __name__ == "__main__":
    main()