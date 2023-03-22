"""Binary file question:
Write a method createBin() which will create a binary file "movies.dat" with the following format:
[m_id,name,numOfScreen,profit] store n records in the file(n is from user)

Write a method readBin() which will read "movies.dat" and display those records 
where number of screens >IOO and profit> 100000."""
import pickle as p 
def createBin():
    file_object=open("movies.dat","wb")
    n=int(input("Enter the number of records"))
    p.dump(["m_id","name","numOfScreen","profit"],file_object)
    for i in range(n):
        m_id=int(input("Movie Id: "))
        name=input("Enter Movie Name: ")
        numOfScreen=int(input("Enter Number of Screen: "))
        profit=int(input("Enter Profit: "))
        p.dump([m_id,name,numOfScreen,profit],file_object)
    file_object.close()

def readBin():
    file_object=open("movies.dat","rb")
    file_contents=p.load(file_object)
    try:
        while True:
            file_contents=p.load(file_object)
            if file_contents[2]>100 and file_contents[3]>100000:
                for i in range(4):
                    print(file_contents[i])
    except:
        file_object.close()
            

createBin()
readBin()