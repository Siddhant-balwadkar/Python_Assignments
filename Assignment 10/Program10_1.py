##############################################################################################
#   Write a program which accepts one number and prints multiplication table of that number.
#   Input : 4
#   Output : 4 8 12 16 20 24 28 32 36 40
##############################################################################################

##############################################################
#
#  Function Name :     MultiplicationTable
#  Description :       Gives Multiplication of given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              01/01/2026
#
##############################################################
def MultiplicationTable(No):
    Dis = []

    for i in range(1,11):
        Multi = No * i
        Dis.append(Multi)

    return Dis


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

    Ret = MultiplicationTable(Value)

    print(Ret)

if __name__ == "__main__":
    main()