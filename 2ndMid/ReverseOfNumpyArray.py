import  numpy

n=list(map(int,input().split()))
#
# k=numpy.array(n,dtype=float)
# print(numpy.flipud(k))

n.reverse()
a=numpy.array(n,dtype=float)
print(a)
