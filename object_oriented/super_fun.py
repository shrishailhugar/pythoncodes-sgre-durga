class Person:
    parent_class_value=20
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def fun1(self):
        print('Parent fun1')
    @classmethod
    def classfun(cls):
        return ('Inside classmethod')
    @staticmethod
    def staticmethod():
        return ('Inside staticmethod')
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary

    def fun1(self):
        super().fun1()
        print('Child Fun1')
        print(super().parent_class_value)
        # print(super().name)
        print(super().staticmethod())
        print(super().classfun())
    @classmethod
    def classfun(cls):
        super().fun1()


obj_empolyee=Employee('prajwal',12,100000)
obj_empolyee.fun1()
obj_empolyee.classfun()
