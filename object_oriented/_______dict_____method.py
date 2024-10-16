#same can be achieved with vars() method.
#.__dict__ is to show all the class atrributes and methods
#here ClassName.__dict__ had no access to instance_attributes and
class DictClass():
    class_attr=10
    def __init__(self,instance_attr):
        self.instance_attr=instance_attr

    def method(self):
        print('Class attribute value is =',self.class_attr)
        print('Instacnce attribute value is=',self.instance_attr)

#with Class this __dict_ fun will yield all class attributes and methods
#{'__module__': '__main__', 'class_attr': 10, '__init__': <function DictClass.__init__ at 0x000002A36D5F8CC0>,
# 'method': <function DictClass.method at 0x000002A36D5F8E00>,
# '__dict__': <attribute '__dict__' of 'DictClass' objects>, '__weakref__': <attribute '__weakref__' of 'DictClass' objects>, '__doc__': None}
print(DictClass.__dict__)


obj1=DictClass(20)

#here it will show only instance attributes. it will not get class attributes and classs methods
print(obj1.__dict__)#{'instance_attr': 20}
