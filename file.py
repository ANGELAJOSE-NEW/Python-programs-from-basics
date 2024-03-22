#f1=open("file1.txt","x")# 'x' is used to create a file. You cannot again create a file of same name or you cannot run twice
# f1=open("file1.txt","r")
# data=f1.read()
# print(data) # by default  a file is opened in read mode

#write can also create a file if it does not exist. If file already exist content will be erased
# f1=open("file1.txt","w")
# f1.write("Hi")
#print(f1.read()) will give error if file is opened in w mode

# r+ will give error if file doesnt exist
f1=open("file1.txt","r+")
print(f1.read())
f1.write("All")