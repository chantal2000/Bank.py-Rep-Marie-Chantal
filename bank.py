from datetime import datetime
class Account:
    def __init__(self,name,phonenumber,loan):
        self.name=name
        self.loan=loan
        self.phonenumber=phonenumber
        self.balance=0
        self.statement=[]
        self.loan=0
    def showbalance(self):
        return  f"Hello {self.name} your balance is {self.balance}"
    def deposit(self,amount):
        try:
            10+amount
        except TypeError:
            return f"Amount must be figures"
        
        if amount<0:
            return f"amount can't be less than 0"
        else:
            self.balance += amount
            now=datetime.now()
            transaction={
                "amount":50,
                "time":now,
                "narration":"You deposited"
            }
            self.statement.append(transaction)
            return self.showbalance()
    def transfer(self,amount,name):
        try:
            10+amount
        except TypeError:
            return f"Amount must be figures"
        fee=amount*0.05
        total=amount+fee
        self.balance-=total
        if amount<0:
            return f"You can't transfer"
           
        elif total>self.balance :
            return f"your balance is {self.balance} and You need atleast {total}"
        else:
            self.balance-=total
            return f"Your balance is {self.balance}"

    def show_statement(self):
        for transaction in self.statement:
                    amount=transaction["amount"]
                    narration=transaction["narration"]
                    time=transaction["time"]
                    date=time.strftime("%d%m%y")
                    print(f"{date}: {narration} {amount}")
        return 
        
    def withdraw(self,amount):
        try:
            10+amount
        except TypeError:
            return f"Amount must be figures"
        if amount>self.balance:
            return f"Your balance is {self.balance} and You can not withdraw {amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            transaction={
                "amount":20,
                "time":now,
                "narration":"You withdrew"
            }
            self.statement.append(transaction)
            return self.showbalance()
    def show_statement(self):
        for transaction in self.statement:
                    amount=transaction["amount"]
                    narration=transaction["narration"]
                    time=transaction["time"]
                    date=time.strftime("%d%m%y")
                    print(f"{date}: {narration} {amount}")
        return 
        
    def borrow(self,amount):
        try:
            10+amount
        except TypeError:
            return f"Amount must be figures"
        if amount<0:
            return "You can't borrow"
        elif self.loan>0:
            return "You arleady have loan"
        elif amount<0.1*self.balance:
            return "You are not qualified"
        else:
            loan=amount*1.05
            self.loan=loan
            self.balance+=amount
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "narration":"You borrowed money"
            }
            self.statement.append(transaction)
            return f"{self.showbalance()} and you Your outstanding loan is {self.loan}"


    def repayloan(self,amount):
        try:
            10+amount
        except TypeError:
            return f"Amount must be figures"
        if amount<0:
            return "You have to pay"
        elif amount<self.loan:
            self.loan-=amount
            return "Entire Loan is not paid"
        else:
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff)
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "narration":"You repaid Your loan"
            }
            self.statement.append(transaction)
            return f"{self.showbalance()} and your loan is completely cleared"
class MobileMoneyAccount(Account):
    def __init__(self,name,phonenumber,loan,service_provider):
        Account.__init__(self,name,phonenumber,loan)
        self.service_provider=service_provider

    def buy_airtime(self,amount):
        try:
            10+amount
        except TypeError:
            return f"Amount must be figures"
        if amount<0:
            return f"Your balance is negative and You can't buy airtime"
        elif amount<self.balance:
            return f"Dear Customer Your balance is not sufficient;deposit money and try again"
        else:
            self.balance=self.balance-amount
            return f"Dear Customer; Your can Buy airtime and your balance is {self.balance} "
    def withdraw(self,amount):
        try:
            30000+amount
        except TypeError:
            return f"Amount must be figures"
        if amount>self.balance:
            return f"Your balance is {self.balance} and You can not withdraw {amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            transaction={
                "amount":20,
                "time":now,
                "narration":"You withdrew"
            }
            self.statement.append(transaction)
            return self.showbalance()
        





        




    