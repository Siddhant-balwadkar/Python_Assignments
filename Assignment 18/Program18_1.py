############################################################################################
#   Write a program which accept N number from user and return addition of all elements from
#   that list.
#   Input :  Number of elements : 6
#   Input Elements : 13   5   45  7   4   56
#   Output : 130
#
############################################################################################


##############################################################
#
#  Function Name :          AddList
#  Description :            return addition of all elements from
#                           that list.
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   14/07/2026
#
##############################################################
def AddList(No):
    Sum = 0
    for i in No:
        Sum = Sum + i
    
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
    # Value2 = list(map(int,input("Enter elements : ").split()))
    for i in range(1,Value1+1):
        Element = int(input(f"Number of elements {i} : "))
        Value2.append(Element)

    Ret = AddList(Value2)

    print("Addition of List is :",Ret)

if __name__ == "__main__":
    main()