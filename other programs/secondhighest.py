
# ns=int(input())
arr=map(int, input().split())
print(arr)

# print(type(arr))
# larr=list(arr)
# x=[]
# y=(set(larr))
# [x.append(a) for a in larr if a not in x]
# print(x)
# print(y)
# print(sorted(x))
# print(x)
# print(x[-2])
# print(sorted(list(set(arr)))[-2])
print(sorted(list(set(arr)),reverse=True)[1])
