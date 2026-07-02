##############################################################################################
#   Write a program which accepts one number and prints cube of that number
#   Input : 5
#   Output : 125
##############################################################################################

##############################################################
#
#  Function Name :     CalculateCube
#  Description :       Calculates the cube of the given number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
###############################################################
def CalculateCube(No):
    Cube = No * No * No
    return Cube   


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


    Ret = CalculateCube(Values1)
    print("Cube is :",Ret)

if __name__ == "__main__":
    main()