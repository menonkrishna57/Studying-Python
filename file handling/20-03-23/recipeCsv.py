"""CSV file question:
Write a method createCsv() which will create "recipe . csv" with following format :
R_code, R_name, Qty, TimeTaken
Write a method SearchRecipe(), which will ask the user for the recipe and display all the details if found. Give appropriate message if 
recipe not found"""

import csv as c
def createCsv():
    file_object=open("recipe.csv","w",newline='')
    write_obj=c.writer(file_object,delimiter='\t')
    write_obj.writerow(["R_code","R_name","Qty","TimeTaken"])
    record_number=int(input("Enter the number of recipe you want to record: "))
    
    for i in range(record_number):
        r_code=int(input("Enter the Recipe Code: "))
        r_name=input("Enter the Recipe Name: ")
        qty=int(input("Enter the recipe quantity: "))
        timetaken=int(input("Enter the time taken in minutes: "))
        write_obj.writerow([r_code,r_name,qty,timetaken])
    
    file_object.close()

def searchRecipe():
    r_code=input("Enter the Recipe Code you want to search: ")
    """r_name=input("Enter the Recipe Name: ")
    qty=int(input("Enter the recipe quantity: "))
    timetaken=int(input("Enter the time taken in minutes: "))"""

    file_obj=open("recipe.csv",newline='')
    read_obj=c.reader(file_obj,delimiter='\t')
    found=False
    for i in read_obj:
        
        if i[0]==r_code:
            print(i)
            found=True
    if found==False:
        print("No recipes found for that Recipe Code.")

createCsv()
searchRecipe()    