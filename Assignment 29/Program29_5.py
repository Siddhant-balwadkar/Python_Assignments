############################################################################################
#   Q5) Frequency of a string in File
#   Problem Statement :
#   Write a program which accepts a file name and one string from the user and returns the
#   frequency (count of occurrences) of that string in the file.
#   Input:
#   Demo.txt Marvellous
#   Expected Output :
#   Count how many times "Marvellous" appears in Demo.txt
#############################################################################################
import os
import sys

############################################################################################
#
#  Function Name :     Frequency
#  Description :       Returns the frequency (count of occurrences) of a string in a file.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              07/08/2026
#
############################################################################################
def Frequency(FileName, SearchWord):
    if(os.path.exists(FileName)):
        try:
            count = 0
            with open(FileName, 'r') as file:
                for line in file:
                    count += line.count(SearchWord)
            
            print(f"Count how many times \"{SearchWord}\" appears in {FileName}: {count}")
            return count
        except Exception as e:
            print(f"Error : Unable to read file. {e}")
    else:
        print(f"Error : File '{FileName}' does not exist.")
        return -1


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Accepts a file name input from the user
#                      and invokes the Frequency function.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              07/08/2026
#
############################################################################################
def main():
    if(len(sys.argv) == 3):
        File = sys.argv[1]
        Word = sys.argv[2]

        Frequency(File, Word)
    else:
        print("Error : Invalid number of arguments")
        print("Usage : PythonScriptName.py FileName SearchWord")
        return

############################################################################################
#
#           Starter of the main function
#
############################################################################################
if __name__ == "__main__":
    main()