"""f=open("example.txt","r")
a=f.read()
mylower=""
myupper=""
for i in a:
    if i.islower():
        mylower+=i
    if i.isupper():
        myupper+=i
print(mylower+myupper)
"""
f=open("example.txt","r")
a=f.readlines()

print(a)