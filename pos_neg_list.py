n=input("Enter elements sep by ,")
list=n.split(",")
list1=[]
list2=[]
for i in list:
  if int(i)<0:
    list1.append(i)
  else:
    list2.append(i)
print(list1)
print(list2)
