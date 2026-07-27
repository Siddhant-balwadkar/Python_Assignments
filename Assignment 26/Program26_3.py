############################################################################################
#   Write a python program to implement a class named Arithmetic with the following
#   characteristics :
#   . The class should contain two instance variables : Value1 and Value2.
#   . Define a constructor(__init__) that initializes all instance variables to 0.
#   . Implement the following instance methods :
#       . Accept() - accepts values for Value1 and Value2 from the user.
#       . Addition() - returns addition of Value1 and Value2.
#       . Subtraction() - returns subtraction of Value1 and Value2.
#       . Multiplication() - returns multiplication of Value1 and Value2.
#       . Division()- returns division of Value1 and Value2.
#
#   . Create multiple objects of the Arithmetic class and invoke all the instance methods for each object.   
############################################################################################


############################################################################################
#
#  Class Name :        Arithmetic
#  Description :       Performs basic arithmetic operations (Addition, Subtraction,
#                      Multiplication, Division) on two numbers.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
class Arithmetic:
    #Constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # Instance Method
    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))  

    #Instance Method
    def Addition(self):
        return self.Value1 + self.Value2

    #Instance Method
    def Subtraction(self):
        return self.Value1 - self.Value2

    #Instance Method
    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if(self.Value2 == 0):
            return "ERROR : Division by zero is not allowed"
        return self.Value1 / self.Value2


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Creates multiple Arithmetic objects,
#                      invokes all operations, and displays their returned results.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def main():
    print("--- Arithmetic Object 1 ---")
    obj1 = Arithmetic()
    obj1.Accept()
    print("Addition is       : ", obj1.Addition())
    print("Subtraction is    : ", obj1.Subtraction())
    print("Multiplication is : ", obj1.Multiplication())
    print("Division is       : ", obj1.Division())
    print()

    print("--- Arithmetic Object 2 ---")
    obj2 = Arithmetic()
    obj2.Accept()
    print("Addition is       : ", obj2.Addition())
    print("Subtraction is    : ", obj2.Subtraction())
    print("Multiplication is : ", obj2.Multiplication())
    print("Division is       : ", obj2.Division())


############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()