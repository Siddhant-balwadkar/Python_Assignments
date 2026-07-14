############################################################################################
#   Write a program which accept N number from user and store it into List. Return Minimum
#   number from that list.
#   Input :  Number of elements : 4
#   Input Elements : 13   5   45  7
#   Output : 5
#
############################################################################################


##############################################################
#
#  Function Name :          MaxList
#  Description :            Finds Minimum number from the list
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   14/07/2026
#
##############################################################
def MaxList(No):
    Sum = No[0]

    for i in No:
        if(Sum > i):
            Sum = i
    
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
    Value1 = int(input("Number of elements : "))
    Value2 = []
    # Value2 = list(map(int,input("Input elements : ").split()))
    for i in range(1,Value1+1):
        Element = int(input(f"Input elements {i} : "))
        Value2.append(Element)

    Ret = MaxList(Value2)

    print("Minimum element from List is :",Ret)

if __name__ == "__main__":
    main()