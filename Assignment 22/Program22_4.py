############################################################################################
#   Write a program that calculates 
#   1^5+2^5+3^5+.....+N^5
#   for multiple values of N simultaneously using Pool.
#   Input :
#   [1000000,
#   2000000,
#   3000000,
#   4000000]
#   Measure total execution time.
############################################################################################
from multiprocessing import Pool
import time

############################################################################################
#
#  Function Name :     Calculate
#  Description :       Calculates 1^5+2^5+3^5+.....+N^5 for multiple values of N
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def Calculate(n):
    Multiple = 0
    for i in range(1,n+1):
        Multiple = Multiple + i ** 5

    return Multiple

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

    start_time = time.perf_counter()
    with Pool() as p:
        Ret = p.map(Calculate,Value)

    print("Multiple values is :",Ret)

    end_time = time.perf_counter()
    print(f"Total time required : {end_time - start_time}")

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()