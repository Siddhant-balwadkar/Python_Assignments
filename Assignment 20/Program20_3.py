############################################################################################
#
#   Design a python application that creates two threads named EvenList and OddList.
#   . Both threads should accept a list of integers as input.
#   . The EvenList thread should:
#       . Extract all even elements from the list.
#       . Calculate and display their sum.
#   . The OddList thread should:
#       . Extract all odd elements from the list.
#       . Calculate and display their sum.
#   . Threads should run concurrently.
#
############################################################################################
import threading

############################################################################################
#
#  Function Name :     EvenList
#  Description :       Extract all even elements from the list
#                      Calculate and display their sum
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def EvenList(No):
    print("Even List Thread :")
    Factor = 0
    for i in No:
        if(i % 2 == 0):
            print(i)
            Factor = Factor + i

    print("Sum of Even element :",Factor)

############################################################################################
#
#  Function Name :     OddList
#  Description :       Extract all odd elements from the list.
#                      Calculate and display their sum.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def OddList(No):
    print("Odd List Thread :")
    Factor = 0
    for i in No:
        if(i % 2 != 0):
            print(i)
            Factor = Factor + i

    print("Sum of odd elements :",Factor)


############################################################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def main():
    Value = list(map(int,input("Enter the number : ").split()))

    t1 = threading.Thread(target=EvenList, args=(Value,))
    t2 = threading.Thread(target=OddList, args=(Value,))

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