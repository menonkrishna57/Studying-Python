from operator import truediv


number=int(input("Enter Number:"))
prime=0
primecheck=False
if number>0:
        for i in range(1,number+1):
            if number%i==0:
                prime+=1

if prime==2:
    primecheck=True
print(primecheck)