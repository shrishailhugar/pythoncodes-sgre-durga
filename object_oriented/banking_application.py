class Bank:
    brnach='Honaganahalli'
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def get_balance(self):
        return self.balance
    def deposit(self,balance):
        self.balance+=balance
        print(f'You have successfully added money {balance} for {self.name} account')

    def withdraw(self,amount):
        if (self.balance-amount<500):
            print('Cannot proceed this transaction as it is against minimum balance')
        else:
            self.balance-=amount
            print(f'Successfully withdrawn {amount} from {self.name} account')

bank_obj=Bank('Bapu',1000)
while True:
    inp=input('Enter d for deposit, w for withdraw,e for ending,g to get balanace: ')
    if inp=='d':
        amount=int(input('Enter amount to be deposited:'))
        bank_obj.deposit(amount)
    elif inp=='w':
        amount = int(input('Enter amount to be deposited:'))
        bank_obj.withdraw(amount)
    elif inp == 'g':
        print(bank_obj.get_balance())
    elif inp=='d':
        break
    else:
        print('Please provide valid arg:')