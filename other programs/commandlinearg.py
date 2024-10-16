from sys import argv

print(argv,(type(argv[0])))
x=list(map(int,argv[1:]))
print(sum(x))