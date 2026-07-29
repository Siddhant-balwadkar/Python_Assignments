############################################################################################
#   Q4) Copy File Contents into Another File
#   Problem Statement :
#   Write a program which accepts two file name from the user.
#       . First file is an existing file
#       . Seconf file is a new file
#   Copy all contents from the first file into second file.
#   Input :
#   ABC.txt  Demo.txt
#   Expected Output :
#   Contents of ABC.txt copied into Demo.txt.
############################################################################################



############################################################################################
#
#  Function Name :     CpyFile
#  Description :       Opens the specified file, reads its contents, and prints the 
#                      total word count.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def CpyFile(SourceFile, DestFile):
    try:
        with open(SourceFile,"r") as Srcfile, \
            open(DestFile,"w") as DstFile:
            for line in Srcfile:
                for line in Srcfile:
                    DstFile.write(line)
                    
        print(f"Contents of {SourceFile} successfully copied into {DestFile}.")

    except Exception as eobj:
        print(f"An error occured : {eobj}")


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Accepts source and destination file names
#                      from the user and invokes the CopyFile function.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def main():
    Source = input("Enter Source File Name : ")
    Destination = input("Enter Destination File Name : ")

    CpyFile(Source, Destination)


############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()