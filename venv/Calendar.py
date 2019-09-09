s=int(input())


if s<1 or s>31:
    exit(0)

s=s%7

if s==1:
    print("Monday")
elif s==2:
    print("Tuesday")
elif s==3:
    print("Wednesday")
elif s==4:
    print("Thrusday")
elif s==5:
    print("Friday")
elif s==5:
    print("Saturday")
else:
    print("Sunday")