print('Hi')
try:
    print(10/0)
except ZeroDivisionError as e:
    print(type(e))
    print(e.__class__)
    print(e.__class__.__name__)
print('Hello')