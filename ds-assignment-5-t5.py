class Account: 
    def _init_(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance = self.balance - amount
    

    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def _init_(self, title=None, balance=0, interestRate=0):
        super()._init_(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate / 100)


obj1 = SavingsAccount("preethi", 2000, 5)
print("Initial Balance:", obj1.getBalance())
obj1.withdrawal(500)
print("Balance after withdrawal:", obj1.getBalance())
obj1.deposit(500)
print("Balance after deposit:", obj1.getBalance())
print("Interest on current balance:", obj1.interestAmount())
