class BalanceException(Exception):
    pass
    
class BankAccount:
    def __init__(self,initial_amount,acct_name):
        self.balance=initial_amount
        self.name=acct_name
        print(f"\n Account '{self.name}' created. \n Balance=$ {self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' \n balance = ${self.balance:.2f}")
    def deposit(self,amount):
        self.balance =self.balance+amount
        print("\n Desposit complete")
        self.get_balance()
    def transcation (self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\n Sorry ,account '{self.name}' only has a balance of $ {self.balance:.2f}")
    def withdraw (self ,amount):
        try:
            self.transcation(amount)
            self.balance=self.balance-amount
            print("\n Transcation successful")
            self.get_balance()
        except BalanceException as error:
            print(f"Withraw interruped:{error}")
    def transfer (self,amount,account):
        try:
            print('\n ********* \n' \
            'Begining Transfer...')
            self.transcation(amount)
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceException as error:
            print(f"\n Transfer interrupted. {error}")

class InterstRewardAcct(BankAccount):
     def deposit(self,amount):
        self.balance =self.balance+(amount*1.05)
        print("\n Desposit complete")
        self.get_balance()


class SavingAcct(InterstRewardAcct):
        def __init__(self,initial_amount,acct_name):
            super().__init__(initial_amount,acct_name)
            self.fee =5
        def withdraw(self, amount):
            try:
                self.transcation(amount+self.fee)
                self.balance=self.balance-(amount+self.fee)
                print("\n Withdraw Completed")
            except BalanceException as error:
                print(f"\n Withdraw interrupted. {error}")
