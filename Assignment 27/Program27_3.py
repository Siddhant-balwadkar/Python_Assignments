############################################################################################
#   Write a python program to implement a class named Numbers with the following
#   specifications :
#   . The class should contain one instance variables :
#       . Value
#   . Define a constructor(__init__) that accepts a number from the user and initializes Value.
#   . Implement the following instance methods :
#       . ChkPrime() - return True if the number is prime, otherwise returns False.
#       . ChkPerfect() - returns True if the number is perfect, otherwise returns False.
#       . Factors() - displays all factors of the number
#       . SumFactors() - returns the sum of all factors
#   . Create multiple objects and demonstrate all methods.
############################################################################################

############################################################################################
#
#  Class Name :        Numbers
#  Description :       Provides mathematical checks and factor calculations for a given
#                      integer (Prime check, Perfect check, Factors, Sum of Factors).
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
class Numbers:
    #Class variable
    ROI = 10.5

    #Constructor
    def __init__(self,A):
        self.Value = A

    # Instance Method
    def ChkPrime(self):
        if(self.Value <= 1):
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if(self.Value%i==0):
                return False
        return True

    def Factors(self):
        print(f"Factors of {self.Value} are : ", end="")
        for i in range(1, (self.Value // 2) + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, (self.Value // 2) + 1):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        if self.Value <= 0:
            return False
        return self.SumFactors() == self.Value

############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Accepts input, creates multiple Numbers 
#                      objects, and tests all instance methods.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################

def main():
    print("--- Number Object 1 ---")
    val1 = int(input("Enter first number: "))
    obj1 = Numbers(val1)

    if obj1.ChkPrime():
        print(f"{obj1.Value} is a Prime number")
    else:
        print(f"{obj1.Value} is not a Prime number")

    obj1.Factors()
    print("Sum of factors is :", obj1.SumFactors())

    if obj1.ChkPerfect():
        print(f"{obj1.Value} is a Perfect number")
    else:
        print(f"{obj1.Value} is not a Perfect number")

    print("-" * 50)

    print("\n--- Number Object 2 ---")
    val2 = int(input("Enter second number: "))
    obj2 = Numbers(val2)

    if obj2.ChkPrime():
        print(f"{obj2.Value} is a Prime number")
    else:
        print(f"{obj2.Value} is not a Prime number")

    obj2.Factors()
    print("Sum of factors is :", obj2.SumFactors())

    if obj2.ChkPerfect():
        print(f"{obj2.Value} is a Perfect number")
    else:
        print(f"{obj2.Value} is not a Perfect number")

    print("-" * 50)

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()