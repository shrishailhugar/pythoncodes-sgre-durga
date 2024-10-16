class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(C,B):
    p
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())