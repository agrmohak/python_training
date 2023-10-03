import banking_exceptions.exceptions as ex
class BankAccount:
    def __init__(self, account_number, name, password, balance):
        self._id = account_number
        self._name = name
        self._balance = balance
        self._password = password
        self._interest_rate = 8

    def authenticate(self, password):
        if self._password == password: 
            return True
        raise ex.IncorrectPassword
            
    def check_balance(self):
        return self._balance
    
    def is_valid_transact_amount(self, amount):
        if(amount > 0):
            return True
        raise ex.InvalidAmount
    
    def withdraw(self, amount, password):
        if self._balance <0 :
            raise ex.InsufficientFunds
        self.is_valid_transact_amount(amount)
        self.authenticate(password)
        self._balance -= amount
        return True
        
    
    def deposit(self, amount):
        self.is_valid_transact_amount(amount)
        self._balance += amount
        return True

    def credit_interest(self):
        if self._balance > 0:
            interest = self._balance * self._interest_rate/1200
            self.deposit(interest)

    def __str__(self):
        return f'{type(self).__name__}[Name : {self._name}\t Balance : {self._balance}]'
    
    def __repr__(self):
        self.__str__()

class SavingsAccount(BankAccount):
    def __init__(self, account_number, name, password, balance, min_balance=5000):
        super().__init__(account_number, name, password, balance)
        self._interest_rate = 12
        self._min_balance = min_balance
    
    
    def get_max_withdrawal_amount(self):
        return self._balance - self._min_balance
    
    def withdraw(self, amount, password):
        if amount < self.get_max_withdrawal_amount(): 
            return super().withdraw(amount, password)
    

class CurrentAccount(BankAccount):
    def __init__(self, account_number, name, password, balance):
        super().__init__(account_number, name, password, balance)
        self._interest_rate = 0
        self._min_balance = 0
    
class OverDraftAccount(BankAccount):
    def __init__(self, account_number, name, password, balance):
        super().__init__(account_number, name, password, balance)
        self._interest_rate = 8
        self._max_balance = 0
        self._od_fee_interest = 1
        self._utilised_od = 0


    def get_od_limit(self):
        limit = self._max_balance / 10
        return limit
    
    def get_max_withdrawal_amount(self):
        return self._balance + self.get_od_limit()
    
    def calculate_od_fee(self, amount):
        return (amount - self._balance)/100
    
    def withdraw(self, amount, password):
        if(amount < self.get_max_withdrawal_amount()):
            od_fee = self.calculate_od_fee(amount)
            super().withdraw(amount, password)
            super().withdraw(od_fee, password)
            return True
        raise ex.InvalidAmount
    
    def update_max_balance(self):
        if self._balance > self._max_balance:
            self._max_balance = self._balance

    def deposit(self, amount):
        super().deposit(amount)
        self.update_max_balance()
        