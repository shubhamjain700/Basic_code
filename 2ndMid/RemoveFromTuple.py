t=(1,2,3,4,5)
item=int(input())
t=list(t)

for i in range(t.count(item)):
    t.remove(item)
t=tuple(t)
print(t)