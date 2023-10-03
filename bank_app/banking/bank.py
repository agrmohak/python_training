from banking.accounts.bank_account import BankAccount, SavingsAccount, CurrentAccount, OverDraftAccount
import banking_exceptions.exceptions as ex

class Bank:
    def __init__(self, name, address):
        self._name = name
        self.address = address
        self.__accounts = []
        self.__last_id = 1

    def is_valid_account(self, account):
        return isinstance(account, BankAccount)

    def create_account(self, name,password, balance = 0 , account_type='SAVING'):
        if account_type.upper()=='CURRENT' :
            account = CurrentAccount(self.__last_id, name, password, balance)

        elif account_type.upper()=='OVERDRAFT' :
            account = OverDraftAccount(self.__last_id, name, password, balance)

        else:
            account = SavingsAccount(self.__last_id, name, password, balance)

        self.__accounts.append(account)
        self.__last_id += 1
        return account._id
    
    def close_account(self, account_num, password):
        account = self.get_account(account_num)
        if account.authenticate(password):
            balance = account._balance
            self.__accounts.remove(account)
            return balance

    def authenticate(self, account_num, password):
        account = self.get_account(account_num)
        if account:
            return account._password == password
        raise ex.IncorrectPassword
    
    def get_account(self, account_number) -> BankAccount:
        for index, account in enumerate(self.__accounts):
            if account._id == account_number:
                return account
        
        raise ex.AccountDoesNotExist
    

    def delete_account(self, account_number):
        account = self.get_account(account_number)
        self.__accounts.remove(account)

    def transfer_money(self, from_account_num, to_account_num, amount, password):

        from_account = self.get_account(from_account_num)
        to_account = self.get_account(to_account_num)
        print(from_account)
        print(to_account)
        if from_account.withdraw(amount, password):
            to_account.deposit(amount)
            return True
        
        raise ex.InsufficientFunds
    
    def info_all__accounts(self, account_type=''):
        for account in self.__accounts:
            print(f'Number : {account._id}\t Name: {account._name}\t Balance {account._balance}')
    
    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
            return True
    

    def withdraw(self, account_number, amount, password):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount, password)
            return True


    def credit_interest_all(self):
        for account in self.__accounts:
            account.credit_interest()

    
