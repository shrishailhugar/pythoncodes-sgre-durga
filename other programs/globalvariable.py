def f1():
    global a
    a=20
def f2():
    print(a)
    print(globals()['a'])
    print(globals())
f1()
f2()