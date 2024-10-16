in1=input("Enter first string:")
in2=input("Enter 2nd string:")

x1={}
x1={l:in1.count(l) for l in in1 }
x2={l:in2.count(l) for l in in2}

print(x1,"\n",x2)
print(x1==x2)