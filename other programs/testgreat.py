while True:
    a,b,c,d=eval(input('Enter the 4 numbers:'))
    res=a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
    print(res)