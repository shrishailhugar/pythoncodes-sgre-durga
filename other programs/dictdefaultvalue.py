dict1={'a':"shreee",'b':"Bapu"}

#here  if the key present it' going to get that value else it will print default value
print(dict1.get('a','sh'))
print(dict1)

#settig default
dict1.setdefault('c',"Manu")
print(dict1)