def lower(func):
    def wrapper(a,b):
        obj = func(a,b)
        return obj.lower()
    return wrapper

def split(func):
    def wrapper(a,b):
        obj = func(a,b)
        return obj.split()
    return wrapper

def add_ele(func):
    def wrapper(a,b):
        obj = func(a,b)
        obj.append(b.upper())
        return obj
    return wrapper

@add_ele
@split
@lower
def func(a,b):
   return (a+b)

print(func('Hi Welcome!','Shree'))
