import re

def is_password_valid(password):
    print(re.findall('[A-Z,a-z,]',password))

    if len(password)<16:
        print('the length of the password is less than 16')
        return False
    if len(re.findall('[A-z]',password))<1:
        print('there is no Upper char')
        return False
    if len(re.findall('[a-z]',password))<1:
        print('There are no lower cases')
        return False
    if len(re.findall('[0-9]',password))<1:
        print('No digit present')
        return False
    print(re.findall('[@!#%*&.,/?]',password))
    if len(re.findall('[@!#%*&.,/?]',password))<1:
        print('No specical cases found')
        return False
    return True

while not is_password_valid(input('Enter the Password:')):
    print('Bad Password please enter once again')


print('Good Password to keep')