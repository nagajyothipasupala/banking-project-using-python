
import random
class Create():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def check_passsword(self):
        return self.password==password
accounts=[]
loginaccount=None

while True:     
    print("1.create bank account:\n2.login:\n")
    choice=int(input("enter choice:"))
    if choice==1:
        username=input("enter username:")
        password=input("enter password:")
        accounts.append(Create(username,password))
        print("Bank Account Created Succesfully")
    elif choice==2:
        username=input("enter username:")
        password=input("enter password:")
        print(username,"login success")
        for account in accounts:
            if account.username==username and account.password==password:
                loginaccount=account
                break
            print("login successful")
        if  loginaccount is None:
            print("enter valid details")
        else:
            print("you are logged in as",username)
            break    
    else:
        print("enter the correct choice")
        break        
"""
class Bank_Account():
    def __init__(self,account_number,account_balance=0):
        self.account_number=account_number
        self.account_balance=account_balance

    def deposit(self,amount):
        a=int(input("enter amount to deposit:"))
        if amount>0:
            self.account_balance+=amount
            print("amount deposited in your account is:",self.account_balance)       
        else:
            print("depositing amount should be more than 0")
    def withdraw(self,amount):
        b=int(input("enter amount to withdraw:"))
        if amount>0 and amount<self.account_balance:
            self.account_balance-=amount
            print("withdrawn amount is:",self.amount)   
        else:
            print("invalid amount to withdraw")
    def get_account_balance(self):
               return "total account balance is:",self.account_balance
"""
while True:
    pnr=[]
    pnr.append(random.randint(1000000,9999999))
    print(username,"your account number is:",pnr)
    print("enter your choice to do transactions:\n1.deposit\n2.withdraw\n3.total balance\n4.exit\n")
    choice=int(input("select an option:"))
    if choice==1:
        amount=int(input("enter amount to deposit:"))
        print("deposited ampount is:",amount)
        print("total amount in your account is:",amount)
        
    if choice==2:
        w_amount=int(input("enter amount to withdraw:"))
        if w_amount<amount and w_amount>0:
            print("withdrawn amount is:",w_amount)
            amount=amount-w_amount
            print("current balance is",amount)
        else:
            print("unsufficient amount")    

        
    if choice==3:
        print("current balance is:",amount)
    if choice==4:
        print("exit")
        break


    
           
                                    


