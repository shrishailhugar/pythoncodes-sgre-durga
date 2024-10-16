s1={1,2,3,4}
s2={3,4,5,6}
s3=s1.union(s2)
print(s1)
print(s2)
print(s3)
s3=s1|s2
print(s3)
s4=s1.intersection(s2)
print(s4)
s4=s1&s2
print(s4)
s5=s1.difference(s2)
print(s5)
s5=s2.difference(s1)
print(s5)
s5=s1-s2
print(s5)

s6=s1.symmetric_difference(s2)
print(s6)
s6=s2.symmetric_difference(s1)
print(s6)
s6=s1^s2
print(s6)

list1=[1,1,2,2,3]
list2=[]
for i in list1:
    if i not in list2:
        print(f'element {i} not present adding')
        list2.append(i)
        print(list2)
    else:
        print(f'element {i} already exist')
print(list2)
s1=set(list1)
print(s1)

l1=[1,2,3]
s1={i*i for i in l1}
print(s1)
