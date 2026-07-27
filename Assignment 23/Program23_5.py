############################################################################################
#   Write a program that calculates factorials of multiple numbers
#   simultaneously using multiprocessing.Pool.
#   Input : 
#   Data = [10, 15, 20, 25]
#   Expected Task :
#   For every N, calculate :
#   N!
#   Expected Output Format :
#   Process ID : 1240
#   Input number : 20
#   Factorial : 2432902008176640000
############################################################################################
from multiprocessing import Pool
import os

############################################################################################
#
#  Function Name :     Calculate
#  Description :       Calculates odd numbers count till N
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def Calculate(n):
    Fact = 1
    for i in range(1, n + 1):
        Fact = Fact * i

    return os.getpid(),n,Fact

############################################################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def main():
    Data = list(map(int,input("Enter the numbers : ").split()))

    with Pool() as p:
        Ret = p.map(Calculate,Data)

    for pid, n, fact in Ret:
        print(f"Process ID : {pid}")
        print(f"Input Number : {n}")
        print(f"Factorial : {fact}")

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()