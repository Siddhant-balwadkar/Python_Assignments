############################################################################################
#   Design a python application that creates two threads.
#   . Thread 1 should compute the sum of elements from list.
#   . Thread 2 should compute the product of elements from the same list.
#   . Return the results to the main thread and display them.
############################################################################################
import threading

############################################################################################
#
#  Function Name :     Sum
#  Description :       Compute the sum of elements from list.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def Sum(Num):
    print("Sum of list is : ",end="  ")
    Add = 0
    for i in Num:
        Add = Add + i

    print(Add)

############################################################################################
#
#  Function Name :     Product
#  Description :       Compute the product of elements from the same list.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def Product(Num):
    print("Product of list is : ",end="  ")
    Mult = 1
    for i in Num:
        Mult = Mult * i
    
    print(Mult)


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
    t1 = threading.Thread(target=Sum,args=(Value,))
    t2 = threading.Thread(target=Product,args=(Value,))

    t1.start()
    t2.start()

    t1.join()
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