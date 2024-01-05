from utility import *
import matplotlib.pyplot as plt


all_grades = {}

def calc_GPA(degree):
    if degree >= 95:
        msg ="A+ grade"
    elif degree >= 90:
        msg ="A grade"
    elif degree >= 85:
        msg ="A- grade"
    elif degree >= 80:
        msg ="B+ grade"
    elif degree >= 75:
        msg ="B grade"
    elif degree >= 70:
        msg ="B- grade"
    elif degree >= 65:
        msg ="C+ grade"
    elif degree >= 60:
        msg ="C grade"
    elif degree >= 57:
        msg ="C- grade"
    elif degree >= 54:
        msg ="D+ grade"
    elif degree >= 50:
        msg ="D grade"
    else:
        msg ="F grade"
    return msg



def listGrades():
    global all_grades
    all_grades = readCsv("courses-grades-code.csv")
    print("List of all grades for students:")
    print("**********************************")
    for student_grades in all_grades:
        student_code = student_grades["student_code"]
        english = student_grades["english"]
        english_grade = calc_GPA(int(english))
        math = student_grades["math"]
        math_grade = calc_GPA(int(math))
        autuCAD = student_grades["autuCAD"]
        autuCAD_grade = calc_GPA(int(autuCAD))
        humanRight = student_grades["humanRight"]
        humanRight_grade = calc_GPA(int(humanRight))
        programming = student_grades["programming"]
        programming_grade = calc_GPA(int(programming))

        print(f"Student Code: {student_code}")
        print(f"English: {english}, GPA is: {english_grade}")
        print(f"Math: {math}, GPA is: {math_grade}")
        print(f"AutoCAD: {autuCAD}, GPA is: {autuCAD_grade}")
        print(f"Human Right: {humanRight}, GPA is: {humanRight_grade}")
        print(f"Programming: {programming}, GPA is: {programming_grade}")
        print("-----------------------------")
        print("\n")

def getStudentGrades():
    global all_grades
    student_code= input("Enter student code: ")
    # Search for the student by their code
    student_found = False
    for student_grades in all_grades:
        if student_grades["student_code"] == student_code:
            student_found = True
            print("Grades for Student with Code {}: ".format(student_code))
            print("English: {}".format(student_grades["english"]))
            print("Math: {}".format(student_grades["math"]))
            print("AutoCAD: {}".format(student_grades["autuCAD"]))
            print("Human Right: {}".format(student_grades["humanRight"]))
            print("Programming: {}".format(student_grades["programming"]))
            break

    if not student_found:
        print("Student with Code {} not found.".format(student_code))



def addNewStudent():

    student_code = input("Enter student code: ")
    english = input("Enter English grade: ")
    math = input("Enter Math grade: ")
    autuCAD = input("Enter AutoCAD grade: ")
    humanRight = input("Enter Human Right grade: ")
    programming = input("Enter Programming grade: ")

    # Create a dictionary for the new student
    new_student = {
        "\n"
        "student_code": student_code,
        "english": english,
        "math": math,
        "autuCAD": autuCAD,
        "humanRight": humanRight,
        "programming": programming,
    }

    writeCsv("courses-grades-code.csv", [new_student])

    print("Student with code {} added successfully.".format(student_code))


def printStudentResultToHtml():
    student_code=input("Enter student code you need to print his certificate: ")
    filename = f"{student_code}.html"
    with open(filename, "w") as file:
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("<title>Student Result</title>\n")
        file.write("<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css\">\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write("<div class=\"container\">\n")
        file.write("<div class=\"row\">\n")
        file.write(f"<h3>Student Code: {student_code}</h3>\n")
        file.write("<table class='table'>\n")
        file.write(
            "<tr><th>English grade</th><th>Math grade</th><th>autuCAD grade</th><th>humanRight grade</th><th>programming grade</th></tr>\n")
        for result in all_grades:
            if result["student_code"] == student_code:
                english_grade_gba = calc_GPA(int(result['english']))
                math_grade_gba = calc_GPA(int(result['math']))
                autoCad_grade_gba = calc_GPA(int(result['autuCAD']))
                hunam_grades_gba = calc_GPA(int(result['humanRight']))
                programming_grades_gba = calc_GPA(int(result['english']))
                file.write(
                    f"<tr><td>{result['english']}</td><td>{result['math']}</td><td>{result['autuCAD']}</td><td>{result['humanRight']}</td><td>{result['programming']}</td></tr>\n")
                file.write(
                    f"<tr><td>{english_grade_gba}</td><td>{math_grade_gba}</td><td>{autoCad_grade_gba}</td><td>{hunam_grades_gba}</td><td>{programming_grades_gba}</td></tr>\n")               
        file.write( "<tr><th>max degree: 90</th><th>max degree: 90</th><th>max degree: 90</th><th>max degree: 90</th><th>max degree: 90</th></tr>\n")

        file.write("</table>\n")
        file.write("</body>\n")
        file.write("</html>\n")

    print(f"Student result for {student_code} saved to {filename}.")    




