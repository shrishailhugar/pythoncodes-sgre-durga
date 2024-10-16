input_string=input()
#sorted will not change the input_string and it will return list,and here it's sorts based on ASCII codes
#so 0(49)...9(57)    then A(65),B....Z(90),   a(97),b,......z(122)
sorted_input_list=sorted(input_string)
start_index_of_string=0
for char in sorted_input_list:
    if char.isalpha():
        break
    start_index_of_string+=1
#here + operator merge 2 list no content of arguments changes
res_string=''.join(sorted_input_list[start_index_of_string:]+sorted_input_list[:start_index_of_string])
print(res_string)