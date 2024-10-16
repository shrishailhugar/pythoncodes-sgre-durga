input_string=input("Enter input string:")
count=0
prev_count=0
input_string=''.join(sorted(input_string))
res_string=''
while count<len(input_string):
    count+=input_string.count(input_string[count])
    res_string+=str(count-prev_count)+input_string[count-1]
    prev_count=count
print(res_string)

#2nd way
list_of_unique=list(sorted(set(input_string)))
for char in list_of_unique:
    print(f'{char} present {input_string.count(char)} times')