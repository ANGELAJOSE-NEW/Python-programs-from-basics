for i in range(101,1000):
  n=i
  sum=0
  while n>=1:
    dig=n%10
    sum+=dig
    n=n//10
  if sum%9==0:
    print(i)