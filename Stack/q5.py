"""Q5)

Implement a stack operation to store those names that start and ends with the same letter.

Program should stop when the user enters a word END"""

data=[]
def myPush(n):
    data.append(n)

def sten(n):
    return n[0]==n[-1]
    
    
def MyInput():
    
    while True:
        t=input("Enter Name(END to stop): ")
        if t=="END":
            break

        elif sten(t):
            myPush(t)

MyInput()
print(data)