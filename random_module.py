import random
#a=random.randint(1,3)
a=random.randrange(1,3)
b=random.random()
c=random.uniform(1,3)
#print(c)
l=[1,7,34,78,90]
d=random.choice(l)
print(d)
random.shuffle(l)
print(l)