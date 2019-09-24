def matrixvalidayion(m):
    for i in range(len(m)):
        if(len(m[i])!=len(m[i+1]) and type(m[i])!=list and type(m[i+1])!=list):
            return  False
        else:
            return  True

m=[[1,2,3,4,5],[3,4,5,6,70]]
k=matrixvalidayion(m)
print(k)