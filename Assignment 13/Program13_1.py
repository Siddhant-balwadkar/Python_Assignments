##############################################################################################
#   Write a program which accepts length and width of a rectangle and prints area.
#   Input : 10 5
#   Output : 50
##############################################################################################

##############################################################
#
#  Function Name :     RectangleArea
#  Description :       Calculates the area of a rectangle
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def RectangleArea(Length, Width):
    Area = Length * Width
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
    
    print("Enter length of rectangle : ")
    Value1 = int(input())

    print("Enter width of rectangle : ")
    Value2 = int(input())

    Ret = RectangleArea(Value1, Value2)

    print("Area of rectangle is :", Ret)

if __name__ == "__main__":
    main()
