ingredients=[]
def inputer():
    global likes,dislikes,potential_cust
    potential_cust=int(input("Potential Customers: "))
    likes=[]
    dislikes=[]
    for i in range(potential_cust):
        lk=input("Things the customer likes: ").split()
        dlk=input("Things the customer hates: ").split()
        likes.append(lk)
        dislikes.append(dlk)
    print()

def file_inputer():
    global likes,dislikes,potential_cust
    file_object=open("input_data\\c_coarse.in.txt")
    potential_cust=int(file_object.readline())


def repeater(a):
    checked=list()
    final=[]
    for i in a:
        if i not in checked:
            counter=a.count(i)
            dumper=[counter,i]
            final.append(dumper)
            checked.append(i)
    

def allIngredients(new):#Gets all the ingredients without repetition
    global ingredients
    if new not in ingredients:
        ingredients.append(new)



def likeCalc():
    global totallikes
    totallikes=[]
    for i in likes:
        for p in i:
            if p.isnumeric()==False:
                totallikes.append(p)
                allIngredients(p)
    repeater(totallikes)    


def dislikeCalc():
    global totaldislikes
    totaldislikes=[]
    for i in dislikes:
        for p in i:
            if p.isnumeric()==False:
                totaldislikes.append(p)
                allIngredients(p)
    repeater(totaldislikes)



def CustomerCheck(ingred): #Checks how many customers with the current ingredients
        
        likedno=0
        for customer_no in range(potential_cust):
            liked=True
            for dislike_no in range(int(len(dislikes[customer_no]))):

                if dislikes[customer_no][dislike_no] in ingred:
                    liked=False
            if liked==True:
                for like_no in range(len(likes[customer_no])):

                    if likes[customer_no][like_no] not in ingred and likes[customer_no][like_no].isnumeric()==False:
                        liked=False
                if liked==True:
                    likedno+=1
        return likedno

def allIngreds(ingred):
    from itertools import combinations as c
    p=[]
    for i in range(len(ingred)):
        a=list(c(ingred, i))
        p.append(a)
    p.append((ingred))
    return p #Gets all the possible ingredients

def master():
    inputer()
    likeCalc()
    dislikeCalc()
    all_possible_menu=allIngreds(ingredients)
    print(all_possible_menu)
    for i in all_possible_menu:
        for t in i:
            print(CustomerCheck(t),t)



master()