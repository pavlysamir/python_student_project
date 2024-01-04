from utility import *
from students import *
from courses import * 
from grades import *
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

    elif choice =="2": 
        os.system("cls") 
        listCaurses()
        caurse_choice = processMenu({
        "1" : "View caurses ",
        "2" : "Add caurse ",
        "3" : "Edit caurse ",
        "4" : "Remove caurse ",
        "0": "Back..."
    })
        if caurse_choice =="1": viewCaurse()
        elif caurse_choice =="2": addCaurse()
        elif caurse_choice =="3": editCaurse()
        elif caurse_choice =="4": removeCaurse()
        elif caurse_choice =="0":back()       

    elif choice =="3":
        os.system("cls")
        listGrades()
        grade_choice = processMenu({
        "1" : "View student grades ",
        "2" : "Add student grades ",
        "3" : "print student grades in HTML"
        })

        if grade_choice =="1": getStudentGrades()
        elif grade_choice =="2": addNewStudent()
        elif grade_choice =="3":printStudentResultToHtml()
    elif choice =="0": break
    input("press any key to continue...")



