"""Q6)
Input a sentence and reverse it using STACK"""
a=[]
def mypush(n):
    a.append(n)
    
    
def display():
    for x in a[::-1]:
        print(x,end='')
        
        
s=input("Enter a sentence ")
for x in s:
    mypush(x)
display()