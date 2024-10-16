# from differentfile import set

# 1-Built_in
# 2-global
# 3-enclosed
# 4-local

# SCOPE===== LEGB


# Built in Namespaces

x = 10  # Global


print(dir(__builtins__))


def funeclosed():
    x = 20  # enclosed

    def funlocal():
        x = 30  # local
        print(" in local x=", x)

    print("in enclosed x=", x)

    funlocal()


def funeclosed1():
    global x
    print('using global x=', x)


funeclosed()
funeclosed1()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# here set will be called from python if no local functions present else it will call local
# else here i've written same set function in another file differntfile.py from there it will execute if it's not present in local file
# YOU SHOULD IMPORT FUNCTION NOT ONLY FILE
# if that's not present in both local and imported file then it will go for inbuilt function
# def set(l):
#     print(l)
#     print("Hi it's set")
#     return l

list = [1, 3, 4, 4]
x = set(list)
print(x)