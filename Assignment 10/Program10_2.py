##############################################################################################
#   Write a program which accepts one number and prints sum of first N natural number.
#   Input : 5
#   Output : 15
##############################################################################################

##############################################################
#
#  Function Name :     SumNaturalNum
#  Description :       sum of first N natural numbers
#  Author :            Siddhant Vikas Balwadkar
#  Date :              01/01/2026
#
##############################################################
def SumNaturalNum(No):
    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + i

    return Sum        


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              01/01/2026
#
##############################################################
def main():
    
    print("Enter a number : ")
    Value = int(input())

    Ret = SumNaturalNum(Value)

    print(Ret)

if __name__ == "__main__":
    main()