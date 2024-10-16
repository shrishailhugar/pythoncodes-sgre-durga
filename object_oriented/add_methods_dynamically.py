class AddMethodDynamic():
    pass


def __init__(self,name):
    self.name=name
def change_name(self,name):
    self.name=name

AddMethodDynamic.__init__=__init__
AddMethodDynamic.method1=change_name
obj=AddMethodDynamic('Guru')
print(obj.name)
obj.method1('Abhi')
print(obj.name)