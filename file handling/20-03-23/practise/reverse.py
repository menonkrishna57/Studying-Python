import pickle as p

file_obj=open("example.bin","rb")
file_contents=[]
try:
    while True:
        file_contents.append(p.load(file_obj))
except:
    file_obj.close()

for i in range(len(file_contents)):
    if i%2==0:
        print(file_contents[::-1][i][::-1])
    if i%2!=0:
        print(file_contents[::-1][i])