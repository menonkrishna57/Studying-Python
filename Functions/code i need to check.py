def changeval(m,n):
    for i in range(n):
        if m[i]%5==0:
            m[i]//=5
        if m[i]%3==0:
            m[i]//=3
L=[25,8,75,12]
changeval(L,4)
for i in L:
    print(i,end="#")