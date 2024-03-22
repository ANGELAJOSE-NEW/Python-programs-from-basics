
n=input("Number of heights separated by space:")
sum=count=0
list1=n.split(" ")
print(list1)
for i in list1:#dont think i=0 etc i gets equated to content of list
  sum+=int(i)
  count+=1
print(round(sum/count))
