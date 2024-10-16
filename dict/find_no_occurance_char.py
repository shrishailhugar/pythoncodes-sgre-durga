
inp=input('Enter String:')
print(inp)
d={}
ov=['a','e','i','o','u']
for char in inp:
    if char in ov:
        d[char]=d.get(char,0)+1
print(sorted(d.items()))
d={2:'w',1:'x',3:'s'}
print(sorted(d))
print(sorted(d.items()))