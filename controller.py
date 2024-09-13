import time


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.curr_user = None
    
    def run(self):
        while True:
            
            try:  
                menu_choice = int(self.view.main_menu())
                
                if menu_choice == 1:
                        login_verdict = self.login()
                        # Login Successful
                        if login_verdict == 0:
                            home_verdict = self.home()
                            match home_verdict:
                                case 1:
                                    self.register()
                                case 2:
                                    self.deposit()
                                case 3:
                                    self.withdraw()
                                case 4:
                                    self.transfer_fund()
                                case 5:
                                    self.check_info()
                                case 6:
                                    self.logout()
                                case _:
                                    print("Invalid choice.")

                        # Invalid Username or Password
                        elif login_verdict == -1:
                            continue
                elif menu_choice == 2:
                    print("Exiting the application...")
                    time.sleep(2)
                    break
                else:
                    print("Invalid choice.")
                    time.sleep(2)

            except ValueError as e:
                print("Invalid input")
                time.sleep(2)
                continue

    
    def login(self):
        username, password = self.view.login()
        if username in self.model.credentials:
            if password == self.model.credentials[username].get("password"):
                self.curr_user = username
                return 0
            else:
                print("Incorrect password")
                time.sleep(2)
                return -1
        else:
            print("Username does not exists.")
            time.sleep(2)
            return -1


    def home(self):
        try:
            choice = int(self.view.home_page())  
            return choice
        except ValueError as e:
            print("Invalid input")
            time.sleep(2)
            return -1

    def register(self):
        name, password, email, username, initial_balance = self.view.register()
        try:
            self.model.register(name, password, email, username, initial_balance)
        except Exception as e:
            print("An error occured during registration")
    
    def deposit(self):
        username, amount = self.view.deposit()
        self.model.deposit(username, amount)
        print(self.model.accounts)

    def withdraw(self):
        username, amount = self.view.withdraw()
        self.model.withdraw(username, amount)
        print(self.model.accounts)

    def transfer_fund(self):
        username, recipient, amount = self.view.transfer_fund()
        self.model.transfer_fund(username, recipient, amount)
        print(self.model.accounts)
    
    def check_info(self):
        username = self.view.check_info()
        self.model.check_bank_info(username)
        print(self.model.accounts)

    def logout(self):
        self.run()
    
    