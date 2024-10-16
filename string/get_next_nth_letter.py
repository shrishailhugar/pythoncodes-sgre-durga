input_string=input('Enter the string:')
prev_letter=''
print(ord('a'),type(ord('a')))
for letter in input_string:
    print(letter if letter.isalpha() else '',end='')
    print(chr(ord(prev_letter)+int(letter)) if letter.isdigit() else '',end='')
    prev_letter=letter if letter.isalpha() else ''