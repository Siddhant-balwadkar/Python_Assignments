############################################################################################
#   For every number in the given list, count how many prime numbers exist between 1 and N
#   using multiprocessing Pool.
#   Example :
#   10000
#   20000
#   30000
#   40000
#   Display total prime count for each number.
############################################################################################
from multiprocessing import Pool

############################################################################################
#
#  Function Name :     ChkPrime
#  Description :       Check if a single number is prime
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def ChkPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

############################################################################################
#
#  Function Name :     CountPrime
#  Description :       Count Prime numbers between 1 and n
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def CountPrime(n):
    if n < 2:
        return 0

    Count = 1

    for num in range(3, n + 1, 2):
        if ChkPrime(num):
            Count = Count + 1 

    return Count

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
        Ret = p.map(CountPrime,Value)

    print("Total Count of prime numbers is :",Ret)

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()