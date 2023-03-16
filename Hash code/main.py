def inputer():
    pc=int(input("Potential Customers: "))
    likes=[]
    dislikes=[]
    for i in range(pc):
        lk=input("Things the customer likes: ").split()
        dlk=input("Things the customer hates: ").split()
        likes.append(lk)
        dislikes.append(dlk)
    print()
inputer()

