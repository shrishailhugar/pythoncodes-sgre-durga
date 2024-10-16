
def decoratorfun(func):
    def wrapper(a ,b):
        print("i'm inside this wrapper to decorate add function")
        return func(a ,b)
    return wrapper

@decoratorfun
def add(a ,b):
    print( a +b)

add(2 ,3)

#########################################################################


def lowfun(func):
    def wrapper():
        print('inside lower')
        obj =func()
        print(obj)
        lower =obj.lower()
        return lower
    return wrapper


def splitfun(func):
    def wrapper():
        print('inside split')
        obj =func()
        print(obj)
        splitword =obj.split()
        return splitword
    return wrapper

@splitfun
@lowfun
def function():
    return "Hello World!"

print(function())

######################################################


# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


# human = Celsius(37)

# print(human.temperature)

# print(human.to_fahrenheit())

# human.temperature = -300