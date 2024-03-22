for i in range(0,100):
  if i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  if i%3==0 and i%5==0:#if you put elif this condition will not be checked if any of the above if condition is satisfied
    print("FizzBuzz")
  else:
    print(i)