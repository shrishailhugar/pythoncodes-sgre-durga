s='Hi Bapu how are you Bro'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.swapcase())
print(s.title())

def fibonacci(n):
    a,b=0,1
    while(a<=n):
        # print(f'a={a},b={b}')
        yield a
        x=a
        a=b
        b+=x
for i in fibonacci(10):
    print(i)