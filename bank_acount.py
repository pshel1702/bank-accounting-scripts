# FIXME: Add Bank Account class definition here

#bank_account_class def:

class BankAccount:
    """Set initial balances and update based on deposits/withdrawals."""
    #Set default of balance as None, so that any value passed in will be set as balance
    def __init__(self,balance=0):
        self.balance = balance
    
    #Method to increase balance of current instance based on amount passed
    def deposit(self,amount):
       self.balance += amount
    
    #Method to reduce balance of current instance based on amount withdrawn
    def withdraw(self,amount):
        if amount>self.balance:
            print("Invalid transaction: not enough funds to withdraw $50.")
        else:
            self.balance -= amount


# You can see how this class should be used below. Make sure you
# run your code and test it out to make sure it works.

account_1 = BankAccount()
account_2 = BankAccount()
account_3 = BankAccount(100)
# account_3.balance
#   >>> 100
account_1.deposit(100)
#print(account_1.balance)
#   >>> 100
account_2.deposit(50)
#account_2.balance
#   >>> 50
account_3.deposit(75)
#account_3.balance
#   >>> 175
account_2.withdraw(10)
#print(account_2.balance)
#   >>> 40
account_1.withdraw(10)
# account_1.balance
#   >>> 90
account_2.withdraw(50)
#   >>> "Invalid transaction: not enough funds to withdraw $50." 
#print(account_2.balance)
#   >>> 40    # still 40 since the previous transaction was not successful
