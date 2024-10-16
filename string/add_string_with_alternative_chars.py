
input_str1=input('Enter the input')
input_str2=input('Enter the input')
input_str3=input('Enter the input')

for length in range(max(len(input_str1),len(input_str2),len(input_str3))):
    if length<len(input_str1):
        print(input_str1[length],end='')
    if length<len(input_str2):
        print(input_str2[length],end='')
    if length<len(input_str3):
        print(input_str3[length],end='')

