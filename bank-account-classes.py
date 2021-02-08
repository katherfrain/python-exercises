class BankAccount: 

    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, add_amount = 0):
        if add_amount == 0:
            add_amount = float(input('How much money would you like to deposit? Please enter the amount without a dollar sign. '))
        self.balance = self.balance + add_amount
        print(f'You have added {add_amount} to your balance, reaching ${self.balance}')

    def withdraw(self, withdrawl_amount = 0):
        if withdrawl_amount == 0:
            withdrawl_amount = float(input('How much money would you like to withdraw? Please enter the amount without a dollar sign. '))
        self.balance = self.balance - withdrawl_amount
        print(f'You have withdrawn ${withdrawl_amount} from your account, leaving ${self.balance} remaining.')

    def transfer_funds(self, transfer_destination = ""):
        transfer_funds = float(input('How much money would you like to transfer? '))
        
        if transfer_destination == "":
            transfer_destination = input('What is the destination of your transfer? ')

        self.withdraw(transfer_funds)
        transfer_destination.deposit(transfer_funds)
        



savings = BankAccount(100, 1040)
savings.deposit()

checking = BankAccount(100, 1050)
print(savings.balance, checking.balance)
savings.transfer_funds(checking)
print(savings.balance, checking.balance)
