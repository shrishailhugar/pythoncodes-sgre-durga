from itertools import product,combinations,permutations,combinations_with_replacement
# print(list(product([1,2,3],repeat=10)))
# print(list(combinations([1,2,3]),2))
print(list(permutations([1,2,3],3)))
print(list(combinations([1,2,3],3)))
print(list(combinations_with_replacement([1,2,3],3)))
print(list(product([1,2,3],repeat=3)))

l1=list(map(int,input().split()))
print(l1)