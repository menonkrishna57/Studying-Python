"""Write a program to create a tuple of length 5. print the squares of each value."""
x=()
for i in range(5):
    a=int(input("Enter Number: "))
    x+=(a,)
for i in x:
    print(i**2)