import cmath
eq=input("Enter your equation(in format 'ax2 + bx + c = 0'):")
eq=eq.strip()
x=0
for x in range(len(eq)):
    if(eq[x]=='x'):
        