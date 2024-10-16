class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
class Employee(Person):
    def __init__(self,name,age,salary,eid):
        super().__init__(name,age)
        self.salary=salary
        self.eid=eid
    def display(self):
        super().display()
        print(self.salary)
        print(self.eid)
e=Employee('Bapu','15',1000000,'123')
e.display()