############################################################################################
#   Write a program which accept N number from user and store it into List. Accept one another
#   number from user and return frequency of that number from List.
#   Input :  Number of elements : 11
#   Input Elements : 13   5   45  7  4  56  5  34  2  5  65
#   Element to search : 5
#   Output : 3
#
############################################################################################


##############################################################
#
#  Function Name :          FrequencyNum
#  Description :            Find frequency of that number from List
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   14/07/2026
#
##############################################################
def FrequencyNum(No1, No2):
    Sum = 0

    for i in No1:
        if(No2 == i):
            Sum = Sum + 1
    
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
    
    Value3 = int(input("Element to search : "))

    Ret = FrequencyNum(Value2,Value3)

    print("Frequency of element from List is :",Ret)

if __name__ == "__main__":
    main()