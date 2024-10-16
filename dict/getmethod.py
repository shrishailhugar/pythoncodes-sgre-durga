d={1:'A',2:'B'}

print(d.popitem())
print(d.pop(1))
print(d)
d={1:'A',3:'C'}
d[2]='B'
print(d)
print(d.popitem())
print(d)