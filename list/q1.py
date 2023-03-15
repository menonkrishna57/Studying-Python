"""Write a program to accept 5 values for a list 11 from user. create another list which
will coontain the elements which are next . eg;
l1=[1,2,3,4]
l2=[2,3,4,5]"""
l1=[]
l2=[]
for i in range(5):
    a=int(input("Enter a number: "))
    l1.append(a)
    l2.append(a+1)
print(f"l1={l1}\nl2={l2}")