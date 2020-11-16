class SavingAccount:
    def __init__(self, pin=200499, interestRate = 0.25):
        self.pin = pin
        self.balance = 0
        self.interestRate = interestRate
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def change_pin(self, oldpin, newpin):
        if self.pin == oldpin:
            self.pin = newpin
            print("The old pin is ", oldpin)
            print("New pin is ", self.pin)

        else:
            print("Pin is wrong")

    def totalinterestRate(self):
        print("\n Total interest rate: ", self.balance * self.interestRate)

    def display(self):
        print("\n Net Available Balance=", self.balance)

# Driver code


# creating an object of class
s = SavingAccount()

# Calling functions with that class object

pin = int(input("Please enter pin: "))
newpin = int(input("Please enter new pin: "))
s.deposit()
s.withdraw()
s.totalinterestRate()
s.display()
