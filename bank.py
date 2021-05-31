from datetime import datetime
class Account:
    def __init__(self,name,phonenumber,loan):
        self.name=name
        self.loan=loan
        self.phonenumber=phonenumber
        self.balance=0
        self.statement=[]
    def showbalance(self):
        return  f"Hello {self.name} your balance is {self.balance}"
    def deposit(self,amount):
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
    def show_statement(self):
        for transaction in self.statement:
                    amount=transaction["amount"]
                    narration=transaction["narration"]
                    time=transaction["time"]
                    date=time.strftime("%d%m%y")
                    print(f"{date}: {narration} {amount}")
        return 
        
    def withdraw(self,amount):
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
        return f"Hello {self.name}, you have borrowed{self.loan}; your new balance is {amount-self.loan} "
    def repayloan(self,amount):
        return f"Hello {self.name}, you have repaid {self.loan} ; your new balance is{amount-self.loan+self.loan}"
    