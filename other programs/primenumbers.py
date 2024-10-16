l1=[]
ss=list(range(2,2))
print(ss)
print(range(2,2))
def get_prime_nos(n):
    i=3
    if n>=2:
        while n>i:
            for j in range(2,(i//2)+1,1):
                if i%j == 0:
                    break
            else:
                l1.append(i)
            i+=1
def get_prime_no_list(n):
    l1.append(2)
    k=3
    while(len(l1)<=n-1):
        for j in range(2,(k//2)+1):
            print(j,k)
            if k%j==0:
                break
        else:
            l1.append(k)
        k+=1

def is_prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            print('the number is not prime')
            return True
    else:
        print(f'the {n} number is prime')
        return False
# get_prime_nos(55)
# get_prime_no_list(10)
print(is_prime(35))
print(l1)

l=[x for x in range(2,100) if is_prime(x) ]
print(l)