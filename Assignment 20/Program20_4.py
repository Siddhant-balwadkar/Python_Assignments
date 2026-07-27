############################################################################################
#
#   Design a python application that creates three threads named Small, Capital and Digits.
#   . All threads should accept a string as input.
#   . The Small thread should count and display the number of lowercase characters.
#   . The Capital thread should count and display the number of uppercase charcters.
#   . The Digits thread should count and display the number of numberic digits.
#   . Each thread must also display :
#       . ThreadID
#       . Thread Name
#
############################################################################################
import threading

############################################################################################
#
#  Function Name :     Small
#  Description :       Count and display the number of lowercase characters.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def Small(Str):
    Count = 0

    for ch in Str:
        if ch.islower():
            Count = Count + 1

    print("Thread ID   :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small letters :", Count)
    print()

############################################################################################
#
#  Function Name :     Capital
#  Description :       Count and display the number of uppercase charcters.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def Capital(Str):
    Count = 0

    for ch in Str:
        if ch.isupper():
            Count = Count + 1

    print("Thread ID   :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital letters :", Count)
    print()

############################################################################################
#
#  Function Name :     Digits
#  Description :       Count and display the number of numberic digits.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def Digits(Str):
    Count = 0

    for ch in Str:
        if ch.isdigit():
            Count = Count + 1

    print("Thread ID   :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", Count)
    print()


############################################################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              23/07/2026
#
############################################################################################
def main():
    Value = input("Enter a string : ")

    t1 = threading.Thread(target=Small, args=(Value,), name="Small")
    t2 = threading.Thread(target=Capital, args=(Value,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(Value,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()