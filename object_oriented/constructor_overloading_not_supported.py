class Test:
    def __init__(self):
        print('no-arg')
    def __init__(self,x):
        print('one-arg')
    def __init__(self,x,y):
        print('two-arg')
# t=Test()
# t=Test(1)
t=Test(1,2)

class Test1:
    def __init__(self,a=None,b=None):
        print('Constructor with variabe lenght arg.')

t=Test1()
t=Test1(1)
t=Test1(1,2)