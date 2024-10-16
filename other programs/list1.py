l1=['a',1,12.2,True,'Bharath','jai']
# print(l1)
# print(l1)
# print(l1[0])
# print(l1[1])
# print(l1[-1])
#slice
# print(l1[0:1])
# print(l1[0:100])
# print(l1[0:5:2])
# print(l1[::-1])
# print(l1[5:-5:-1])
# print(l1[0:0])

# #append
# list1=[]
# list1.append(2)
# list1.append('bharath')
# list2=[['A','B'],'C']
# list1.append(list2)
# print(list1)
# print(list1[2][0][0])
# #multidimensional list
# z=[2, 'bharath', [['A', 'B'], 'C']]#z[2]
# x=[['A', 'B'], 'C']#x[0]
# y=['A', 'B'] #y[0]
# print(z[2][0][1])

#insert
# lins=[]
# lins.insert(0,1)
# lins.insert(0,2)
# lins.insert(0,3)
# lins.insert(0,4)
# print(lins)
# lins.insert(4,10)
# lins.insert(4,20)
# print(lins)
# lins.insert(100,50)
# lins.insert(-100,60)
# print(lins)
# lins2=['hi','BGMS']
# lins.insert(len(lins),lins2)
# print(lins)

#extend
lext1=[1,2,3]
lext2=[4,5,6]
lext1.extend(lext2)
print(lext1)
lext2.extend(lext1)
print(lext2)
print(sum(list(range(0,50))))
