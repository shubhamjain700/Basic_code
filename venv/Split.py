# h='hello world'
# data=h.split('o')
# print(data)
# e='1,2,3,4,5,6,7,8,9,0'
# data=e.split(',')
# print(data)


h=123
ls=list(str(h))

for i in range(len(ls)):
    ls[i]=int(ls[i])


print(sum(ls))