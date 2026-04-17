class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name = holder_name # public attribute
        self._branch = "banani 11"  # protected
        self.__balance = initial_deposit # this is privet attribute
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return f'forkia taka nai'



rafsun = Bank("choooto bro",10000)

print(rafsun.holder_name)
rafsun.deposit(4000)
print(rafsun.get_balance())

print(rafsun._branch)

print(dir(rafsun))
rafsun._Bank__balance = 0
print(rafsun._Bank__balance)