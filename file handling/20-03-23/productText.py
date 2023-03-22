"""text file question.
Write a method createFile() which will create a file "product.txt" with the following format:
Pcode, pname,qty,price. Ask the user for number of records to be stored. Accept the details and
store it in the product.txt.
Write a method readFiIe() which will read the "product.txt" file and display only those records
where qty >IOO."""

def createFile():
    file_object=open("product.txt","w")
    record_number=int(input("Enter the number of records: "))
    files=[]
    for i in range(record_number):
        pcode=input("Product Code: ")
        pname=input("Enter Product Name: ")
        qty=input("Enter Product Quantity: ")
        price=input("Enter Product Price: ")
        record=f"{pcode}\t{pname}\t{qty}\t{price}\n"
        files.append(record)
    file_object.writelines(files)
    file_object.close()

def readFile():
    file_object=open("product.txt")
    file_contents=file_object.readlines()
    for i in file_contents:
        myfile=i.split("\t")
        if int(myfile[2])>100:
            print(i)

createFile()
readFile()