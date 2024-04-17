class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +₹{amount}")
        return f"Deposited {amount}. Current Balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -₹{amount}")
            return f"Withdrew ₹{amount}. Current Balance: ₹{self.balance}"
        else:
            return "Insufficient funds"

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transfer to {recipient.name}: -₹{amount}")
            recipient.transactions.append(f"Transfer from {self.name}: +$₹{amount}")
            return f"Transferred ₹{amount} to {recipient.name}. Current Balance: ₹{self.balance}"
        else:
            return "Insufficient funds"

    def get_transactions(self):
        return self.transactions

    def quit(self):
        return "Thank you for using our ATM. Goodbye!"


class Customer:
    def __init__(self, name):
        self.name = name
        self.account = None

    def create_account(self):
        self.account = ATM()
        self.account.name = self.name

    def get_account_balance(self):
        if self.account:
            return f"Current Balance: ₹{self.account.balance}"
        else:
            return "No account found. Please create an account first."

    def get_transactions_history(self):
        if self.account:
            return self.account.get_transactions()
        else:
            return "No account found. Please create an account first."

# Example usage:
customer1 = Customer(input("Enter your name: "))
customer1.create_account()

print("Welcome, ", customer1.name)
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. View Balance")
    print("5. View Transaction History")
    print("6. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter deposit amount: ₹"))
        print(customer1.account.deposit(amount))
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: ₹"))
        print(customer1.account.withdraw(amount))
    elif choice == '3':
        recipient_name = input("Enter recipient's name: ")
        recipient = Customer(recipient_name)
        recipient.create_account()
        amount = float(input("Enter transfer amount: ₹"))
        print(customer1.account.transfer(amount, recipient.account))
    elif choice == '4':
        print(customer1.get_account_balance())
    elif choice == '5':
        print("Transaction History:")
        for transaction in customer1.get_transactions_history():
            print(transaction)
    elif choice == '6':
        print(customer1.account.quit())
        break
    else:
        print("Invalid choice. Please enter a valid option.")
