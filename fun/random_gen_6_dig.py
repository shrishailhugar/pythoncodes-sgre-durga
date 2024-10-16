from  random import randint,randrange,choice
# for i in range(10):
#     for i in range(2):
#         print(randint(0,9),end='')
#         print(randrange(0,10,1),end='')
#         print(choice(range(0,10)),end='')
#     print()

chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(100):
    for i in range(3):
        print(choice(range(0,9)),end='')
        # x=randint(65,90)
        # y=randint(97,120)
        # l=[x,y]
        print(chr(choice([randint(65,90),randint(97,120)])),end='')
    print()
