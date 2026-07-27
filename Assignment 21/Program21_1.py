############################################################################################
#
#   Design a python application that creates two threads named Prime, NonPrime.
#   . Both threads should accept a list of integers.
#   . The Prime thread should display all prime numbers from the list.
#   . The NonPrime thread should sisplay all non-prime numbers from the list.
#
############################################################################################
import threading

############################################################################################
#
#  Function Name :     isPrime
#  Description :       Check if the number is a prime number or not
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################

def isPrime(No):
    if No < 2:
        return False
    
    for i in range(2,No):
        if No % i == 0:
            return False

    return True


############################################################################################
#
#  Function Name :     Prime
#  Description :       Display all prime numbers from the list.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################

def Prime(Num):
    print("Prime Numbers : ")
    for i in Num:
        if isPrime(i):
            print(i)

############################################################################################
#
#  Function Name :     NonPrime
#  Description :       Display all non prime numbers from the list.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def NonPrime(Num):
    print("Non-Prime Numbers are : ")
    for i in Num:
        if not isPrime(i):
            print(i)


############################################################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def main():
    Value = list(map(int,input("Enter the elements : ").split()))
    t1 = threading.Thread(target=Prime,args=(Value,), name="Prime")
    t2 = threading.Thread(target=NonPrime,args=(Value,), name="NonPrime")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print()
    print("Exit from main")

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()