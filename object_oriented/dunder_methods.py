# .__init__ and .__str__ called dunder methods. because they begin and end with double underscores
class Dunder():
    def __init__(self,age):
        self.age=age
    def __str__(self):
        return 'Hi this is age factor class'

obj=Dunder(27)
print(obj)