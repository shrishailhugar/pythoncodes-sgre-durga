class P:
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent classmethod')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    @classmethod
    def m2(cls):
        pass
        # super().__init__()
        # super().m1()
        super().m2()
        super().m3()
    @staticmethod
    def m3():
        # super().__init__()
        # super().m1()
        # super().m2()
        # super().m3()
        pass

class indirect(P):
    @classmethod
    def m2(cls):
        super(indirect,cls).__init__(cls)
        super(indirect,cls).m1(cls)
    @staticmethod
    def m3():
        super(indirect,indirect).m2()
        super(indirect,indirect).m3()

child_obj=C()
print('***************************')
# child_obj.m1()
C.m2()
child_obj.m3()
C.m3()
print('###########################')
indirect.m2()
indirect.m3()