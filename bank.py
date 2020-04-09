class Account:
    def __init__(self, name, account_id, balance):
        self.name = name
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
    def get_money(self, get):
        self.balance-=get
acc = Account("Nasko", "1234", 120)
print(acc.balance)
acc.deposit(200)
print(acc.balance)
acc.get_money(10)
print(acc.balance)
