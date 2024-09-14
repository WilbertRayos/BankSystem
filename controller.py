import time

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.curr_user = None

    def login(self):
        try:
            menu_choice = int(self.view.main_menu())
            if menu_choice == 1:
                username, password = self.view.login()
                if username in self.model.credentials:
                    if password == self.model.credentials[username].get("password"):
                        self.curr_user = username
                        print(f"Login Successful. Welcome {self.curr_user}")
                        time.sleep(1)
                        self.run()
                    else:
                        print("Incorrect password")
                        time.sleep(1)
                        self.login() 
                else:
                    print("Username does not exist.")
                    time.sleep(1)
                    self.login() 
            elif menu_choice == 2:
                print("Exiting System...")
            else:
                raise ValueError
        except ValueError as e:
            print("Invalid Input")
            self.login()

    def run(self):
        while True:
            if not self.curr_user:
                self.login()
                break
            else:
                while True:
                    try:
                        home_choice = int(self.view.home_page())
                        option = {
                            1: self.register,
                            2: self.deposit,
                            3: self.withdraw,
                            4: self.transfer_fund,
                            5: self.check_info,
                            6: self.logout
                        }
                        if home_choice in option:
                            if home_choice == 6:
                                self.logout()  
                                break
                            else:
                                option[home_choice]() 
                        else:
                            raise ValueError
                    except ValueError as e:
                        print("Invalid Input...")

    def register(self):
        name, password, email, username, initial_balance = self.view.register()
        try:
            self.model.register(name, password, email, username, initial_balance)
            print("Registration Successful")
        except Exception as e:
            print("An error occurred during registration")

    def deposit(self):
        try:
            username, amount = self.view.deposit()
            self.model.deposit(username, amount)
            print("Deposit Success")
        except ValueError:
            print("Invalid Input...")
        except KeyError:
            print("Invalid Account. Please Register the account...")
        except Exception as e:
            print("An error occurred. Deposit failed...")

    def withdraw(self):
        try:
            username, amount = self.view.withdraw()
            self.model.withdraw(username, amount)
            print("Withdraw Success")
        except ValueError:
            print("Invalid Input")
        except KeyError:
            print("Invalid Account")
        except Exception as e:
            print("An error occurred. Withdraw failed...")

    def transfer_fund(self):
        try:
            username, recipient, amount = self.view.transfer_fund()
            self.model.transfer_fund(username, recipient, amount)
            print("Transfer of funds Successful")
        except ValueError:
            print("Invalid Input")
        except KeyError:
            print("Invalid Account")
        except Exception as e:
            print("An error occurred. Transfer of funds failed")

    def check_info(self):
        try:
            username = self.view.check_info()
            self.model.check_bank_info(username)
        except ValueError:
            print("Invalid Input")
        except KeyError:
            print("Invalid Account")
        except Exception as e:
            print("An error occurred.")

    def logout(self):
        print(f"Logging out {self.curr_user}...")
        self.curr_user = None  
        time.sleep(1)
        print("Logged out successfully.")
