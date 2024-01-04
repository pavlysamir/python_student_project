# import json
# from datetime import datetime
# import csv
# import matplotlib.pyplot as plt
# import pandas as pd
# STUDENTS_FILE = "students.json"
# students_data = []
# COURSES_FILE = "courses.json"
# courses_data = []
# all_grades=[]
# Gradesfile = 'course_code.csv'
# # Load existing student data
# def load_students_data_file():
#     try:
#         with open("students.json", "r") as file:
#             students_data = json.load(file)
#             return students_data
#     except FileNotFoundError:
#         print("student file not founded")
# # Function to save students data to file
# def save_students_data_file():
#     with open("students.json", "w") as file:
#         json.dump(students_data, file, indent=2)
# # Function to print students information
# def print_allstudents():
#     print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#     print("-----------------")
#     print("List of Students:")
#     print("-----------------")
#     for student in students_data:
#         print(f"Code: {student['code']}, Name: {student['name']}, Birthdate: {student['birthdate']}")
#     print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
# # Function to edit students information
# def add_student():
#     print("********* Add a New Student ********** ")
#     code = input("Enter student code for ex s#num : ")
#     name = input("Enter student name: ")
#     birthdate_str = input("Enter student birthdate (DD-MM-YYYY) for ex 30-6-2000: ")


#     new_student = {"code": code, "name": name, "birthdate": birthdate_str}
#     students_data.append(new_student)
#     #save_students_data_file()
#     print(f"Student {name} added successfully.")
# # Function to edit student information
# def edit_student():
#     print("Edit Student Information:")
#     code = input("Enter student code you need to edit: ")
#     for student in students_data:
#         if student["code"] == code:
#             print(f"Editing student: {student['name']}")
#             new_name = input("Enter new name (press Enter to keep current): ").strip()
#             new_birthdate_str = input("Enter new birthdate (YYYY-MM-DD) (press Enter to keep current): ").strip()
#             if new_name:
#                 student["name"] = new_name
#             if new_birthdate_str:
#                 try:
#                     new_birthdate = datetime.strptime(new_birthdate_str, "%Y-%m-%d").date()
#                     student["birthdate"] = new_birthdate_str
#                 except ValueError:
#                     print("Invalid date format. Birthdate not updated.")
#             #save_students_data_file()
#             print("Student information updated successfully.")
#             break
#     else:
#         print(f"Student with this code {code} not found.")
# # Function to remove a student
# def remove_student():
#     print("Remove Student:")
#     code = input("Enter student code you need to remove: ")
#     for student in students_data:
#         if student["code"] == code:
#             students_data.remove(student)
#             #save_students_data_file()
#             print(f"Student {student['name']} removed successfully.")
#             break
#     else:
#         print(f"Student with this code {code} not found.")

# ##########################
# ##########################

# # Load existing courses data
# def load_courses_data_file():
#     try:
#         with open("courses.json", "r") as file:
#             courses_data = json.load(file)
#             return courses_data
#     except FileNotFoundError:
#         print("courses file not found please check it to can load the data")
# # Function to save courses data to file
# def save_courses_data_file():
#     with open("courses.json", "w") as file:
#         json.dump(courses_data, file, indent=2)
# #Function to print courses information
# def print_allcourses():
#     print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#     print("----------------")
#     print("List of Courses:")
#     print("----------------")
#     for course in courses_data:
#         print(f"Code: {course['code']}, Name: {course['name']}, Max degree: {course['maxdegree']}")
#     print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
# # Function to edit student information
# def add_course():
#     print("********* Add a New Course ********** ")
#     code = input("Enter Course code for ex c#num : ")
#     name = input("Enter course name: ")
#     maxdegree = input("Enter course max degree : ")
#     new_course = {"code": code, "name": name, "maxdegree": maxdegree}
#     courses_data.append(new_course)
#     #save_courses_data_file()
#     print(f"Course {name} added successfully.")
# # Function to edit course information
# def edit_course():
#     print("Edit course Information:")
#     code = input("Enter course code you need to edit: ")
#     for course in courses_data:
#         if course["code"] == code:
#             print(f"Editing course: {course['name']}")
#             new_name = input("Enter new name (press Enter to keep current): ").strip()
#             maxdegree = input("Enter course max degree (press Enter to keep current): ").strip()
#             if new_name:
#                 course["name"] = new_name
#             if maxdegree:
#                 course["maxdegree"] = maxdegree
#             #save_courses_data_file()
#             print("Course information updated successfully.")
#             break
#     else:
#         print(f"Course with this code {code} not found.")
# # Function to remove a student
# def remove_course():
#     print("Remove Course:")
#     code = input("Enter Course code you need to remove: ")
#     for course in courses_data:
#         if course["code"] == code:
#             courses_data.remove(course)
#             #save_courses_data_file()
#             print(f"Course {course['name']} removed successfully.")
#             break
#     else:
#         print(f"Course with this code {code} not found.")

