l=[[1,1,1],[1,1,1],[1,1,1]]
pos=input("Enter the position in format row,column:")
l1=pos.split(",")
a=int(l1[0])
b=int(l1[1])
l[a-1][b-1]='x'
print(l)