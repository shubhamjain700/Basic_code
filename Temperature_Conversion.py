t=float(input("Enter the temp"))
f=int(input("Enter 1 to convert celcius to farenhiet or press 2 to convert farenheit celcius"))

if f==1:
    print(t*1.8 +32)
elif f==2:
    print(((t-32)*5)/9)