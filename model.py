class Model:
    
    # Data Model
    accounts = {
        "NinoDulay18":{
            "name":"Nino Dulay",
            "balance": 10000,
            "password": "1234",
            "email": "nino@gmail.com",
            "username": "NinoDulay18"
        },
        "JohnDoe32":{
            "name":"John Doe",
            "balance": 20000,
            "password": "4321",
            "email": "john@gmail.com",
            "username": "JohnDoe32"
        }
    }

    credentials = {
        "Wilbert07": {
            "username": "Wilbert07",
            "password": "admin123"
        }
    }
    
    def __init__(self):
        pass

    def withdraw(self, username, withdraw_amt):
        if withdraw_amt > self.accounts[username]["balance"]:
            print("You have insufficient balance to withdraw")
        else:
            self.accounts[username]["balance"] -= withdraw_amt
            print(f"You have successfully withdrawn Php {withdraw_amt} from your bank account.")

    def deposit(self, username, deposit_amt):
        if deposit_amt <= 0:
            print("You can not deposit negative amount of money.")
        else:
            self.accounts[username]["balance"] += deposit_amt
            print(f"You have successfully deposited Php {deposit_amt} to your bank account.")

    def transfer_fund(self, username, recipient, transfer_amt):
        if recipient in self.accounts:
            if transfer_amt > self.accounts[username]["balance"]:
                print("Insufficient balance for transfer.")
            else:
                self.accounts[username]["balance"] -= transfer_amt
                self.accounts[recipient]["balance"] += transfer_amt
                print(f"Succesfully transferred Php {transfer_amt} to {recipient}.")
        else:
            print("Recipient account does not exist.")

    def register(self, name, password, email, username, intl_bal):
        if username in self.accounts:
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
            Model.accounts.update(new_account)

    def check_bank_info(self, username):
        print(f"Name: {self.accounts[username]['name']}")
        print(f"Username: {self.accounts[username]['username']}")
        print(f"Password: {self.accounts[username]['password']}")
        print(f"Balance: {self.accounts[username]['balance']}")
        print(f"Email: {self.accounts[username]['email']}")

