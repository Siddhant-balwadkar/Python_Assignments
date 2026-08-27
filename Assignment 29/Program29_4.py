############################################################################################
#   Q4) Compare Two Files (Command Line)
#   Problem Statement :
#   Write a program which accepts a two file name through command line arguments and compares
#   the contents of both Files.
#       . If both files contains the same contents, display Success
#       . Otherwise display failure 
#   Input (Command Line):
#   Demo.txt Hello.txt
#   Expected Output :
#   Sucess OR Failure
#############################################################################################
import os
import sys
import hashlib

############################################################################################
#
#  Function Name :     CheckSum
#  Description :       Calculates the MD5 checksum of a file.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              07/08/2026
#
############################################################################################
def CheckSum(FileName):
    fobj = open(FileName,"r+b")
    hobj = hashlib.md5()
    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

############################################################################################
#
#  Function Name :     CompareFiles
#  Description :       Compares the contents of two files.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              07/08/2026
#
############################################################################################
def CompFile(SrcFile, DestFile):
    if(os.path.exists(SrcFile) and os.path.exists(DestFile)):
        Comp1 = CheckSum(SrcFile)
        Comp2 = CheckSum(DestFile)

        if(Comp1 == Comp2):
            print(f"Both files {SrcFile} and {DestFile} have the same contents.")
            print("Success")
        else:
            print(f"Files {SrcFile} and {DestFile} have different contents.")
            print("Failure")
    else:
        print(f"One or both files {SrcFile} and {DestFile} do not exist.")


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Accepts a file name input from the user
#                      and invokes the Display function.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              07/08/2026
#
############################################################################################
def main():
    DestFile = "Demo.txt"
    if(len(sys.argv) == 3):
        srcFile = sys.argv[1]
        DestFile = sys.argv[2]

        CompFile(srcFile, DestFile)
    else:
        print("Error : Invalid number of arguments")
        print("Usage : ApplicationName.py SourceFile DestinationFile")
        return

############################################################################################
#
#           Starter of the main function
#
############################################################################################
if __name__ == "__main__":
    main()