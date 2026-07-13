############################################################################################
#   Write a program which accept one number and display below pattern
#   Input :  5
#   Output : 1
#            1  2
#            1  2   3
#            1  2   3   4
#            1  2   3   4   5
#
############################################################################################


##############################################################
#
#  Function Name :          DisplayPattern
#  Description :            Display star * pattern
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   13/07/2026
#
##############################################################
def DisplayPattern(No):
    Row = No
    Column = 1

    for i in range(1,Row+1):
        for n in range(1,Column+1):
            print(n,end="\t")
        Column = Column + 1
        print()


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              13/07/2026
#
##############################################################
def main():
    Value = int(input("Enter the number : "))

    DisplayPattern(Value)

if __name__ == "__main__":
    main()