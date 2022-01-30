import cmath
a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))
c=int(input("Enter the value of C: "))
discrim=(b**2) - (4*a*c)  
print(discrim)
#-b+- sq(b^2 -4ac)
sol1=(-b+cmath.sqrt(discrim))/2*a
sol2=(-b-cmath.sqrt(discrim))/2*a
print(f"The solution for {a}x²+{b}x+{c} is {sol1} and {sol2}")      