# protected can be accessed outside class and in base classes
# private can be inside class only
# AttributeError: 'child' object has no attribute '_child__privvar'
class Parent:
    def __init__(self):
        self._protvar = 3
        self.__privvar = 4

    def getprivvalue(self):
        print(f'privavalueof class ={self.__privvar}')


class child(Parent):
    def __init__(self):
        super().__init__()
        print("calling the protected var value from parent class", self._protvar)
        # print("Fetching the private var value from parent class",self.__privvar)

        self._protvar = 5
        self.__privvar = 6
        print("calling the protected var value from par child class", self._protvar)
        print("calling the private var value from child class", self.__privvar)


childObj = child()
parentobj = Parent()
print(parentobj._protvar)
# print(parentobj.__privvar)
parentobj.getprivvalue()