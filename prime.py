# n=int(input("Enter number:"))
# prime=True
# i=2
# while i<=n//2:
#   if(n%i==0):
#     prime=False
#     break
#   i+=1
# if prime==True:
#   print('prime')
# else:
#   print("Not prime")


#print prime number less than 100

for n in range(100):
  prime=True
  i=2
  while i<=n//2:
    if n%i==0:
      prime=False
      break
    else:
      i+=1
  if (prime==True):
    print(f"{n} is prime")
  else:
    print(f"{n} not prime")