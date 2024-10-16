from copy import copy,deepcopy


#in python (= assign ) operator will not copy the object instead it creates binding between existing  object and targeted variable name
#Here both the var names lista and listb referring same object so changes to the object will reflect to both the vars
lista=[1,2,3,4]
listb=lista
print(id(lista),"   ",id(listb))
listb.append(5)
print(lista,"id=",id(lista),"\nHere both the var names lista and listb referring same object\n",listb,"id=",id(listb))



#___________________________________SHALLOW COPY_________________________________________________#


xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9],20]
ys = list(xs)  # Make a shallow copy
# ys=copy(xs) the above and this are same

print(xs,'id=',id(xs),"Before        ",ys,'id=',id(xs))
xs[1][0]=5
print(xs,"id=",id(xs),"\nafter altering pointed object element the changes we can see in both list \n",ys,"id=",id(ys))
print(id(xs[1]),"\nid of child object we can see both parent elements id's differs but there child objects referring to same object\n",id(ys[1]))


#__________________________________________BUT1__
       #@adding new pointer will not reflect in both the lists as it's addition of new object

xs.append(10)
ys.append(12)
print(xs,'id=',id(xs),"\nafter adding new pointer to each that will not relflect bcz we are adding new pointer(object) after copy \n",ys,'id=',id(ys))


#___________________________________________BUT2__
    #@Assignment after assignment the
print(f"BEFORE assingment child object id's of\n xs[3]={id(xs[3])} and \nys[3]={id(ys[3])} are")
xs[3]='x'
ys[3]='y'
print(f"After assingment child object id's of \nxs[3]={id(xs[3])} and \nys[3]={id(ys[3])} are")
print(xs,"\nAfter reassignment the pointer the complete child object is changing not object element\n",ys)


#_____________________________________________________________DEEP_COPY________________________________________________________
zs=deepcopy(xs)
print(xs,"id=",id(xs),zs,id(zs))
xs[1][0]='z'
print(xs,"\nafter altering object elements also this will not afftct copied object as it's having it's own reference object\n",zs)