class Test:
    a=10
    def __init__(self):
        Test.b=20
        type(self).b=30
    def m1(self):
        Test.d=40
    @classmethod
    def m2(cls):
        cls.e=50
        Test.f=60
    @staticmethod
    def m3():
        Test.g=70

Test.h=80
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
t.m2()
print(Test.__dict__)
t.m3()
print(Test.__dict__)

