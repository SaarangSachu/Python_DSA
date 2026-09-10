class Account:
    def __init__(self,account_number,account_holder_name):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self._balance=0.0

    def deposit(self,amount):
        if amount>0:
            self._balance=self._balance+amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self,amount):
        if amount>0:
            if amount>self._balance:
                print("Insufficient Money")
            else:
                self._balance=self._balance-amount
                
        else:
            print("enter a valid amount")

    def get_balance(self):
        return self._balance

class SavingAccount(Account):
    def __init__(self,account_number,account_holder_name,interest_rate):

        super().__init__(account_number,account_holder_name)
        self.interest_rate=interest_rate

    def add_interest(self):
        self.deposit(self.get_balance()*self.interest_rate)


class CheckingAccount(Account):
    def __init__(self,account_number,account_holder_name,overdraft_limit):
        super().__init__(account_number,account_holder_name)
        self.overdraft_limit=overdraft_limit

    def withdraw(self,amount):
        if amount>0:
            if amount<=(self._balance+self.overdraft_limit):
                self._balance-=amount
            else:
                print("Transaction declined:Exceeds overdraft limit")
        else:
            print("invalid amount")

class Customer:
    def __init__(self,name,customer_id):
        self.name=name
        self.customer_id=customer_id
        self.accounts=[]

    def add_account(self,account):
        self.accounts.append(account)

    def get_total_balance(self):
        total=0
        for i in self.accounts:
            total+=i.get_balance()
        return total

# Create The Customer
alice=Customer("Alice","001")
# Create The Account
alice_saving=SavingAccount("101","Alice",0.05)
alice_checking=CheckingAccount("202","Alice",500)
# Transaction
alice_saving.deposit(1000)
alice_checking.withdraw(200)
# add acount to customer
alice.add_account(alice_saving)
alice.add_account(alice_checking)
# Check net worth
print(f"Alice's total net worth is: ${alice.get_total_balance()}")

