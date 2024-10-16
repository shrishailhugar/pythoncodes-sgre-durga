number=eval(input('Enter the number:'))


count=0
def fact1(n):
    global count
    count+=1
    if n==0:
        return 1
    else:
        return n*fact1(n-1)


print(fact1(number))

def factorial(n):
    if n>1:
        print(n)
        return n*factorial(n-1)
    else:
        return 1

print(factorial(number))
print(globals()['count'])