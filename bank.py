class BankAccount:
    def __init__(self, name):
        self.name = name
        self.is_open = False
        self.__balance = 0

    def open(self):
        self.is_open = True

    def close_account(self):
        self.is_open = False

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('Account is closed')

        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('Account is closed')

        if abs(amount) >= self.__balance:
            raise ValueError('Insufficient balance')     

        self.__balance -= abs(amount)
        return self.__balance    

    def get_balance(self):
        if not self.is_open:
            raise ValueError('Account is closed')
        return self.__balance 

    def set_balance(self, amount):
        if not self.is_open:
            raise ValueError('Account is closed')
        self.__balance = amount        
                
if __name__ == "__main__":
    owner = BankAccount('Mercy')
    print(owner.is_open)
    owner.open()
    print(owner.is_open)
    owner.set_balance(40000000)
    owner.get_balance()
    print(owner.get_balance())
    print(owner.withdraw(100000))
   


