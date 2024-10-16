class Book():
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages

b1=Book(200)
b2=Book(300)
b3=Book(100)
print(b1+b2)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self, other):
        return self.marks>other.marks
    def __le__(self,other):
        return self.marks<=other.marks

s1=Student('A',544)
s2=Student('B',443)
s3=Student('C',225)
print(s1>s2)
print(s3>s2)
print(s2<s3)#no need to lt if gt implemented
print(s1<=s2)
print(s1>=s2)#no need to implement le if ge implemented
