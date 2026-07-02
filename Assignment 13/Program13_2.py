##############################################################################################
#   Write a program which accepts radius of a circle and prints area.
#   Input : 5
#   Output : 78.5
##############################################################################################

##############################################################
#
#  Function Name :     CircleArea
#  Description :       Calculates the area of a circle
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def CircleArea(Radius):
    Pi = 3.14
    Area = Radius * Radius * Pi
    return Area


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def main():
    
    print("Enter radius of circle : ")
    Value = int(input())

    Ret = CircleArea(Value)

    print("Area of circle is :", Ret)

if __name__ == "__main__":
    main()
