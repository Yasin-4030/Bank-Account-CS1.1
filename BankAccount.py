
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
        print (f'Amount Deposited: ${amount}')
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount}')
        else:
            print("Insufficient funds")

    def get_balance(self):
        return f'Your current balance is: ${self.balance}'

    def add_interest(self):
        monthly_interest = self.balance *  0.00083
        print(f'Your monthly interest is: {monthly_interest}')

    def print_receipt(self):
        print()
        # print(self.full_name)
        # print(self.account_number)
        # print(self.routing_number)
        # print(self.balance)
        print('{} with account# {} has ${} in account.'.format(self.full_name, self.account_number, self.balance))
        

account = BankAccount("Mohammad", 20172648, 772017264, 2600)
account.deposit(900)
# print(account.get_balance())
account.withdraw(220)
print(account.get_balance())
account.add_interest()
account.print_receipt()