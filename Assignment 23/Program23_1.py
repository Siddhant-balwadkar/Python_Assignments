############################################################################################
#   Write a program using multiprocessing.Pool to calculate the
#   sum of all even numbers from 1 to N for every number from the given
#   list. 
#   Input : 
#   Data = [1000000, 2000000, 3000000, 4000000]
#   Expected Task
#   For each number N, calculate: 
#   2 + 4 + 6 + ... + N
#   Expected Output Format :
#   Process ID : 1234
#   Input number : 1000000
#   Sum of Even Numbers : 250000500000
############################################################################################
from multiprocessing import Pool
import os

############################################################################################
#
#  Function Name :     Calculate
#  Description :       Calculates sum of even numbers till N
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def Calculate(n):
    Sum = 0
    for i in range(2,n+1,2):
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
        print(f"Sum of Even Numbers : {sum}")

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()