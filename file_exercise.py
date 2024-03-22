# f1=open("file1.txt",'r')
# s=f1.read()
# s.replace("\n"," ")
# D={}
# ns=s.lower()
# for i in ns:
#   D[i]=ns.count(i)
# print(D)

#  Write a code segment that opens a file for input and prints the number of four letter words in the file
f1=open("file1.txt",'r')
s=f1.read()
ns=s.lower()
ns=ns.replace('\n',' ')
list=ns.split(" ")
print(list)
count=0
for i in list:
  if(len(i)==4):
    count+=1

print(count)
s='ANgela'
print(s.replace('a','x'))
print(s)