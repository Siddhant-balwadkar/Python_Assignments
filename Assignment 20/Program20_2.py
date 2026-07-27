############################################################################################
#
#   Design a python application that creates two threads named EvenFactor and OddFactor
#   . Both threads should accept one integer number as a parameter.
#   . The EvenFactor thread should:
#       . Identify all even factors of the given numbers.
#       . Calculate and display the sum of even factors.
#   . The OddFactor thread should:
#       . Identify all odd factors of the given number.
#       . Calculate and display the sum of odd factors. 
#   . After both threads complete execution, the main thread should display the message:
#   "Exit from main"
#
############################################################################################
import threading

############################################################################################
#
#  Function Name :     EvenFactor
#  Description :       Identify all even factors of the given numbers
#                      Calculate and display the sum of even factors
#  Author :            Siddhant Vikas Balwadkar
#  Date :              21/07/2026
#
############################################################################################
def EvenFactor(No):
    print("Even Factor Thread :")
    Factor = 0
    for i in range(1,No+1):
        if(No % i == 0) and (i % 2 == 0):
            print(i)
            Factor = Factor + i

    print("Sum of Even factors :",Factor)

############################################################################################
#
#  Function Name :     ChOddFactorkOdd
#  Description :       Identify all even factors of the given numbers.
#                      Calculate and display the sum of even factors
#  Author :            Siddhant Vikas Balwadkar
#  Date :              21/07/2026
#
############################################################################################
def OddFactor(No):
    print("Odd Thread :")
    Factor = 0
    for i in range(1,No+1):
        if(No % i == 0) and (i % 2 != 0):
            print(i)
            Factor = Factor + i

    print("Sum of odd factors :",Factor)


############################################################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              21/07/2026
#
############################################################################################
def main():
    Value = int(input("Enter the number : "))
    t1 = threading.Thread(target=EvenFactor, args=(Value,))
    t2 = threading.Thread(target=OddFactor, args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    

    print("Exit from main")

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()