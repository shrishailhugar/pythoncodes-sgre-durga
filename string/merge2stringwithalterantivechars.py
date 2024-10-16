import time

s1='Sandeep'
s2='Sathwik'
st=time.time()
s=''
for i in range(min(len(s1),len(s2))+1):
    print('i=',i)
    if i==min(len(s1),len(s2)):
        print('II=',i)
        if len(s1)>len(s2):
            s+=s1[i:]
        elif len(s2)>len(s1):
            s+=s2[i:]
        break
    s+=s1[i]+s2[i]
print(s)
print(f'time taken {time.time()-st:.10f}')

st=time.time()
ress=''
i,j=0,0
while i<len(s1) or j<len(s2):
    if i < len(s1):
        ress+=s1[i]
    if j< len(s2):
        ress+=s2[i]
    i+=1
    j+=1
print(ress)
print(f'time taken= {time.time()-st:.10f}')
st=time.time()
i,j=0,0
s=''
while i<len(s1) and j<len(s2):
    s+=s1[i]+s2[i]
    i+=1
    j+=1
if len(s1)>len(s2):
    s+=s1[i:]
else:
    s+=s2[i:]
print(s)
print(f'time taken={time.time()-st:.10f}')