d = {}
print(d)
print(type(d))
d = {1: 'a', 2: 'b'}
print(d)
# l=[(10,'A'),(20,'B')]
# l=[[100,'A'],[200,'B']]
l = [[100, ['A', 'C']], [200, 'B']]
d = dict(l)
print(d)

print(d[200])
print(d[100][1])

d1 = {1: 'Bharath', 2: {'city_name':['tm', {'Tamil':'200cc'}]}}
print(d1[2]['city_name'][1]['Tamil'])

d1[3]='SGRE'
print(d1)

del d1[3]
print(d1)

d1.pop(2)
print(d1)

dd1={1:'A'}
dd2={1:'A'}
# dd2={2:'B'}
print(dd1==dd2)


d1 = {1: 'Bharath', 2: {'city_name':['tm', {'game1':3000}]}}
#default value
print(d1[2]['city_name'][1].get('game1',100))

#update
d1[2]['city_name'][1]['game1']=4000
print(d1)
print(d1[2]['city_name'][1].get('game1',100))

d1={1:'A',2:'B',3:'C'}
for item in d1.items():
    print(item)
for k,v in d1.items():
    print(k,v)
print(d1.keys())
print(d1.values())



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# print(myfamily['child1'].keys())
for k,v in myfamily.items():
    print(k,v)
    v={'name': 'Emil', 'year': 2004}
    print(v.keys())
    print(v.values())
    for k1,v1 in v.items():
        print(k1,':',v1)

#setdefault
d={1:'A',2:'B'}
# d[1]='Z'
d.setdefault(1,'Z')
print(d)