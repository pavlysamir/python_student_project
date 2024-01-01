from utility import *
from students import *
import os

while True:
    os.system("cls")
    print("Students program")


    choice = processMenu({
        "1" : "Students ",
        "2" : "Courses ",
        "3" : "Grades ",
        "0" : "Exit "
    })

    if choice == "1":
        os.system("cls") 
        listStudents()
        student_choice = processMenu({
        "1" : "View Students ",
        "2" : "Add Student ",
        "3" : "Edit Student ",
        "4" : "Remove Student ",
        "0": "back..."
    })
        
        if student_choice =="1": viewStudent()
        elif student_choice =="2": addStudent()
        elif student_choice =="3": editStudent()
        elif student_choice =="4": removeStudent()
        elif student_choice =="0":back()

    elif choice =="2": print("courses")
    elif choice =="3":print("grades")
    elif choice =="0": break
    input("press any key to continue...")



