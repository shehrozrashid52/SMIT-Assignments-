class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.add_transaction(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        return self.balance

    def add_transaction(self, description):
        self.transactions.append(description)

    def print_statement(self):
        print(f"Statement for Account: {self.account_number}")
        for transaction in self.transactions:
            print(transaction)

class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_holder):
        account_number = len(self.accounts) + 1
        new_account = BankAccount(account_number, account_holder)
        self.accounts[account_number] = new_account
        print(f"Account created successfully. Account Number: {account_number}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender = self.get_account(sender_account_number)
        receiver = self.get_account(receiver_account_number)
        if sender and receiver and amount > 0 and sender.balance >= amount:
            sender.withdraw(amount)
            receiver.deposit(amount)
            print(f"Transferred {amount} from {sender_account_number} to {receiver_account_number}.")
        else:
            print("Transfer failed. Check account details and balance.")

    def admin_check_total_deposit(self):
        total_deposit = sum(account.balance for account in self.accounts.values())
        print(f"Total Deposits in Bank: {total_deposit}")
        return total_deposit

    def admin_check_total_accounts(self):
        total_accounts = len(self.accounts)
        print(f"Total Number of Accounts: {total_accounts}")
        return total_accounts

# Menu-Driven Interface
def main():
    bank = Bank()
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Open Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Print Statement")
        print("7. Admin: Check Total Deposits")
        print("8. Admin: Check Total Accounts")
        print("9. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter account holder name: ")
            bank.open_account(name)
        elif choice == 2:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == 3:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == 4:
            account_number = int(input("Enter account number: "))
            account = bank.get_account(account_number)
            if account:
                print(f"Balance: {account.check_balance()}")
            else:
                print("Account not found.")
        elif choice == 5:
            sender_account_number = int(input("Enter sender account number: "))
            receiver_account_number = int(input("Enter receiver account number: "))
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(sender_account_number, receiver_account_number, amount)
        elif choice == 6:
            account_number = int(input("Enter account number: "))
            account = bank.get_account(account_number)
            if account:
                account.print_statement()
            else:
                print("Account not found.")
        elif choice == 7:
            bank.admin_check_total_deposit()
        elif choice == 8:
            bank.admin_check_total_accounts()
        elif choice == 9:
            print("Exiting Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()