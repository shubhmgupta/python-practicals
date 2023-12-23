# WAP to read a file and Print the words in reverse order.
f=open('file.txt','r')
data=f.read()
words=data.split()
for i in words:
    print(f"{i} => {i[-1::-1]}")