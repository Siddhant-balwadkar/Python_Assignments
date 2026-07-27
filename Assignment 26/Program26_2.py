############################################################################################
#   Write a python program to implement a class named Circle with the following
#   requirements :
#   . The class should contain three instance variables : Radius, Area and Circumference.
#   . The class should contain one class variable named PI,initialized to 3.14.
#   . Define a constructor(__init__) that initializes all instance variables to 0.0.
#   . Implement the following instance methods :
#       . Accept() - accepts the radius of the circle from the user.
#       . CalculateArea() - calculates the area of the circle and stores it in the Area variable.
#       . CalculateCircumference() - calculates the circumference of the circle and stores it in
#         the Circumference variable.
#       . Display()- display the values of Radius, Area and Circumference.
#   . Create multiple objects of the Circle class and invoke all the instance methods for each object.   
############################################################################################


############################################################################################
#
#  Class Name :        Circle
#  Description :       Calculates and displays the Area and Circumference of a Circle.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
class Circle:
    #Class variable
    PI = 3.14

    #Constructor
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # Instance Method
    def Accept(self):
        self.Radius = float(input("Enter radius of circle : "))  

    #Instance Method
    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius * self.Radius)

    #Instance Method
    def Display(self):
        print("Radius of circle is : ",self.Radius)
        print("Area of circle is : ",self.Area)
        print("Circumference of circle is : ",self.Circumference)

    #Instance Method
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Creates multiple Circle objects,
#                      invokes methods, and demonstrates calculation functionality.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def main():
    print("--- Circle Object 1 ---")
    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    print("--- Circle Object 2 ---")
    obj2 = Circle()
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()


############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()