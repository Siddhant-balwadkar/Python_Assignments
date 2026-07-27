############################################################################################
#   Write a program that counts how many even numbers exist
#   between 1 and N using Pool.map().
#   Input : 
#   Data = [1000000, 2000000, 3000000, 4000000]
#   Expected Output Format :
#   Process ID : 1236
#   Input number : 1000000
#   Even Numbers count : 500000
############################################################################################
from multiprocessing import Pool
import os

############################################################################################
#
#  Function Name :     Calculate
#  Description :       Calculates even numbers count till N
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def Calculate(n):
    count = 0
    for i in range(1,n+1):
        if(i % 2 == 0):
            count = count + 1

    return os.getpid(),n,count

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

    for pid, n, count in Ret:
        print(f"Process ID : {pid}")
        print(f"Input Number : {n}")
        print(f"Count of Even Numbers : {count}")


############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()