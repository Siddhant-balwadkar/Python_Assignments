##############################################################################################
#   Write a program which accepts marks and displays grade.
#   Condition Example :
#   >= 75 : Distinction
#   >= 60 : First Class
#   >= 50 : Second Class
#   < 50 : Fail
#
#    Input : 85
#   Output : A
##############################################################################################

##############################################################
#
#  Function Name :     EvaluateGrade
#  Description :       Evaluates the grade based on marks
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def EvaluateGrade(Marks):
    if(Marks >= 75):
        return "Distinction"
    elif(Marks >= 60):
        return "First Class"
    elif(Marks >= 50):
        return "Second Class"
    else:
        return "Fail"

##############################################################
#
#  Function Name :     main
#  Description :       It is the main function
#  Author :            Siddhant Vikas Balwadkar
#  Date :              02/07/2026
#
##############################################################
def main():
    
    print("Enter a Marks : ")
    Value = int(input())

    Ret = EvaluateGrade(Value)

    print("Grade is :", Ret)

if __name__ == "__main__":
    main()
