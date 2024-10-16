input_string1=input("Enter the string:")
input_string2=input("Enter the string:")
d={}
if len(input_string1)!=len(input_string2):
    print('Both inputted string are having different length so these are not anograms')
else:
    if sorted(input_string1)==sorted(input_string2):
        print('both are anograms')

    else:
        print("both are not anograms")