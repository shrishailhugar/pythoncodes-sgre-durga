str = '2+35-*4/35+-10*-2+6-*2'
opertions = ['+', '-', '/', '*']
# list1=[x for i,x in enumerate(str) if  ]
# # evallist=[x for x in list1 if list1.in]
list1 = []
for i, x in enumerate(str):
    print(i,x)
    if (i == 0):
        list1.append(x)
    else:
        if x in opertions and str[i - 1] in opertions:
            pass

        else:
            list1.append(x)

print(list1)