############################################################################################
#   Write a python program to implement a class named Demo with the following
#   specifications :
#   . The class should contain two instance variables : no1 and no2.
#   . The class should contain one class variable named Value.
#   . Define a constructor(__init__) that accepts two parameters and initializes the instance variables.
#   . Implement two instance methods :
#       . Fun() - displays the values of instance variables no1 and no2.
#       . Gun() - displays the values of instance variable no1 and no2.
#   Create two objects of the Demo class as follows :
#   obj1 = Demo(11, 21)
#   obj2 = Demo(51, 101)
#   Call the instance methods in the given sequence : 
#   obj1.Fun()
#   obj2.Fun()
#   obj1.Gun()
#   obj2.Gun()
############################################################################################


############################################################################################
#
#  Class Name :        Demo
#  Description :       Demonstrates OOP concepts in Python using class variables,
#                      instance variables, constructors, and instance methods.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################

class Demo:
    # Class variable (shared across all instances)
    Value = 0

    def __init__(self, A, B):
        # Instance variables (unique to each instance)
        self.no1 = A
        self.no2 = B

    # Instance Method to display instance variables
    def Fun(self):
        print("Inside instance method named Fun")
        print("Value of no1:", self.no1)
        print("Value of no2:", self.no2)

    # Instance Method to display instance variables
    def Gun(self):
        print("Inside instance method named Gun")
        print("Value of no1:", self.no1)
        print("Value of no2:", self.no2)


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Instantiates Demo objects
#                      and invokes their instance methods.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################

def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()


############################################################################################
#
#                      Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()