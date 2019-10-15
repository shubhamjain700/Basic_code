#
# b=[('hello',2.3),('bavi',3.9),('shreya',3.1)]
# s=['sdfs','ewfwe']
# d=['dsf','edef']
#
# b.sort(key=lambda x:x[1])

# b=(('hello',2.3),('bavi',3.9),('shreya',3.1))
#
# b=sorted(key=lambda x:x[1])

# print(b)

# b=list(map(len,b))
# print(b)

# s=list(map(lambda x:x+'ABC',s))
# print(s)
def fund(l,k):
    x=[]
    for i in range(len(l)):
        su=0

        for j in range(i,len(l)):
            su+=l[j]
            if su<=k:
                x.append(l[j])
            else:
                break
        if sum(x)==k:
            break
        else:
            x=[]
    if len(x)>0:
        return x
    else:
        return None


l=eval(input())
k=int(input())
print(fund(l,k))