def generateBarChartForStudent(choice):
    global all_grades
    student_codes=[]
    english_grades=[]
    math_grades=[]
    autoCad_grades=[]
    humanRights_grades=[]
    programming_grades=[]
    for grade in all_grades:
        student_codes.append(grade["student_code"])
        english_grades.append(grade["english"])
        math_grades.append(grade["math"])
        autoCad_grades.append(grade["autuCAD"])
        humanRights_grades.append(grade["humanRight"])
        programming_grades.append(grade["programming"])

    if choice=="1":
        english_grades, student_codes = zip(*sorted(zip(english_grades, student_codes)))
        showBarChart('English grads for student',student_codes,english_grades)
    elif choice=="2":
        math_grades, student_codes = zip(*sorted(zip(math_grades, student_codes)))
        showBarChart('Math grads for student',student_codes,math_grades)
    elif choice=="3":
        autoCad_grades, student_codes = zip(*sorted(zip(autoCad_grades, student_codes)))
        showBarChart('AutoCad grads for student',student_codes,autoCad_grades)    
    elif choice=="4":
        humanRights_grades, student_codes = zip(*sorted(zip(humanRights_grades, student_codes)))
        showBarChart('Human Rights grads for student',student_codes,humanRights_grades)
    elif choice=="5":
        programming_grades, student_codes = zip(*sorted(zip(programming_grades, student_codes)))
        showBarChart('Programming grads for student',student_codes,programming_grades)
    else :
        print("wrong choice, please try again  :)")
        return

def generatePieChartForStudent(choice):
    global all_grades
    student_codes=[]
    english_grades=[]
    math_grades=[]
    autoCad_grades=[]
    humanRights_grades=[]
    programming_grades=[]
    for grade in all_grades:
        student_codes.append(grade["student_code"])
        english_grades.append(int(grade["english"]))
        math_grades.append(grade["math"])
        autoCad_grades.append(grade["autuCAD"])
        humanRights_grades.append(grade["humanRight"])
        programming_grades.append(grade["programming"])

    if choice=="1":
        english_grades, student_codes = zip(*sorted(zip(english_grades, student_codes)))
        showPieChart('English grads for student',english_grades,english_grades)
    elif choice=="2":
        math_grades, student_codes = zip(*sorted(zip(math_grades, student_codes)))
        showPieChart('Math grads for student',math_grades,math_grades)
    elif choice=="3":
        autoCad_grades, student_codes = zip(*sorted(zip(autoCad_grades, student_codes)))
        showPieChart('AutoCad grads for student',autoCad_grades,autoCad_grades)    
    elif choice=="4":
        humanRights_grades, student_codes = zip(*sorted(zip(humanRights_grades, student_codes)))
        showPieChart('Human Rights grads for student',humanRights_grades,humanRights_grades)
    elif choice=="5":
        programming_grades, student_codes = zip(*sorted(zip(programming_grades, student_codes)))
        showPieChart('Programming grads for student',programming_grades,programming_grades)
    else :
        print("wrong choice, please try again  :)")
        return



def showBarChart(title,xAxis,yAxis):
    plt.title(title)
    plt.bar(xAxis,yAxis)
    plt.show()

def showPieChart(title,xAxis,yAxis):
    
    plt.title(title)
    plt.pie(xAxis,labels=yAxis)
    plt.show()