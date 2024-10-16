class Test:
    def m1(self):
        print('No arg')
    def m1(self,x):
        print('one -arg')
    def m1(self,x,y):
        print('2 arg')

t=Test()
# t.m1()
# t.m1(1)
t.m1(1,2)

#get name of passed arg class
#here we can use same method for all the operations irrespective of type of arg passed
#actually no need of method overloading
class Test1:
    def m1(self,x):
        print(f'{x.__class__.__name__} method is supported')
t1=Test1()
t1.m1(10)
t1.m1(10.5)
t1.m1('a')