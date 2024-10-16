input_duplicate_string=input('Enter the duplicate string')
res=[]
[res.append(x) for x in input_duplicate_string if x not in res]
print(''.join(sorted(res)))

#2nd way
res=[x for x in input_duplicate_string]
print(''.join(sorted(set((res)))))


#3rd way
print(''.join(sorted(set(input_duplicate_string))))

