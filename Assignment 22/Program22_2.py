############################################################################################
#   Write a program that calculates factorials of multiple numbers simultaneously using 
#   Pool.map()
#   Example Input :
#   [10, 15, 20, 25]
#   Display :
#   . Procees ID
#   . Input numbers
#   . Factorials
############################################################################################
from multiprocessing import Pool
import os

############################################################################################
#
#  Function Name :     Factorials
#  Description :       Return Factorial of given list.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def Factorials(n):
    #print("ProcessID :",os.getpid())
    Fact = 1
    listFact = []
    for i in range(1,n+1):
        Fact = Fact * i

    listFact.append(Fact)

    print("--------------------")
    print("Process ID:", os.getpid())
    print("Input Number:", n)
    print("Factorial:", Fact)
    print("--------------------")

    return listFact

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
        Ret = p.map(Factorials,Value)

    print("Factorials :",Ret)

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()