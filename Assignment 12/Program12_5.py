###############################################################
#   Write a program which accepts one number and prints that many numbers in reverse order.
#   Input : 5
#   Output : 5 4 3 2 1
############################################################### 

##############################################################
#
#  Function Name :     DisplayReverse
#  Description :       Display number from given number to 1
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def DisplayReverse(No):
    Dis = []

    for i in range(No,0,-1):
        Dis.append(i)

    return Dis


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def main():
    
    print("Enter a first number : ")
    Value = int(input())

    Ret = DisplayReverse(Value)

    print(Ret)

if __name__ == "__main__":
    main()

##############################################
#   OUTPUT :
#
#   Enter a first number :
#   5
#   [5, 4, 3, 2, 1]

##############################################