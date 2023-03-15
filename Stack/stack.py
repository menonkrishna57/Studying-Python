
a=[]


def myPush(n):
    a.append()
    
def myPop():
    if len(a)==0:
        print("Stack is Empty")
    else:
        print("Number poped is ",a.pop())
        
def myPeak():
    if len(a)==0:
        print("Stack is Empty")
    else:
        print("peak element is ",a[-1])
        
def myCount():
    print("Count= ",len(a))

data=[5,10,15,20,25,30,35,40,45,50]
for x in data:
    if x%2==1:
        myPush(x)