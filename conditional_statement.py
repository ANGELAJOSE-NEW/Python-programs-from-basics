# age=int(input("Enter age:"))
# if age!=18:
#   print("CAn vote")
# else:
#   print("Cant vote")

"""num=int(input("Enter number:"))
if num%2==0:
  print(f"{num} is even")
else:
  print(f"{num} is odd")"""

#nested if
height=int(input("Enter height in feet:"))
if height>3:
  print("You can ride")
  age=int(input("Enter age:"))
  if age<+18:
    print("Pay 250")
  elif age<=12:
    print("Pay 120")
  else:
    print("Pay 500")
else:
  print("Cannot ride")
print("Bye")


