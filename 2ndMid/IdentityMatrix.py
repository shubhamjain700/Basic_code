import  numpy
n,p=map(int,input().split())
#
# s=numpy.identity(n,dtype=int)
s=numpy.eye(n,p,dtype=float)
print(s)
