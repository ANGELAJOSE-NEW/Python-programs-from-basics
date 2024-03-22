n=input("Enter the string:")
list1=n.split(" ")

for i in list1:
  if i[::-1]==i:
    print(f"{i} is pallindrome")