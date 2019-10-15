import random
re=random.random()
print(re)

l=[1,2,3,4,5,6]
random.shuffle(l)
print(l)

re=random.randrange(1000,9999,10)
print(re)

re=random.randint(1000,9999)
print(re)


l=['dr','ewfdew']
re=random.choice(l)
print(re)

l=[1,2,3,4]
re=random.choices(l,k=30,weights=[1,1,1,5])
print(re)

l=[1,2,3,4]
re=random.sample(l,k=3)
print(re)
