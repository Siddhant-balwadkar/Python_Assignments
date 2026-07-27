############################################################################################
#
#   Design a python application that creates two threads.
#   . Thread 1 should calculate and display the maximum element from the same list.
#   . Thread 2 should calculate and display the minimum element from the same list.
#   . The list should be accepted from the user.
#
############################################################################################
import threading

############################################################################################
#
#  Function Name :     MaxNum
#  Description :       Display the maximum element from the same list.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def MaxNum(Num):
    print("Maximum Numbers is : ",end="  ")
    Max = Num[0]
    for i in Num:
        if Max < i:
            Max = i
    print(Max)


############################################################################################
#
#  Function Name :     MinNum
#  Description :       Display the minimum element from the same list.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              27/07/2026
#
############################################################################################
def MinNum(Num):
    print("Minimun Numbers is : ",end="  ")
    Min = Num[0]
    for i in Num:
        if Min > i:
            Min = i
    print(Min)
    

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
    t1 = threading.Thread(target=MaxNum,args=(Value,))
    t2 = threading.Thread(target=MinNum,args=(Value,))

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