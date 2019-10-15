import  numpy
n,m=map(int,input().split())
a=list(map(int ,input().split()))
b=list(map(int ,input().split()))
a=numpy.array(a)
b=numpy.array(b)
a=a.reshape(n,m)
b=b.reshape(n,m)


print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.power(a,b))