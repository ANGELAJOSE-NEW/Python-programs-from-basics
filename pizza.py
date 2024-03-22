size=input("Enter the size of pizza:a)small b)medium c)large")
bill=0
if size=="small":
  bill+=100
  pepper=input("Need pepperoni Y/N")
  if pepper=="Y":
    bill+=30
if size=="medium":
  bill+=200
  pepper=input("Need pepperoni Y/N")
  if pepper=="Y":
    bill+=50
if size=="large":
  bill+=300
  pepper=input("Need pepperoni Y/N")
  if pepper=="Y":
    bill+=50
cheese=input("Enter cheese Y/N")
if cheese=="Y":
  bill+=20

print(f"Bill for {size} pizza is {bill}")