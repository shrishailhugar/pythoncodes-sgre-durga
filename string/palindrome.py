input_string=input('Enter the input String:')
reverse_string=input_string[::-1]
if input_string==reverse_string:
    print('both strings are palindrome')
else:
    print('Not a palindrome')
reverse_string=reversed(input_string)
reverse_string=''.join(reverse_string)
if input_string==reverse_string:
    print('both are palindrome')
else:
    print('Not a Palindrome')