import random
"""a=random.randint(0,1)
if a==1:
  print("Head")
else:
  print("Tail")"""

l=[]
names=input("Enter the names:")
l=names.split(" ")
num=random.randint(0,len(l)-1)
name=l[num]
print(f"{name} will pay the bill")
