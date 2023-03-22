f = open("name.txt","w")
for i in range(5):
   n = input("Enter name: ")
   f.write(n+" ")
f.close()