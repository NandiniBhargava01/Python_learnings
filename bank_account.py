class Account():
    def __init__(self,balance,acc_no):
        print("give balance and account number:")
        self.balance=balance
        self.acc_no=acc_no
        print("balance:",self.balance)
        print("account_number:",self.acc_no)

    def credit(self,acc_no,val):
        if acc_no==self.acc_no:
            self.balance=self.balance+val
        else:
            pass
        return self.balance

    def debit(self,acc_no,val):
        if acc_no==self.acc_no:
            self.balance=self.balance-val
        else:
            pass
        return self.balance

    def give_balance():
        print(self.balance)
        
        
