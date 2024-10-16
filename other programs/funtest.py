def add_fun(*n):
    print(type(n))
    print(sum(n))

add_fun(1,2,3,4,5,6,7)

num1=10
def add_2_num(num1,num2):
    return num1+num2

print(add_2_num(2,3))
print(num1)

def fun_auth(card,pin):
    pass






def fun_withraw(card,pin,amount):
    fun_auth(card,pin)
    total_amount=get_total_amount()
    if total_amount-amount>500:
        total_amount=total_amount-amount
    else:
        print('minimum balance policy is stopping this operation')

def fun_deposit(card,pin,amount):
    fun_auth(card, pin)

def fun_check_balanace(card,pin):
    fun_auth(card,pin)

def get_total_amount():
    return 5000

print(num1)