n=int(input("No of terms:"))
a=0
b=1
print(a,b,end=' ')

while a<n-2:
  c=a+b
  print(c,end=' ')
 
  a=b
  b=c
  
