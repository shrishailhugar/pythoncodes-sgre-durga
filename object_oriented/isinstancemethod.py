#it is to find whether the given object is a part of class or not
#The action of creating concrete objects from an existing class is known as instantiation.
class Parent():
    def __init__(self):
        pass
class Child1(Parent):
    def __init__(self):
        pass
class Independent_child():
    def __init__(self):
        pass
parent_obj=Parent()
child1_obj=Child1()
ind_child=Independent_child()
#print the object from which class
print(type(child1_obj))

#isinstance will return true of false
print(isinstance(child1_obj,Parent))#True as it's inherited from Parent class
print(isinstance(ind_child,Parent))#False as it's not inherited from Parent class
print(isinstance(child1_obj,Child1))#True as it's the instance of class
print(isinstance(ind_child,Independent_child))#True as it's the instance of class
