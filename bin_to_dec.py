n=input("Enter binary number:")
d,f=n.split('.')
k=(len(d))-1

sum=0
for i in d:
  sum+=(int(i)*(2**k))
  k-=1
#print(sum)
fraction=0
j=-1
for i in f:
  fraction+=int(i)*(2**j)
  j=j-1
dec=sum+fraction
print(dec)
 
