import pickle as p
def readinfo():
    f=open("Textfile.bin" ,"rb")
    counter=0
    while True:

        try:
            a=p.load(f)
            if a[2] in "Ff":
                counter+=1
        except:
            break
    print(counter)

def smortkid():
    f=open("Textfile.bin" ,"rb")
    aboutsmort=[]
    while True:

        try:
            a=p.load(f)
            if a[3]>aboutsmort[3]:
                aboutsmort=[a[0],a[1],a[2],a[3]]
        except:
            break
    print(aboutsmort[3])
    print(aboutsmort)