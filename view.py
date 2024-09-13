class View:
    def __init__(self):
        pass

    def main_menu(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("Which select transaction: ")
        print("1. Login")
        print("2. Exit")
        print("*"*39)
        choice = input("Please enter your option: ")

        return int(choice)
        

    def login(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("LOGIN")
        print("*"*39)
        username = input("Username: ")
        password = input("Password: ")
        
        return [username, password]
    
    def home_page(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("Select transaction: ")
        print("1. Register")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Fund")
        print("5. Check Information")
        print("6. Logout")
        print("*"*39)
        choice = input("Please enter your transaction: ")

        return int(choice)

    def register(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("REGISTER NEW ACCOUNT")
        print("*"*39)
        name = input("Name: ")
        password = input("Password: ")
        email = input("Email: ")
        username = input("Username: ")
        initial_balance = float(input("Initial Balance: "))

        return [name, password, email, username, initial_balance]
    
    def deposit(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("DEPOSIT")
        print("*"*39)
        username = input("Account Username: ")
        amount = float(input("Amount: "))

        return username, amount
    
    def withdraw(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("WITHDRAW")
        print("*"*39)
        username = input("Account Username: ")
        amount = float(input("Amount: "))

        return username, amount

    def transfer_fund(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("TRANSFER FUND")
        username = input("Username: ")
        recipient = input("Recipient: ")
        amount = float(input("Amount: "))

        return username, recipient, amount
    
    def check_info(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("CHECK BANK INFORMATION")
        username = input("Username: ")

        return username

    def logout(self):
        pass

