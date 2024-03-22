count=1
while count<=5:
  print(count)
  if count==3:
    break
  count+=1
  print("Hi")


list1=["Alli","Asha","Unni"]
list2=["Jennus","Geethu","Prince"]
for i in list1:
  for k in list2:
    print(i,k)
    if i=="Alli" and k=="Geethu":
      break
  print("Out from inner loop")
  