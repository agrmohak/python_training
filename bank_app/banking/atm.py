from banking.bank import Bank
from utils.input import read_value
import banking_exceptions.exceptions as BankingExceptions
class ATM: 
    
    def __init__(self, Bank:Bank):
        self.__Bank = Bank
        self._keyboard = read_value

    def start(self):
        print('ATM Menu')
        self._account_number= self._keyboard('Account Number?',int)
        self._password= self._keyboard('Password?')

        if self.__Bank.authenticate(self._account_number, self._password) :
            self._user_menu()

    def _user_menu(self):
        while True:
            choice=self._keyboard('1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transfer\n5. Close Account\n0. Exit\n Choose:',int)
            try:
                if choice == 1:
                    self._do_deposit()

                elif choice == 2:
                    self._do_withdraw()

                elif choice == 3 :
                    self._check_balance()

                elif choice == 4:
                    self._do_transfer()

                elif choice == 5:
                    self._do_close_account()
                
                elif choice == 0:
                    self._show_message('Thank you for banking with us')
                    return True
                return True
            
            except Exception as ex:
                print(ex)
                continue

    def _do_close_account(self):
        if self._keyboard('To close account type CLOSE ACCOUNT : ') == 'CLOSE ACCOUNT':
            balance = self.__Bank.close_account(self._account_number, self._password)
            self._dispense_cash(balance)
            self._show_message('Account closed succesfully')
        
    def _check_balance(self):
        account = self.__Bank.get_account(self._account_number)
        if account:
            self._show_message(f'Available Balance : {account._balance}')
        
    def _do_transfer(self):
        to_account = self._keyboard('Account Number', int)
        amount = self._keyboard('Amount', int)
        self.__Bank.transfer_money(self._account_number, to_account, amount, self._password)

    def _do_deposit(self):
        amount = self._keyboard('Enter amount to deposit', int)
        self.__Bank.deposit(self._account_number, amount)

    def _do_withdraw(self):
        amount = self._keyboard('Enter amount to be withdrawn', int)
        self.__Bank.withdraw(self._account_number, amount, self._password)
        self._dispense_cash(amount)

    def _dispense_cash(self, amount):
        self._show_message(f'Please take your cash {amount}')

    def _show_message(self,message):
        print(message,' ')


    