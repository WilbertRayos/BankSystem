from . import db

class API:
    def __init__(self):
        pass

    def withdraw(self, username, withdraw_amt):
        if withdraw_amt > db.accounts[username]["balance"]:
            print("You have insufficient balance to withdraw")
        else:
            db.accounts[username]["balance"] -= withdraw_amt
            print(f"You have successfully withdrawn Php {withdraw_amt} from your bank account.")

    def deposit(self, username, deposit_amt):
        if deposit_amt <= 0:
            print("You can not deposit negative amount of money.")
        else:
            db.accounts[username]["balance"] += deposit_amt
            print(f"You have successfully deposited Php {deposit_amt} to your bank account.")

    def transfer_fund(self, username, recipient, transfer_amt):
        if recipient in db.accounts:
            if transfer_amt > db.accounts[username]["balance"]:
                print("Insufficient balance for transfer.")
            else:
                db.accounts[username]["balance"] -= transfer_amt
                db.accounts[recipient]["balance"] += transfer_amt
                print(f"Succesfully transferred Php {transfer_amt} to {recipient}.")
        else:
            print("Recipient account does not exist.")

    def register(self, name, password, email, username, intl_bal):
        if username in db.accounts:
            print("Username already exists.")
        else:
            new_account = {
                username:{
                    "name": name,
                    "balance": intl_bal,
                    "password": password,
                    "email": email,
                    "username": username
                }
            }
            db.accounts.update(new_account)

    def check_bank_info(self, username):
        print(f"Name: {db.accounts[username]['name']}")
        print(f"Username: {db.accounts[username]['username']}")
        print(f"Password: {db.accounts[username]['password']}")
        print(f"Balance: {db.accounts[username]['balance']}")
        print(f"Email: {db.accounts[username]['email']}")
    
    def main_menu_process(self, choice):
        if choice == 1:
            


# register("Altis Dulay", "4321", "altis@gmail.com", "AltisDulay20", 50000)
# check_bank_info("AltisDulay20")
# print()
# withdraw("AltisDulay20", 20000)
# print()
# check_bank_info("AltisDulay20")
# print()
# transfer_fund("AltisDulay20", "NinoDulay18", 20000)
# print()
# check_bank_info("AltisDulay20")
# print()
# check_bank_info("NinoDulay18")

'''
Welcome to Bank System
1. Login
2. Register
# >>> 2

Username: 
Password:
Initial Deposit:
Email:
Username:

Are you sure? (Y/N): 


Succesfully Registered, Please Log In.
----------------------------------------------

Welcome to Bank System
1. Login
2. Register

# >>> 1

Username: NinoDulay18
Password: 1234

Succesfully Logged In! What do you want to do:
1. Withdraw
2. Transfer
3. Deposit
4. Log out
>>>
'''