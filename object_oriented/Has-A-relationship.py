class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def info(self):
        print(f'The car is {self.name} and color is {self.color}')

class Eemployee:
    def __init__(self,name,id,car):
        self.name=name
        self.id=id
        self.car=car
    def m2(self):
        print(f'Employee name {self.name} having id{self.id} has {self.car.name} of {self.car.color} color')


c=Car('Tata','Red')
e=Eemployee('Guru','14231423',c)
e.m2()


        