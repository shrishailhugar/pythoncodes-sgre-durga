def is_even(n):
    if n%2==0:
        return True
    else:
        return False


inp=eval(input('Enter list'))
fil_0bj=filter(is_even,inp)
print(type(fil_0bj))
print(fil_0bj)
print(list(fil_0bj))

print(list(filter(lambda a:True if a%2==0 else False,inp)))


#number divisible by 3
print(list(filter(lambda a: True if a%3==0 and a%2!=0 else False,inp)))

t1=eval(input('Enter Heroine names:'))
print(list(filter(lambda name: True if name[0]=='k' else False,t1)))

t1=eval(input('Enter first tuple1:'))
t2=eval(input('Enter 2nd tuple2:'))
print(list(filter(lambda x,y:True if x*y>10 else False,t1,t2)))