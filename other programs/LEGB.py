from math import pi
# print(pi)

pi=3.0
# print(pi)

def fun1():
   global pi
   # print(pi)
   pi=2
   return pi

print(fun1())
print(pi)