from functools import reduce
t1=eval(input('Enter tuple:'))
print(reduce(lambda x,y:x+y,t1))
print(reduce(lambda x,y:x+y,range(0,10)))