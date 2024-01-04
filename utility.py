import json
import csv
import os


def processMenu(items):

    #print 
    print("------------")
    print("**  Choise from this menu  **")
    print("-------------------------------")


    #loop to display items
    for key in items.keys():
        print("{}:{}".format(key,items[key]))
    print("-------------------------")


    #check if i choice from items or not 
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in items.keys() :return choice
        print("Wrong choice, try again.......")



def writeJSON(items,filePath):
    file = open(filePath,"w")
    data = json.dumps(items)
    file.write(data)
    file.close()

def readJSON(filePath):
    if os.path.exists(filePath):
        file = open(filePath,"r")
        data =file.read()
        items =json.loads(data)
        file.close()
        return items
    else:
        return [] 

def readCsv(filePath):
    if os.path.exists(filePath):
        with open(filePath, mode='r', newline='') as file:
            items = list(csv.DictReader(file))
            return items
    else:
        return [] 



def getCode(items,subject):
    while True:
        code = input("Enter code {}:".format(subject))
        if code in items.keys(): break
        print("Code is not found, please try again.....")
    print("----------------------")
    return code

def writeCsv(filePath, data):
    with open(filePath, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= data[0].keys())

        #fieldnames=dat[0].keys يعنى اسماء الخانات تساوى اول عنصر فى الداتا 


        #file.tell دى بتورينا مكان الفايل فين يعنى لو بتساوى صفر يبقا الفايل فاضى
        
        if file.tell() == 0:
            writer.writeheader()

        writer.writerows(data)