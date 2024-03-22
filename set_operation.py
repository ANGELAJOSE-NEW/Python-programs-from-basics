set1={"Angel","Anu","Geethu"}
set2={"Jennus","Aleena","Angela","Anu"}
print(set1.union(set2))#function invoked on set1 , argument set2
print(set1|set2)
set3={"Jathu","Aleena"}
print(set1|set2|set3)
print(set1.union(set2,set3))
print(set1.union(("Alli",)))#initially tuple gets converted to set and then perform union
#set1.update(set2)
print(set1)
print(set1.intersection(set2))
print(set1 & set2)
#set1.intersection_update(set2)
#print(set1)
print(set1.difference(set2)) 
print(set1-set2)
print(set2.difference(set1,set3))
#set1.difference_update(set2)
print(set1.symmetric_difference(set2))
print(set1.isdisjoint(set2))
set4={"Angel","Anu"}
print(set4.issubset(set1))
print(set4<=set1)
print(set1.issuperset(set4))
print(set1>=set4)
print(set1>=set1)