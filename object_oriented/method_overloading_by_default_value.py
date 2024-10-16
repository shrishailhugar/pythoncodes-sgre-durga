class Test:
    def m1(self,a=None,b=None):
        if a is not None and b is not None:
            print('2 arg')
        elif a is not None:
            print('1-arg')
        else:
            print('no-arg')
t=Test()
t.m1(1,2)
t.m1(1)
t.m1()
