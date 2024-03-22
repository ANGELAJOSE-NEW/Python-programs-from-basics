name="Angela"
for i in name:
    print(i)

names=["ALli",'asha','unni']
for j in names:
    print(j)

list2=[]
list1=[1,2,3,4,5]
for k in list1:
    list2.append(k*k)
print(list2)

list2=[3,7,5,4]
for i in list2:
    print(i)
else:
    print("Successfully completed")

for i in list2:
    print(i)
    if i==3:
        break
else:
    print("Successfully completed")

tuple1=(2,5,3,34)

for i in tuple1:
    if(i%6==0):
        print(i)
        break
else:
    print("No number divisible by 6")