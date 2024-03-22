# n=input("Enter the string:")
# n1=n.lower()
# D={}
# for i in n1:

#   D[i]=n1.count(i)
# print(D)

D={'Angela':'17/12/','Jennus':'12/34/21','Isha':'34/21/22'}
n=input("Enter the name:")
for i in D:
  if i==n:
    print("Birthday:",D[i])