class Account:
    def __init__(self,name,mobile_no,location,balance):
        self.name=name
        self.mobile_no=mobile_no
        self.location=location
        self.balance=balance
    def balance_enquary(self):
        return f'Your total balance is {self.balance}'
    def deposit(self,amount):
        self.balance+=amount
        return f'Amount deposited successfully total balance is {self.balance}'
    def withdraw(self,amount):
        if (self.balance-amount)<500:
            return f'Cannot proceed the transaction as minimum balance is not securing'
        else:
            self.balance-=amount
            return f'Successfully debited amount left balance is {self.balance}'

ac1=Account('shantanu',8123232232,'luckno',500)
ac2=Account('shree',82223434535,'banglore',5000)
print(ac1.balance_enquary())
print(ac1.deposit(400))
print(ac2.balance_enquary())
print('id of ac1=',id(ac1))
print('id of shantanu',id(ac1.name))
print('id of ac2=',id(ac2))

s='abcd'
print('id of a=',id(s[0]))
print('id of b=',id(s[1]))
print('id of c=',id(s[2]))
print('id of d=',id(s[3]))