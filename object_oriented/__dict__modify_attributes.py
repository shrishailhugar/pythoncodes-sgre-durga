class Modify():
    class_attribute=10
    def __init__(self,age):
        self.age=age

print(vars(Modify))
obj1=Modify(27)
print(vars(obj1))
#modifying class attribute
print(Modify.__dict__)
print(Modify.__dict__['class_attribute'])
Modify.__dict__['class_attribute']=50
print(Modify.__dict__['class_attribute'])
print(obj1.__dict__)
print(obj1.__dict__['age'])
obj1.__dict__['age']=25
print(obj1.__dict__['age'])