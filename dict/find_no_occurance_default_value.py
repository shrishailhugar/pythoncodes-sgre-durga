#dict.get() will return value if key presnet else returns None
#if we want it to return some default value

d={}
d['a']=100
d['b']=200

print(d.get('a',0),d.get('c',0),d.get('d'),sep='  ')

input_string=input('Enter the string:')
vowels=['a','e','i','o','u']
li=[x for x in input_string if x in vowels]
input_string=''.join(li)
d={}
for char in sorted(input_string):
    d[char]=d.get(char,0)+1
print((d.items()))

import inspect
def aa():
    print(inspect.stack()[1][3])
aa()