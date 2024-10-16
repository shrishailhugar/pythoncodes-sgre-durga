l1=[10,20,30]
l2=[30,40,60]
l=[x for x in l1 if x not in l2]
print(l)
l=[x for x in l1 if x in l2]
print(l)
l1=['shree','bapu','guru','andy']
l=[x[0] for x in l1]
print(l)
string='the qUick brown fox jums Over the lAzy doga'
l1=string.split()
l=[[x.upper(),len(x)] for x in l1]
print(l)

vow=['a','e','i','o','u','A','E','I','O','U']
# l=[]
# [l.append(x) for x in string if x in vow if x not in l]
l=[x for x in vow if x in string]
print(l)