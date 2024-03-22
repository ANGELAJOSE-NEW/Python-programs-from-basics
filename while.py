# count=0
# while count<4:
#   print(count)
#   count+=1
# else:
#   print("Else is executed because condition became false when count=5")

# count1=1
# while count1<=5:
#   print(count1)
#   count1+=1
#   if count1==3:
#     break
# else:
#   print("Else will not be executed as it was after break")

# count=1
# while count<1:
#   print(count)
#   count+=1
# else:
#   print("Else is executed because condition became false when count=5")


# number=int(input("Enter the number:"))
# while number!=-1:
#   print(number)
#   number=int(input("Input -1 to quit:"))

#calculate sum until the user enters zero
sum=0
num=int(input("Enter number"))
while(num!=0):
  sum+=num
  num=int(input("Enter number"))
print(sum)
