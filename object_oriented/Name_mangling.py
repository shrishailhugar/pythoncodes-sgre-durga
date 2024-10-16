class ManglingClass():

    def __init__(self,value):
        self.__value=value
    def __method1(self):
        return 'The value is='+str(self.__value)

object=ManglingClass(10)
print(vars(object))#{'_ManglingClass__value': 10}
#print(object.__value)  -- AttributeError
#print(object.__method1())--AttributeError
#In above case you see errors while fetching the values but in reality it's not because of private
#it's actually bcz of NameMangling
print(vars(ManglingClass))
#{'__module__': '__main__', '__init__': <function ManglingClass.__init__ at 0x0000017697CD8CC0>,
# '_ManglingClass__method1': <function ManglingClass.__method1 at 0x0000017697CD8E00>,
# '__dict__': <attribute '__dict__' of 'ManglingClass' objects>, '
# __weakref__': <attribute '__weakref__' of 'ManglingClass' objects>, '__doc__': None}

#  --- here you can see in line 8 the __value name renamed by python into _ManglingClass__value here the
#here it's prefixed it by _class name by python
# --- here you can see line 15 the __method is renamed by python into _ManglingClass__method1.
#still we can access these using mangled_names
print(object._ManglingClass__value)#10
print(object._ManglingClass__method1())#The value is 10