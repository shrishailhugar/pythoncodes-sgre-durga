s='Hi Bapu hello Guru'
def rev(sub_s):
 return sub_s[::-1]
print(list(map(rev,s.split()[::2])))

l1=list(s)
a='123'
print(list(a))
print(l1)
print(l1.count('l'))
print(l1.index('l',11,13))
t1=tuple(l1)
itr=tuple(reversed(t1))
print(itr)
ll=sorted(itr)
print(ll)
l1=[1,2,3]

l2=[3,4,5]
set1={1,2,3}
set1.discard(3)
print(set1)
a={(1,2),(3,4)}
d=dict(a)
print(d)
d1={1:'A',2:'B'}
d1.setdefault(1,'K')
print('d1=',d1)
d2={3:'C',4:'D'}
d3={5:'C',1:'Z'}
d1.update(d2)
d.items()
print(d1)
d1.update(d3)
print(d1)

s='abcdabcd123'
d={}
for char in s:
    d[char]=d.get(char,0)+1
print(d)
print('*****************')
class A:
    x=10
    def __init__(self):
        type(self).v=30
        # print(type(self))
        print(A.x)
        A.y=20
        print(A.y)
obj=A()
print(obj.__dict__)
print(A.__dict__)
