# WAP to read a file and Print the total number of characters, words and lines in the file.
f=open('file.txt','r')
data=f.read()
characters=0
words=len(data.split())
lines=len(data.split('\n'))
for i in data.split('\n'):
    characters+=len(i)
print(f"characters : {characters}, Words : {words}, Lines : {lines}")
f.close()

