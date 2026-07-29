############################################################################################
#   Q5) Search a Word in File
#   Problem Statement :
#   Write a program which accepts a file name and checks whether that word is present in
#   the file or not.
#   Input :
#   Demo.txt  Marvellous
#   Expected Output :
#   Display whether the word Marvellous is found in Demo.txt or not.
#############################################################################################


############################################################################################
#
#  Function Name :     SearchWord
#  Description :       Opens the specified file, reads it line by line using a manual
#                      counter, and checks if the target word exists in the file.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def SearchWord(FileName,Target):
    try:
        count = 0
        with open(FileName,"r") as file:
            for i in file:
                word = i.split()
                if Target in word:
                    count += word.count(Target)

        if count > 0:
            print(f"The word '{Target}' is found in {FileName} (Total occurrences: {count}).")
        else:
            print(f"The word '{Target}' is not found in {FileName}.")
    
    except Exception as eobj:
        print(f"An error occured : {eobj}")


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Accepts file name and search word from
#                      the user and invokes the SearchWord function.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def main():
    File = input("Enter File Name : ")
    Word = input("Enter Word to Search : ")
    
    SearchWord(File, Word)


############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()