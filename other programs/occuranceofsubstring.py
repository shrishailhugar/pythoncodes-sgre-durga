s='ABBBBABABBBAddABB'
ss='BB'
ind=0
lind=[]
for i in range(s.count(ss)):
    lind.append(s.find(ss,ind,len(s)))
    ind+=len(ss)
print(lind)

i=s.find(ss)
if i==-1:
    print("No match of substring found")
# else:
while i!=-1:
    print(i)
    i=s.find(ss,i+1,len(s))