# #########################
# #########################
# #calc degree
# def calc_GPA(degree):
#     if degree >= 95:
#         msg ="A+ grade"
#     elif degree >= 90:
#         msg ="A grade"
#     elif degree >= 85:
#         msg ="A- grade"
#     elif degree >= 80:
#         msg ="B+ grade"
#     elif degree >= 75:
#         msg ="B grade"
#     elif degree >= 70:
#         msg ="B- grade"
#     elif degree >= 65:
#         msg ="C+ grade"
#     elif degree >= 60:
#         msg ="C grade"
#     elif degree >= 57:
#         msg ="C- grade"
#     elif degree >= 54:
#         msg ="D+ grade"
#     elif degree >= 50:
#         msg ="D grade"
#     else:
#         msg ="F grade"
#     return msg
# # Function to enter grades of courses for all students
# def addgrades_allstudents():
#     all_grades.clear()
#     for student in students_data:
#         print(f"\nProcessing student: {student['name']} ({student['code']})")
#         for course in courses_data:
#             print(f"\nAssigning grade of course ({course['name']}) and its code is ({course['code']}) and its max degree from ({course['maxdegree']}) ")
#             grade = int(input(f"Enter grade for student {student['name']} in {course['name']} course : "))
#             gpa=calc_GPA(grade)
#             newgrade = {"studentcode": student['code'], "studentname":student['name'],
#                         "coursecode": course["code"],"coursename":course['name'] ,
#                         "coursemaxdegree":course['maxdegree'], "studentdegree": grade,"studentGPA": gpa}
#             all_grades.append(newgrade)
#     print("\n Grades assignment completed.")
#     return all_grades
# # Function to enter grades of courses for all students
# #bouns
# def editgrade_forstud():
#     code = input("Enter student code you need to edit his grade: ")
#     for student in all_grades:
#         if student["studentcode"] == code:
#             newgrade = int(input(f"Enter grade for student {student['studentcode']} in {student['coursename']} course : "))
#             newgpa = calc_GPA(newgrade)
#             student["studentdegree"]=newgrade
#             student["studentGPA"]=newgpa
#             print(f"grade for student {student['studentcode']} in"
#                   f" {student['coursename']} course updated successfully.")
#     else:
#         print("student not founded")
# # Function to save all_grades to CSV file
# def save_grades_to_csv():
#     with open(Gradesfile, mode='w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=["studentcode","studentname","coursecode","coursename","coursemaxdegree","studentdegree","studentGPA"])
#         writer.writeheader()
#         writer.writerows(all_grades)
# #Function to load all_grades from CSV file to all_grades list
# def load_grades_from_csv():
#     all_grades = []
#     try:
#         with open(Gradesfile, mode='r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 all_grades.append({
#                     "studentcode": row["studentcode"],
#                     "studentname":row["studentname"],
#                     "coursecode": row["coursecode"],
#                     "coursename":row["coursename"],
#                     "coursemaxdegree":row["coursemaxdegree"],
#                     "studentdegree": row["studentdegree"],
#                     "studentGPA":row["studentGPA"]
#                 })
#         print(f"Grades for course {course_code} loaded successfully.")
#     except FileNotFoundError:
#         print("Grades file not found please check it to can load the data.")
#     return all_grades
# #Function to print grades of courses for all students
# def print_allstudentsgrades():
#     for row in all_grades:
#         print(row)
# # Function to generate a bar chart for students' results per course
# def generate_bar_chart():
#     course_code=input("Enter the course code: ")#c1 math
#     df = pd.DataFrame(all_grades)
#     grades = df[df["coursecode"] == course_code]
#     y=grades["studentname"] #["mohamed","menna","yousef"]
#     x=grades["studentdegree"]#[85,90,100]
#     plt.pie(x, labels=y)
#     plt.show()
#     print("course code not founded")
# # Function to generate a pie chart for students' results per course
# def generate_pie_chart():
#     course_code = input("Enter the course code: ")
#     df = pd.DataFrame(all_grades)
#     grades = df[df["coursecode"] == course_code]
#     y=grades["studentname"]
#     list=grades["studentdegree"]
#     x = [int(i) for i in list]# convert numbers int
#     plt.bar(y, x)
#     plt.show()

