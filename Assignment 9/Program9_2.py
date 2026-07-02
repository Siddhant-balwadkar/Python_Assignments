##############################################################################################
#   Write a program which contains one function named ChkGreater() that accepts two numbers
#   and prints greater number.
#   Input : 10 20    
#   Output : 20 is greater
##############################################################################################

##############################################################
#
#  Function Name :     ChkGreater
#  Description :       It is used to check and print the greater number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
###############################################################
def ChkGreater(num1, num2):
    if(num1 > num2):
        print(num1, "is greater")
    elif(num1 < num2):
        print(num2, "is greater")
    else:
        print("Both numbers are equal")    


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def main():
    
    print("Enter first number : ")
    Values1 = int(input())
    print("Enter second number : ")
    Values2 = int(input())

    ChkGreater(Values1, Values2)

if __name__ == "__main__":
    main()