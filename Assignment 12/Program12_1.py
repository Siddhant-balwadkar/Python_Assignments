###############################################################
#   Write a program which accepts one character and checks whether it is vowel or consonant.
#   Input : a
#   Output : vowel
############################################################### 

##############################################################
#
#  Function Name :     CheckVowal
#  Description :       Check if the character is a vowal or not
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def CheckVowal(char):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]

    if(char in vowels):
        return True
    else:
        return False

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function 
#  Author :            Siddhant Vikas Balwadkar
#  Date :              30/06/2026
#
##############################################################
def main():

    print("Enter a character to check if it is a vowal or not : ")
    Character = input()

    Ret = CheckVowal(Character)

    if(Ret == True):
        print("Its a vowal")
    else:
        print("Its not a vowal")


if __name__ == "__main__":
    main()

##############################################
#   OUTPUT :
#
#   Enter a character to check if it is a vowal or not :
#   A
#   Its a vowal
#
# ##############################################