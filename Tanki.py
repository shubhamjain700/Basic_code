t = float(input('Enter the time'))
v = (3.14*5*5*10)
result=t*10
h=10


if result > v:
    print('Overflow')
elif result==v:
    print("Full")
else:
    print('Underflow')
    ht=result/(v)
    hr=h-ht
    print(hr)


