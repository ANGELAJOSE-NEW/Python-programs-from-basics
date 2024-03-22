a=int(input("Enter 1st side:"))
b=int(input("Enter 2nd side:"))
c=int(input("Enter 3rd side:"))

list1=[a,b,c]
list1.sort()

if list1[2]**2==list1[0]**2+list1[1]**2:
  print("Right angled triangle")
else:
  print("Not")