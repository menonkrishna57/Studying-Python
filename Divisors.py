Number=int(input("Enter the number:"))
divisors=[]
for i in range(1,Number+1):
    if Number%i==0:
        divisors.append(i)

print(divisors)