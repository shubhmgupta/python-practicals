# WAP to read a file and Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count.
f=open('file.txt','r')
data=f.read()
dict={i:0 for i in data}
del dict['\n']
for i in data.split('\n'):
    for j in i:
        dict[j]+=1
print(dict)
