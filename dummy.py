
try:
    f1=open("text1.txt")
    data1=f1.read()
    f=open("C:\\Users\\Raushan\\OneDrive\\Desktop\\training\\.vscode\\text2.txt")
    data2= f.read()
    

except FileNotFoundError:
    print("File NOT FOUND.")

except:
    print("Something went wrong.")

print(data1,data2)