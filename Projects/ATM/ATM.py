import pickle

# Create class
class bankaccount_ATM:
    # Initialize an instance
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
    
    def check_balance(self):
        print(f"Hello {self.owner}. Your balance is ${self._balance}.")    
    
    # Validate and deposit given amount
    def deposit_money(self, amount):
        if amount < 0:
            print("Can not deposit negative amount.")
        else:
            self._balance += amount
            print(f"New balance is ${self._balance}.")
    
    # Validate and withdraw given amount
    def withdraw_money(self, amount):
        if amount < 0:
            print("Can not withdraw negative amount.")

        else:    
            if amount > self._balance:
                print("Balance in not enough.")
            else:
                self._balance -= amount
                print(f"New balance is {self._balance}.")

# Save list of objects in the database file
def save_database(accounts):
    with open('database.pickle', 'wb') as file:
        pickle.dump(accounts, file)
    print("Account changes saved.")

def menu(account):
    choice = None
    while choice != '4':
        # Display menu
        print("\n1: Check Balance  2: Deposit  3: Withdraw  4: Exit")
        choice = input()
        if choice == '1':
            account.check_balance()

        elif choice == '2':
            amount = float(input("Amount to deposit: "))
            account.deposit_money(amount)
            save_database(accounts)

        elif choice == '3':
            account.withdraw_money(amount)
            save_database(accounts)


# Iterate over the array and find account object with the matching "owner" value
def log_in():
    name = input('Input your name: ')
    for account in accounts:
        if account.owner == name:
            menu(account)

# Load database
with open('database.pickle', 'rb') as file:
    accounts = pickle.load(file)
log_in()

# New user creation
account = bankaccount_ATM("Lia", 5000)
accounts.append(account)
save_database(accounts)