
'''stud=[]
stud=stud+[13]
stud.append('Angela Jose')
stud.extend(['Chemperi',670632,9778194255])
stud.insert(0,'MDL21CS019')
print("KTU ID:",stud[0])
print("Name:",stud[2])
print(len(stud[2])-1)
num=str(stud[5])
print(num[5::])
stud.reverse()
print(stud)
print("Index od name:",stud.index('Angela Jose'))'''



'''numbers=input("Enter numbers separated by space:")
num_str=numbers.split(" ")
a=[]
for i in num_str:
  num=int(i)
  a.append(num)
prime=[]
comp=[]
for i in a:
  count=0
  for j in range(1,i+1):
    if(i%j==0):
      count+=1
    
  if(count==2):
    prime.append(i)
  else:
    comp.append(i)
  
print("prime:",prime)
print("Composite:",comp)'''


# name=list(input("Enter names separated by comma:").split(","))
# name.sort()
# print(name)
# longest=max(name,key=len)
# print(longest)

# for i in name:
#   if(i[0]=='A'):
#     print(i)

# upper=[]
# for i in name:
#   capital=i.upper()
#   upper.append(capital)
# print(upper[::-1])

# print(sorted(name,key=len))
'''marks=[]
mark=input("Enter mark:").split(",")
for i in mark:
  num=int(i)
  marks.append(num)
print("Mean:",sum(marks)/len(marks))'''
import random
import math
mark=[]
for _ in range(25):
  mark.append(random.randint(1,100))
print(mark)
print("Mean:",sum(mark)/len(mark))

mark.sort()
mid=len(mark)//2
print("Median:",mark[mid])

#mode
mode=[]
max_count=0
for i in range(len(mark)):
  count=0
  for j in range(len(mark)):
    if(mark[i]==mark[j]):
      count+=1
  if (count>max_count):
    max_count=count
    mode=[mark[i]]
  elif(count==max_count and mark[i] not in mode):
    mode.append(mark[i])
print(mode)

#std deviation
summ=0
mean=sum(mark)/len(mark)
for i in range (len(mark)):
  num=(mark[i]-mean)**2
  summ+=num
print("Standard deviation:",math.sqrt(summ/mean))

print("Range:",max(mark)-min(mark))

mark_sort=sorted(mark)
q1 = mark_sort[int(0.25 * len(mark))]
q3 = mark_sort[int(0.75 * len(mark))]
iqr = q3 - q1
print("Inter quartile range = ", iqr)
