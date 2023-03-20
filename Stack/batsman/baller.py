"""create 2 list called batsman and ballers 
define a push function to input name/type of player as a sting separated by slash 
define another function to print both the list"""

batsman=[]
baller=[]

def mypush():
    
    b=input("Enter details: ")
    b=b.split("/")
    if b[1].strip().lower() =="batsman":
        batsman.append(b[0])
    if b[1].strip().lower() =="baller":
        baller.append(b[0])

def display():
    print("Batsman: ",batsman)
    print("Baller: ",baller)