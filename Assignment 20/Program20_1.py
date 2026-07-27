############################################################################################
#
#   Design a python application that creates two separate threads named Even and Odd
#   . The even thread should display the first 10 even numbers.
#   . The Odd thread should display the first 10 odd numbers.
#   . Both thread should execute independently using thread module.
#   . Ensure proper thread creation and execution.
#
############################################################################################
import threading

##############################################################
#
#  Function Name :     ChkEven
#  Description :       Displays first 10 even number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def ChkEven():
    print("Even Thread :")

    for i in range(2, 21, 2):
        print(i, end=" ")

    print()


##############################################################
#
#  Function Name :     ChkOdd
#  Description :       Displays first 10 odd number
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def ChkOdd():
    print("Odd Thread :")
  
    for i in range(1, 20, 2):
        print(i, end=" ")

    print()


##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              18/07/2026
#
##############################################################
def main():
    t1 = threading.Thread(target=ChkEven, name=("Even"))
    t2 = threading.Thread(target=ChkOdd, name=("Odd"))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Both threads executed successfully")

if __name__ == "__main__":
    main()