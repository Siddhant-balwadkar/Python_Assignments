############################################################################################
#
#   Design a python application that creates two threads named Thread1, Thread2.
#   . Thread1 should display numbers from 1 to 50.
#   . Thread2 should display numbers from 50 to 1 in reverse order.
#   . Ensure that :
#       . Thread2 starts execution only after Thread1 has completed.
#   . Use appropriate thread synchronization
#
############################################################################################
import threading

############################################################################################
#
#  Function Name :     Thread1
#  Description :       Display numbers from 1 to 50.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def Thread1():
    for i in range(1,51):
        print(i,end="  ")


############################################################################################
#
#  Function Name :     Thread2
#  Description :       Display numbers from 50 to 1 in reverse order.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def Thread2():
    print()
    for i in range(50,0,-1):
        print(i,end="  ")


############################################################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def main():
    t1 = threading.Thread(target=Thread1, name="Thread1")
    t2 = threading.Thread(target=Thread2, name="Thread2")

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