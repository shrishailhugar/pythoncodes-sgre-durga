# You can’t modify class attributes through instances of the containing class.need to cahnge by class_name.attribute.
class Counter_check():
    count = 0

    def __init__(self):
        self.count += 1


objcheck = Counter_check()
print(objcheck.count)
objcheck2 = Counter_check()
print(objcheck2.count)

print(Counter_check.count)
Counter_check.count = 5
print(Counter_check.count, objcheck.count)
objcheck1 = Counter_check()
print(objcheck1.count,Counter_check.count)

class Counter():
    count = 0

    def __init__(self):
        # Counter.count+=1
        print('in Parent class')
        print(self)  # <__main__.Counter object at 0x000001AB34B56300>
        type(self).count += 1  # with this you can avoid hardcoding


class Child(Counter):
    def __init__(self):
        print(type(self).count)
        type(self).count += 1
        super().__init__()


class Child1(Counter):
    def __init__(self):
        print('in child1 class')
        print(type(self))
        print(type(self).count)
        type(self).count += 1
        super().__init__()


Counter()  # called once
obj1 = Counter()
obj2 = Counter()
print(obj1.count, obj2.count, sep='  ')  # 3 3
# above you can see the variable is shared across all the objects.

chobj = Child()
print(chobj.count, obj1.count, obj2.count)  # 3 3 5
# because child we increased child object attribute so the parent class ,class-attribute not going to change(3+1=4)
# even with super it's passing parent a child object so the child class-attribute varied(4+1=5)
obj3 = Counter()
print(obj3.count, obj2.count, obj1.count)  # 4 4 4
# as the above all are parent class objects and class attributes are shared across all objects in the same level(level1).

chobj2 = Child1()
print(chobj2.count)


class Grand1(Child1):
    def __init__(self):
        print(type(self))
        print(type(self).count)


class Grand2(Child1):
    def __init__(self):
        print(type(self))
        print(type(self).count)


grobj1 = Grand1()
