l=['t','i','m','r','l']
while True:
    inp_number=int(input('Enter number:'))
    if inp_number<6:
        print(l[inp_number-1])
    else:
        a=(inp_number-5)%4
        b=(inp_number-5)//4
        if b%2!=0:
            print(l[a])
        else:
            print(l[-a-1])