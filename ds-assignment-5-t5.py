class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate / 100 ) 
        

obj = SavingsAccount("Pratham",1000,5)
print("Initial Balance : ",obj.getBalance())
obj.withdrawal(500)
print("Balance after withdrawal : ",obj.getBalance())
obj.deposit(1500)
print("After deposit : ",obj.getBalance())
print("Intrest on current balance : ",obj.interestAmount())
