class Account:
    def __init__(self,balance,account):
        self.balance = balance
        self.account_no = account
    
    def debit(self, amount):
        self.balance -= amount
        print("You debit account Rs.",amount," \ncurrent balance is :",self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("You cedit account Rs.",amount,"\nyour balance is :",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 8273)
acc1.debit(1000)
acc1.credit(1000)