def int_to_str(num):
	res=''
	while num:
		res+=num%10
		res/=10
	return res

def str_to_int(num):
  res=0
  for i in num:
    res*=10+i
  return res

print(int_to_str(543543))
print(str_to_int('5435356'))