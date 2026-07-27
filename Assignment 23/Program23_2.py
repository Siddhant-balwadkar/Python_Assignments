############################################################################################
#   Write a program using multiprocessing.Pool to calculate the
#   sum of all odd numbers from 1 to N.
#   Input : 
#   Data = [1000000, 2000000, 3000000, 4000000]
#   Expected Task
#   For each number N, calculate: 
#   1 + 3 + 5 + ... + N
#   Expected Output Format :
#   Process ID : 1235
#   Input number : 1000000
#   Sum of Odd Numbers : 250000000000
############################################################################################
from multiprocessing import Pool
import os

############################################################################################
#
#  Function Name :     Calculate
#  Description :       Calculates sum of odd numbers till N
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def Calculate(n):
    Sum = 0
    for i in range(1,n+1,2):
        Sum = Sum + i

    return os.getpid(),n,Sum

############################################################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def main():
    Value = list(map(int,input("Enter the numbers : ").split()))

    with Pool() as p:
        Ret = p.map(Calculate,Value)

    for pid, n, sum in Ret:
            print(f"Process ID : {pid}")
            print(f"Input Number : {n}")
            print(f"Sum of Odd Numbers : {sum}")

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()