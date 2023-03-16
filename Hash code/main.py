def inputer():
    global likes,dislikes
    pc=int(input("Potential Customers: "))
    likes=[]
    dislikes=[]
    for i in range(pc):
        lk=input("Things the customer likes: ").split()
        dlk=input("Things the customer hates: ").split()
        likes.append(lk)
        dislikes.append(dlk)
    print()

def repeater(a):
    checked=list()
    final=[]
    for i in a:
        if i not in checked:
            counter=a.count(i)
            dumper=[counter,i]
            final.append(dumper)
            checked.append(i)
    print(final)
    
def likeCalc():
    global totallikes
    totallikes=[]
    for i in likes:
        for p in i:
            if p.isnumeric()==False:
                totallikes.append(p)
    repeater(totallikes)    

def dislikeCalc():
    global totaldislikes
    totaldislikes=[]
    for i in dislikes:
        for p in i:
            if p.isnumeric()==False:
                totaldislikes.append(p)
    repeater(totaldislikes)

    
    

inputer()
likeCalc()
dislikeCalc()