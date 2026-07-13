############################################################################################
#   Write a program which accept name from user and display length of its name.
#   Input :  Marvellous
#   Output : 10
############################################################################################


##############################################################
#
#  Function Name :          FinLength
#  Description :            Find length of given name
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   06/07/2026
#
##############################################################
def FinLength(char):
    cnt = 0
    for i in char:
        cnt = cnt + 1
    
    return cnt                      # return len(char)
    

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              06/07/2026
#
##############################################################
def main():
    print("Enter the name : ")
    Value = input()

    Ret = FinLength(Value)

    print("Length of name is :",Ret)

if __name__ == "__main__":
    main()