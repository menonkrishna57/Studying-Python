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
    likes=[]
    dislikes=[]
    file_object=open("C:\\Users\\menon\\Codes\\Studying-Python\\Hash code\\d_difficult.in.txt","r")
    potential_cust=int(file_object.readline())
    file_contents=file_object.readlines()
    for i in range(len(file_contents)):
        if i%2:
            dislikes.append(file_contents[i].split())
        else:
            likes.append(file_contents[i].split())
    

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
    totaldislikes=[]
    totallikes=[]
    for i in likes:
        for p in i:
            if p.isnumeric()==False:
                totallikes.append(p)
                allIngredients(p)
    for i in dislikes:
        for p in i:
            if p.isnumeric()==False:
                totaldislikes.append(p)
                allIngredients(p)
    repeater(totallikes)    


"""def dislikeCalc():
    global totaldislikes
    totaldislikes=[]
    for i in dislikes:
        for p in i:
            if p.isnumeric()==False:
                totaldislikes.append(p)
                allIngredients(p)
    repeater(totaldislikes)"""



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
        a=set(c(ingred, i))
        p.append(a)
        print(a)
    p.append((ingred))
    return p #Gets all the possible ingredients

def maxcustomers(customers_for_all):
    maxcustoms=0
    maxmenu=[]
    for i in range(len(customers_for_all)):
        if maxcustoms<customers_for_all[i][0]:
            maxcustoms=customers_for_all[i][0]
            maxmenu=customers_for_all[i][1]
    return maxcustoms,maxmenu


def master():
    file_inputer()
    #inputer()
    likeCalc()
    all_possible_menu=allIngreds(ingredients)
    
    #dislikeCalc()
    
    
    print(all_possible_menu)
    customers=[]
    for menu_set in all_possible_menu:
        for menu in menu_set:
            customers.append([CustomerCheck(menu),menu])
    maxstuff=list(maxcustomers(customers))
    print("You will get",maxstuff[0],"with the menu as:",maxstuff[1])



master()
