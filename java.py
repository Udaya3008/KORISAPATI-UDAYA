# To create the BankAccount class
class bank:
    def __init__(self):
        self.bal = 0 # Initialize balance to 0
        print("Welcome to the SBI")

    def deposit(self):
        amt = float(input("Enter amount to be Deposited:"))
        self.bal += amt
        print("\n deposited amount :",amt)
    def withdraw(self):
        amt = float(input("Enter amount to be Withdrawn:"))
        if self.bal>= amt:
            self.bal -= amt
            print("\n You Withdrew:",amt)
        else:
            print("\nInsufficient balance")

        def display(self):
            print("\nNet Available Balance =",self.bal)

#driver code
s = bank()  #Create an object of BankAccount

s.deposit() #Deposit money
s.withdraw() #Withdraw money
s.display()  #Display balance
