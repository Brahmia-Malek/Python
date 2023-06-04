
class BankAccount:
    
    def __init__(self, int_rate, initial_balance=0): 
        self.int_rate=int_rate
        self.balance=initial_balance
        
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.interest_rate
            self.balance += interest

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate=0.02,initial_balance=0)
    def make_deposit(self,amount):
        self.account.deposit(amount)
    def make_withdraw(self,amount):
        self.account.withdraw(amount)  
    def  display_user_balance(self,balance):
        self.account.balance(balance)     

brahmia=User("brahmia","brahmia.malek@yahoo.com")
brahmia.account.make_deposit(50)
