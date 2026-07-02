##############################################################################################
    #   Write a program which accepts one number and prints all odd number till that number.
    #   Input : 10
    #   Output : 1 3 5 7 9
##############################################################################################

##############################################################
#
#  Function Name :     EvenNum
#  Description :       Gives Even number till given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              01/07/2026
#
##############################################################
def EvenNum(No):
    Odd = []

    for i in range(1, No + 1):
        if(i%2 != 0):
            Odd.append(i)

    return Odd


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              01/07/2026
#
##############################################################
def main():
    
    print("Enter a number : ")
    Value = int(input())

    Ret = EvenNum(Value)

    print(Ret)

if __name__ == "__main__":
    main()
