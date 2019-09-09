string ="Shubham"

for j in range(2,len(string)):
 for i in range(2,j):
    if j%i==0:
       break

 else:
    print(string[j])


