from functools import reduce
print(reduce(lambda a,b:a+b,range(10)))
print(list(filter(lambda a:a%2==0, range(10))))
print(list(map(lambda a,b:a+b,range(10),range(10))))


def splitter(func):
    def wrapper():
        obj=func()
        return obj.split()
    return wrapper

def lowerer(func):
    def wrapper():
        obj=func()
        # print('inside low=',obj)
        return obj.lower()
    return wrapper

@splitter
@lowerer
def lowsplit():
    return 'Hello World'
print(lowsplit())