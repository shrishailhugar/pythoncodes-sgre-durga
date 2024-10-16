no_st=int(input('Enter no of students:'))
st_d={}
for i in range(no_st):
    Name=input('Enter Name:')
    Marks=int(input('Enter Marks'))
    st_d[Name]=Marks
print(st_d)
st_name=input('Enter the name of the student:')
print(st_d.get(st_name,'Student not found'))