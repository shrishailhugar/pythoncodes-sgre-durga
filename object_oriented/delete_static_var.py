class Test:
    a=10
    def __init__(self):
        del Test.a
        Test.b=20
        Test.c=30
    @classmethod
    def m1(cls):
        del cls.b
        del Test.c
        Test.d=40
    @staticmethod
    def m2():
        del Test.d
        Test.e=50
print(Test.__dict__)
Test.m1()
print(Test.__dict__)
#
# print(Test.__dict__)
# t=Test()
# print(Test.__dict__)