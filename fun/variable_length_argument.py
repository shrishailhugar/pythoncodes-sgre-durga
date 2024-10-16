def sum1(*n):
    sumx=0
    print(type(n))
    for i in n:
        sumx+=i
    print(sumx)
sum1()
sum1(10)
sum1(10,30)
sum1(10343,3435,45)


def fun1(*n):
    print(type(n))
    print(n)

fun1((10,20),(30,40))
fun1([12,12],[89,99])
fun1({11,11},{1})
fun1({1:3,5:7},{2:3,6:5})
fun1([11,23,44],(12,5))
fun1([11,23,44],{12,5})

