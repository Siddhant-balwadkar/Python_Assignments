############################################################################################
#   Write a python program to implement a class named BankAccount with the following
#   requirements :
#   . The class should contain two instance variables :
#       . Name (Account holder Name)
#       . Amount (Account Balance)
#   . The class should contain one class variable:
#       .ROI(Rate of Interest),initialize to 10.5
#   . Define a constructor(__init__) that accepts Name and initial Amount.
#   . Implement the following instance methods :
#       . Display() - display account holder name and current balance.
#       . Deposit() - accepts an amount from the user and adds it to balance
#       . Withdraw() - accepts an amount from the user and subtracts it from the balance
#         (Ensure withdrawal is allowed only if sufficient balance exists)
#       . CalculateInterest() - calculates and returns interest using formula : 
#         Interest = (Amount * ROI) / 100
#   . Create multiple objects and demonstrate all methods.
############################################################################################

############################################################################################
#
#  Class Name :        BankAccount
#  Description :       Manages bank account operations including deposits, withdrawals,
#                      balance checking, and interest calculation.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
class BankAccount:
    #Class variable
    ROI = 10.5

    #Constructor
    def __init__(self,A,B):
        self.Name = A
        self.Amount = float(B)

    # Instance Method
    def Display(self):
        print(f"Account Holder Name : {self.Name}")
        print(f"Current Balance : {self.Amount}")
        print()

    def Deposit(self):
        Add = float(input("Amount to deposit : "))
        self.Amount += Add
        print("Amount successfully Credited!")
        print(f"Updated Balance     : {self.Amount}")
        print()

    def Withdraw(self):
        Sub = float(input("Amount to withdraw from account : "))
        if(self.Amount < Sub):
            print("Transaction Failed : Insufficient Balance!")
        else:
            self.Amount -= Sub
            print(f"{Sub} successfully debited")
            print(f"Updated Balance     : {self.Amount}")
            print()

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


############################################################################################
#
#  Function Name :     main
#  Description :       Entry point of the program. Instantiates BankAccount objects
#                      and demonstrates all banking operations.
#  Author :            Siddhant Vikas Balwadkar
#  Date :              28/07/2026
#
############################################################################################
def main():
    print("--- Account 1 ---")
    obj1 = BankAccount("Siddhant Balwadkar", 25000)
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    interest1 = obj1.CalculateInterest()
    print("Calculated Interest :", interest1)
    print("-"*60)

    print("\n--- Account 2 ---")
    obj2 = BankAccount("Shivam Thakur", 35000)
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    interest2 = obj2.CalculateInterest()
    print("Calculated Interest :", interest2)
    print("-"*60)


############################################################################################
#
#           Starter of the main function
#
############################################################################################

if __name__ == "__main__":
    main()