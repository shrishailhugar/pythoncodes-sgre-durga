dict={'Name':'Bapu','age':15,'place':'Savanahalli','class':10}

class Student():
    '''To add student calss'''

stud_obj=Student()
for k,v in dict.items():
    setattr(stud_obj,k,v)

print(vars(stud_obj))