name_1=input("Enter first name:")
name_2=input("Enter second name:")
name1=name_1.lower()
name2=name_2.lower()
name=name1+name2

num1=name.count('t')+name.count('r')+name.count('u')+name.count('e')
num2=name.count('l')+name.count('o')+name.count('v')+name.count('e')
print(str(num1)+str(num2))

