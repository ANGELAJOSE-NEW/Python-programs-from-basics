list1=[]
n=int(input("Enter the number:"))
i=1
while i<=n:
  if n%i==0:
    list1.append(i)
  i+=1
print(list1)
