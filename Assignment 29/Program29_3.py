############################################################################################
#   Q4) Copy File Contents into a New File (Command Line)
#   Problem Statement :
#   Write a program which accepts a file name through command line arguments, creates a new
#   file named Demo.txt and copies all contents from the given file into Demo.txt.
#   Input (Command Line):
#   ABC.txt
#   Expected Output :
#   Create Demo.txt and copy contents of ABC.txt into Demo.txt.
#############################################################################################
import os
import sys

############################################################################################
#
#  Function Name :     CpyFile
#  Description :       Copies contents from the source file to the destination file.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              07/08/2026
#
############################################################################################
def CpyFile(SrcFile, DestFile):
    Dobj = open(DestFile, "w")
    if(os.path.exists(SrcFile)):
        with open(SrcFile,"r") as file:
            for line in file:
                Dobj.write(line)
        Dobj.close()
        print(f"Contents of {SrcFile} have been copied to {DestFile}.")
    else:
        print(f"File {SrcFile} does not exist.")

############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              07/08/2026
#
############################################################################################
def main():
    DestFile = "Demo.txt"
    if(len(sys.argv) == 2):
        srcFile = sys.argv[1]

        CpyFile(srcFile, DestFile)
    else:
        print("Error : Invalid number of arguments")
        print("Usage : ApplicationName.py SourceFile")
        return

############################################################################################
#
#           Starter of the main function
#
############################################################################################
if __name__ == "__main__":
    main()