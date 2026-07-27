############################################################################################
#
#   Design a python application where multiple threads update a shared variable.
#   . Use a Lock to avoid race condition.
#   . Each thread should increment the shared counter multiple times.
#   . Display the final value of the counter after all threads complete execution.
#
############################################################################################
import threading

counter = 0

Lock = threading.Lock()

############################################################################################
#
#  Function Name :     increment
#  Description :       Increase the count of a varaiable.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def increment():
    global counter
    for i in range(1000):
        with Lock:
            counter = counter + 1

############################################################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def main():
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)
    t3 = threading.Thread(target=increment)

    t1.start()
    t3.start()
    t2.start()

    t1.join()
    t2.join()
    t3.join()

    print(counter)
    print("Exit from main")

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()