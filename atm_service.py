class ATMService:
    def __init__(self):
        self.balance = 5000
        self.statement = []

    def display_balance(self):
        print(f"\nYour current balance is Rs. {self.balance}")

    def deposit_money(self):
        amount = int(input("Enter amount to deposit: "))

        if amount > 0:
            self.balance += amount
            self.statement.append(f"Deposited Rs. {amount}")
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw_money(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.statement.append(f"Withdrawn Rs. {amount}")
            print("Amount withdrawn successfully.")

    def show_statement(self):
        print("\n----- Transaction Statement -----")

        if len(self.statement) == 0:
            print("No transactions yet.")
        else:
            for transaction in self.statement:
                print(transaction)