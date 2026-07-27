############################################################################################
#   Write a program which contains filter(), map(), reduce() in it. Python application which
#   contains one list of numbers. List contains the numbers which are accepted from user. Filter
#   should filter out all such numbers which are greater than or equal to 70 and less than or equal
#   to 90. Map function will increase each numbers by 10. Reduce will return product of all that
#   numbers.
#   Input List :    [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#   List after filter : [76, 89, 86, 90, 70]
#   List after map :    [86, 99, 96, 100, 80]
#   Output of reduce :  6538752000
#
############################################################################################
from functools import reduce

##############################################################
#
#  Function Name :     Between
#  Description :       Returns numbers greater than or equal 
#                      to 70 and less than or equal to 90 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def Between(Brr):
    return  Brr >= 70 and Brr <= 90

##############################################################
#
#  Function Name :     Increase
#  Description :       Increse the given number by 10 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def Increase(Brr):
    return Brr + 10


##############################################################
#
#  Function Name :     Product
#  Description :       gives product of the given list
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def Product(No1, No2):
    return No1 * No2


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

    fdata = list(filter(Between,Arr))
    print("List after filter = ",fdata)

    mdata = list(map(Increase,fdata))
    print("List after map = ",mdata)

    rdata = reduce(Product,mdata)
    print("Output of reduce is :",rdata)

if __name__ == "__main__":
    main()