def dim(M):
    return  len(M),len(M[-1])

m1=eval(input())
m2=eval(input())
r1,c1=dim(m1)
r2,c2=dim(m2)
res=eval(str([[0]*c1]*r1))
if(r1,c1)==(r2,c2):
    for i in range(r1):
        for j in range(c1):
            res[i][j]=m1[i][j] +m2[i][j]

    print('First Matrix')
    for i in m1:
        print(*i)

    print('Second Matrix')
    for i in m2:
        print(*i)

    print('Addition Matrix')
    for i in res:
        print(*i)
else  :
    print('Not valid')