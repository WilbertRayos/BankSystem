class UserInterface:
    def __init__(self):
        pass

    def main_menu(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("Which select transaction: ")
        print("1. Login")
        print("2. Exit")
        print("*"*39)
        choice = int(input("Please enter your option: "))
        

    def login(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("LOGIN")
        username = input("Username: ")
        password = input("Password: ")
        print("*"*39)

    def register(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("REGISTER NEW ACCOUNT")
        name = input("Name: ")
        password = input("Password: ")
        email = input("Email: ")
        username = input("Username: ")
        initial_balance = float(input("Initial Balance: "))
        print("*"*39)
    
    def deposit(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("DEPOSIT")
        username = input("Account Username: ")
        amount = float(input("Amount: "))
        print("*"*39)

    def transfer_fund(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("TRANSFER FUND")
        username = input("Username: ")
        recipient = input("Recipient: ")
        amount = float(input("Amount: "))
        print("*"*39)
    
    def check_info(self):
        print(f"{'*'*10} MOOD BOOSTER BANK {'*'*10}")
        print("CHECK BANK INFORMATION")
        username = input("Username: ")
        password = input("Password: ")
        print("*"*39)

    def logout(self):
        pass

    def exit(self):
        pass


        