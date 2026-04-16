class bank:

    def __init__(self,balance):
        self.balance = balance
        self.min_b = 100
        self.max_b = 100000

    def get_b (self):
        return self.balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
    
    def withdraw(self,amount):
        if amount < self.min_b:
            return f'you can\'t withdraw this mony min eto {self.min_b}  '
        elif amount > self.max_b:
            return f'you only withdraw at a time this mony {self.max_b}'
        elif amount > self.balance:
            return f'you can\'t have enough mony your balance {self.balance} '
        else:
            self.balance-= amount
            return f'you withdraw this mony {amount} now your balance is {self.balance}'


barak = bank(10000)

print(barak.withdraw(100000))