import numpy as np
# h=[1,2,3,4,5,6]
# re=np.array(h)
# print(re.shape)
# re=re.reshape(3,2)
# s=re.shape
# print(s)
# print(re,type(re))

a=np.array([[2,3,4],[4,5,6]])

b=np.array([[5,3,4],[4,5,6]])
re=a**b
re1=np.add(a,b)
re1=np.divide(a,b)
print(re,end='\n\n')
# a.flags.writeable=False
a[0][0]=1
a.shape=(3,2)
a=a.reshape(6,1)
print(a)

arr=np.linspace(0,5,10)
print(arr)