import  numpy

a=list(map(int ,input().split()))

l=numpy.array(a)
l=l.reshape(3,3)
l.shape=(3,3)
print(l.shape)
print(l)

