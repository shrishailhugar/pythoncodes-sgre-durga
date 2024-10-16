#the execution of decorator is always BOTTOM ------>> TOP
#in the first decorator we need to call func()
#in next decorator we need to get func type of which will be the return type of last decorator
def get_lower(func):
    print('in Lower')
    def wrapper():
        print('in lower wrapper')
        print(func)
        print('func()=',func())
        #this is the first decorator we need to call function func() which will return string.
        return func().lower()
    return wrapper()
def make_split(func):
    print('In split')
    def wrapper():
        print('in split wrapper')
        print(type(func))
        print(func.split())
        return func.split()
    return wrapper()

def get_first(func):
    print('in get_first')
    def wrapper():
        print('in get_first wrapper')
        return func[0]
    return wrapper()
def get_first_char(func):
    print('In get_first_char')
    def wrapper():
        print('in get_first_char wrapper')
        return func[0]
    return wrapper()
@get_first_char
@get_first
@make_split
@get_lower
def function():
    return 'Hi Shree'

print(function)