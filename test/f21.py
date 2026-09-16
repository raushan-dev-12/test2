p=open("abc.txt")
data=p.read()
p.close()


f=open("abc.txt",mode="w")
f.write(data)
f.write("\n")
f.seek(0)
f.write("R1234567890")
f.write(data[4:9])
pos=data.find("\n")
f.close()


xyz=open("xyz.txt","a")
xyz.write("Hi this is  another trial program file.\n")
xyz.write(data[0:pos])
xyz.write("Hey this is 3rd line.\n")
xyz.write(data[pos+1:])
