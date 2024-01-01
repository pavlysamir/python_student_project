from utility import *
import json

students = {}


def listStudents():
    global students
    students = readJSON("students.json")
    print("**  Name of Students and there codes  **")
    print("----------------------------------")
    for code in students.keys():
        student = students[code]
        print("{}: {} :{}".format(code,student["name"],student["birthday"]))

    return



def viewStudent():
    global students
    code = getCode(students)
    student = students[code]
 
    print("birthday: {}".format(student["birthday"]))
    return

def inputStudent(student):
    global students
    if "code" not in student.keys():
        while True:
            code = input("Enter code:").replace(" ","")
            if not code.isdigit():
                print("Code must not contain letters, try another....")
            elif len(code)!=3:
                print("Code lenth must be 3 digit, try another....")
            elif code in students.keys():
                print("Code already used, try another....")
            else :
                student["code"] = code
                break
        
    student["name"] = input("Enter Name:")
    student["birthday"] = input("Enter BirthDay:")
    return student
          

def addStudent():
    global students
    student =inputStudent({})
    code = student["code"]
    students[code] = student
    writeJSON(students,"students.json")
    

def editStudent():
    global students
    code = getCode(students)
    student = inputStudent(students[code])
    code = student["code"]
    students[code] = student
    writeJSON(students,"students.json")



def removeStudent():
    global students
    code = getCode(students)
    del students[code]
    writeJSON(students,"students.json")

def back():
    return