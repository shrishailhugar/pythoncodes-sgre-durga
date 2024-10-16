inp=eval(input('enter list'))
val=int(input('enter val'))
while True:
    if val in inp:
        inp.remove(val)
    else:
        break

print(inp)