from utility import *

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
        file.write("</head>\n")
        file.write("<body>\n")
        file.write(f"<h1>Student Code: {student_code}</h1>\n")
        file.write("<table border='1'>\n")
        file.write(
            "<tr><th>English grade</th><th>Math grade</th><th>autuCAD grade</th><th>humanRight grade</th><th>programming grade</th></tr>\n")
        for result in all_grades:
            if result["student_code"] == student_code:
                file.write(
                    f"<tr><td>{result['english']}</td><td>{result['math']}</td><td>{result['autuCAD']}</td><td>{result['humanRight']}</td><td>{result['programming']}</td></tr>\n")

        file.write("</table>\n")
        file.write("</body>\n")
        file.write("</html>\n")

    print(f"Student result for {student_code} saved to {filename}.")    