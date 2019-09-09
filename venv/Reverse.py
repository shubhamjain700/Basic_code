# t=input()
#
# t =t[::-1]
# print((t))


# n=list(input())
# t=input()
# k=input()
#
# for i in range(0, len(n)):
#     if n[i]==t:
#         n[i]=k
#
# for i in n:
#     print(i,end="")


for i in range (5):
    if i%2==0:
        print("12345")
    else :
        print(54321)
# for i in range (5):
#     print("ABCDE")
for i in range(5):
    for j in range(5):
        print(chr(65+j),end="")
    print("\n")
n=eval(input("Enter the number"))
for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")
for k in range(n-1,0,-1):
    for j in range(1,k+1):
        print(j,end=" ")
    print("")


