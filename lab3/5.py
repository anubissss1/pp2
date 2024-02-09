class Account:
    def __init__(self, s):
        self.owner = s
        self.balance = 0
    def get_balance(self):
        print(f'{self.owner} has {self.balance} money')
    def deposit(self, x):
        self.balance += x
    def withdraw(self, x):
        if x <= self.balance:
            self.balance -= x
        else:
            print("You don't have that much money!")

x = Account("Vika")
x.deposit(100)
x.deposit(50)
x.get_balance()
x.withdraw(140)
x.get_balance()
x.withdraw(20)
x.get_balance()
x.withdraw(10)
x.get_balance()