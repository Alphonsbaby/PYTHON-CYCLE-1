# Create a Bank account with members account number, name, type of account and balance.
#Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
class bank:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal ")
    def info(self):
        self.accnum = int(input("enter the account number"))
        self.name = str(input("enter the name"))
        self.type = str(input("enter the account type"))
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance  ")

    def display(self):
        print((" name  :::::",self.accnum ))
        print(("account number ::::::", self.name,))
        print((" account type :::::", self.type))
        print(" Net Available Balance=", self.balance)
s =bank()
s.info()
s.deposit()
s.withdraw()
s.display()