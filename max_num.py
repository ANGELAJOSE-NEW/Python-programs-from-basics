n=input("Enter elements of the list separated by space:")
list1=n.split(" ")
large=0

# for i in list1:
#   num=int(i)
#   if num>large:
#     large=num

#print(large)

print(max(list1))

# for i in range(0,len(list1)):
#   num=int(list1[i])
#   if num>large:
#     large=num
# print(large)

list1.sort()
print(list1[len(list1)-1])