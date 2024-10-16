input_string=input('Enter input string')
res_str=''
x=''
d=0
is_char=input_string[0].isalpha()
for char in input_string:
    if is_char:
        if char.isalpha():
            x=char
        if char.isdigit():
            res_str+=x*int(char)
    else:
        if char.isalpha():
           res_str+=char*d
        if char.isdigit():
            d=int(char)
print(sorted(res_str))
print(''.join(sorted(res_str)))
