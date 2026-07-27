############################################################################################
#   Write a program that accepts a list of integers and uses Pool.map()
#   to calculate the sum of squares from 1 to N for every element in the
#   list.
#   Example Input :
#   [1000000, 2000000, 3000000, 4000000]
#   Expected output :
#   [333333833333500000,
#   2666668666667000000,
#   ....]
############################################################################################
from multiprocessing import Pool

############################################################################################
#
#  Function Name :     Sum
#  Description :       Compute the sum of elements from list.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def SumSquare(n):
    return(n * (n + 1)*(2 * n + 1) // 6)


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
        Ret = p.map(SumSquare,Value)

    print("Output :",Ret)

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()