# print("course code not founded")
# # Function to print student's result to HTML file
# def print_student_result_to_html():
#     student_code=input("Enter student code you need to print his certificate: ")
#     filename = f"{student_code}.html"
#     with open(filename, "w") as file:
#         file.write("<html>\n")
#         file.write("<head>\n")
#         file.write("<title>Student Result</title>\n")
#         file.write("</head>\n")
#         file.write("<body>\n")
#         file.write(f"<h1>Student Code: {student_code}</h1>\n")
#         file.write("<table border='1'>\n")
#         file.write(
#             "<tr><th>Course Code</th><th>Course Name</th><th>Course Max Degree</th><th>Student Degree</th></tr>\n")
#         for result in all_grades:
#             if result["studentcode"] == student_code:
#                 file.write(
#                     f"<tr><td>{result['coursecode']}</td><td>{result['coursename']}</td><td>{result['coursemaxdegree']}</td><td>{result['studentdegree']}</td></tr>\n")

#         file.write("</table>\n")
#         file.write("</body>\n")
#         file.write("</html>\n")

#     print(f"Student result for {student_code} saved to {filename}.")

# ### main ###
# #load data from files at the start of programm
# students_data=load_students_data_file()
# courses_data=load_courses_data_file()
# all_grades=load_grades_from_csv()


# while True:
#     print("------------------------------------------------------------")
#     print("*********** Welcome to Student Management System ***********")
#     print("------------------------------------------------------------")
#     print("1. print All Students")
#     print("2. Add Student")
#     print("3. Edit Student")
#     print("4. Remove Student")
#     print("5. Print All Courses")
#     print("6. Add Course")
#     print("7. Edit Course")
#     print("8. Remove Course")
#     print("9. Add Grades for All Students")
#     print("10. Print courses Grades For All Students")
#     print("11. Edit grades for specific student")
#     print("12 generate_bar_char for selected course")
#     print("13 generate_pie_char for selected course")
#     print("14 print student result to HTML file")
#     print("0. Save Data And Exit")
#     choice = input("Enter your choice (0-14): ")

#     if choice == "1":
#         print_allstudents()
#     elif choice == "2":
#         add_student()
#     elif choice == "3":
#         edit_student()
#     elif choice == "4":
#         remove_student()
#     elif choice == "5":
#         print_allcourses()
#     elif choice == "6":
#         add_course()
#     elif choice == "7":
#         edit_course()
#     elif choice == "8":
#         remove_course()
#     elif choice == "9":
#         all_grades=addgrades_allstudents()
#     elif choice == "10":
#         print_allstudentsgrades()
#     elif choice== "11":
#         editgrade_forstud()
#     elif choice== "12":
#         generate_bar_chart()
#     elif choice== "13":
#         generate_pie_chart()
#     elif choice== "14":
#         print_student_result_to_html()
#     elif choice == "0":
#         #save data into files at the end of programm
#         save_students_data_file()
#         save_courses_data_file()
#         save_grades_to_csv()
#         print("Data Saved in files !! Exiting the program")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 0 and 14.")