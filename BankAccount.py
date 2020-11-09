
class BankAccount():
    full_name = ""
    account_number = ""
    routing_number = ""
    balance = 0

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            # print("Amount Withdrawn:")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return f'Your current balance is: ${self.balance}'

    # def add_interest(self):
        # interest = self.balance *  0.00083

account = BankAccount("Mohammad", 2017264, 772017264, 2600)
account.deposit(900)
# print(account.get_balance())
account.withdraw(220)
print(account.get_balance())