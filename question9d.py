# WAP to read a file and Copy even lines of the file to a file named ‘File1’ and odd lines to another file named ‘File2’.
f=open('file.txt','r')
f1=open('file1.txt','w')
f2=open('file2.txt','w')
lines=f.readlines()
for i in range(len(lines)):
    if i%2==0:
        f2.write(lines[i])
    else:
        f1.write(lines[i])
f.close()
f1.close()
f2.close()