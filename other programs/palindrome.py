instr=input("Enter a string")
i=0
while i<len(instr):
    if not (instr[i]==instr[-i-1]):
        print('its not a palindrome')
        break
    i+=1
else:
    print('its a palindrome')
