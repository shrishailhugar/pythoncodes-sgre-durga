class Test:
    def summm(self,*args):
        print(type(args))
        print(args)
        print(sum(args))


t=Test()
t.summm()
t.summm(1,2)
t.summm(1,2,3,4,)