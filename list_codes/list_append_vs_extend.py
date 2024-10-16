l1=[1,2,3]
l1.append('ABC')
print(l1)# [1,2,3,'ABC']
l1=[1,2,3]
l1.extend('ABC')
print(l1)#[1,2,3,'A','B','C']
#here it will treat it as a sequence and add each element
l1.extend(['CDF'])
print(l1)
l1.append([30,40])

print(l1)
