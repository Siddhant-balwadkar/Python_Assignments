###############################################################
#   Write a program which accepts one number and prints that many numbers starting from 1.
#   Input : 5
#   Output : 1 2 3 4 5
############################################################### 

##############################################################
#
#  Function Name :     DisplayForward
#  Description :       Display number from 1 to given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def DisplayForward(No):
    Dis = []

    for i in range(1,No + 1):
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

    Ret = DisplayForward(Value)

    print(Ret)

if __name__ == "__main__":
    main()

##############################################
#   OUTPUT :
#
#   Enter a first number :
#   5
#   [1, 2, 3, 4, 5]

##############################################