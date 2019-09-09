c=input('Enter  1 Character')
d=ord(c)

if d >= 65 and d <=90:
    print('UperCase')
elif 'a' <= c <= 'z':
    print("Lower Case")
elif d>=48 and d<=57:
    print("Number")
else :
    print("Special Character")


