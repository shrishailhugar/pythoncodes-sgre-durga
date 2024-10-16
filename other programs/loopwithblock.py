l=eval(input())

for i in l:
    if i>500:
        print('the item can"t be processed as the item needs insurence')
        break
    print('item =%.2f  processed'%i)
else:
    print('all item proceesed successfully')