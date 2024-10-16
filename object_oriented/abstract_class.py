from abc import abstractmethod,ABC
class vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        pass
class Bus(vehicle):
    def no_of_wheels(self):
        return 4
class Auto(vehicle):
    def no_of_wheels(self):
        return 3

class Truck(vehicle):
    pass
b=Bus()
print(b.no_of_wheels())
a=Auto()
print(a.no_of_wheels())
# t=Truck()
