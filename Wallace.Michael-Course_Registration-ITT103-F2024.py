class Course:
    def __init__(self,name,course_id,fee):
        self.name = name
        self.course_id = course_id
        self.fee = fee

class Student:
    def __init__(self,student_id,student_name,email,courses,balance):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.courses = []
        self.balance = balance

    def enroll(self,course):
        if course in self.courses:
            print(f"Already enrolled in {course.name}")
        else:
            self.courses.append(course)
            print(f"Successfully enrolled in {course.name}")
            self.balance += course.fee

    def get_total_fee(self):
        total_fee = 0
        for course in self.courses:
            total_fee += course.fee
        print(f"The total for all enrolled students is {total_fee}")

class RegistrationSystem:
    def __init__(self):
        self.courses = []
        self.students = {}

    def add_course(self,course_id,name,fee):
        for course in self.courses:
            #check if course was already added
            if course["Course ID"] == course_id:
                print(f"Course with ID {course_id} already added")
                return
            elif course["Course Name"] == name:
                print(f"Course with Name '{name}' already added")
                return
        #Appends the course list to add the following key & value pairs
        #the values will come from the users input
        self.courses.append({"Course ID":course_id, "Course Name":name, "Course Fee":fee})
        print(f"'{name}' added to course list")

    def register_student(self,student_id,student_name,email):
        if student_id in self.students:
            print(f"Student with ID number {student_id} already registered")
        else:
            #creates a key in student dictionary to store student's ID and values for name and email in it from the user input
            self.students[student_id] = {"Name" : student_name, "Email" : email}
            print(f"{self.students[student_id].get("Name")}, registered successfully")

    def enroll_in_course(self,student_id,course_id):
        try:
            if student_id not in self.students:
                print("Student needs to be registered first! ")
            else:
                #Creates a list to store all the courses the student is registered in
                enrolled_courses = [course["Course ID"] for course in self.students[student_id].get("Courses", [])]
                #Checks, if course ID is in the list of courses the student is registered in
                if course_id in enrolled_courses:
                    print(f"Course {course_id} was already added to {self.students[student_id].get('Name')} list of courses")
                else:
                    course_name = None
                    course_fee = None
                    for course in self.courses:
                        #if course ID matches input then said course name is assigned to course_name variable
                        if course["Course ID"] == course_id:
                            #Assigns course name and course fee to the following variables
                            course_name = course["Course Name"]
                            course_fee = course["Course Fee"]
                            break
                    if course_name:
                        #Creates a list inside the student dictionary to hold courses for each student
                        #And updates the list to add course ID, Name of course and course fee
                        self.students[student_id].setdefault("Courses",[]).append({"Course ID": course_id, "Course name": course_name, "Cost": course_fee})
                        #Calculates the total cost for all the courses for a specific student
                        student.balance = sum(course.get("Cost", 0) for course in self.students[student_id]["Courses"])
                        print(f"{course_name}, {course_id} added to {self.students[student_id].get('Name')} list of courses")
                    else:
                        print("Course not Found!")
        except ValueError as e:
            print(f"Error: {e}")

    def calculate_payment(self,student_id):
        if student_id not in self.students:
            print("Student needs to be registered first! ")
        else:
            print("You must pay 40% of student balance to confirm Registration")
            print(f"The balance for {self.students[student_id].get("Name")} is ${student.balance}")
            req_amt = 40 / 100 * student.balance
            while True:
                #Checking payment amount for only numbers
                while True:
                    try:
                        payment = float(input("Enter payment amount"))
                        break
                    except ValueError:
                        print("Please input numbers for payment amount")
                if payment < req_amt:
                    print("You must pay at least 40% to confirm registration")
                    break
                else:
                    student.balance -= payment
                print(f"Registration Confirmed for {self.students[student_id].get("Name")}")
                print(f"Remaining balance for {self.students[student_id].get("Name")} is ${student.balance}")
                break

    def check_student_balance(self,student_id):
        if student_id not in self.students:
            print("Student needs to be registered first!")
        else:
            #prints balance that was calculated when student is being enrolled in a course
            print(f"The balance for {self.students[student_id].get("Name")} is ${student.balance}")

    def show_courses(self):
        if self.courses:
            print("Available Courses :")
            for course in self.courses:
                print(f"Course ID-{course["Course ID"]}, Course Name: {course["Course Name"]}, Cost: ${course["Course Fee"]}")
        else:
            print("No Course has been added as yet!")

    def show_registered_students(self):
        #creates a list to store all the names of the students stored in the student dictionary
        stud_names = [student_info["Name"] for student_info in self.students.values()]
        #prints only the names of the students that are registered
        if stud_names:
            print("All Registered Students are :")
            print(stud_names)
        else:
            print("No Registered Students as yet!")

    def show_students_in_course(self, course_id):
        try:
            student_in_course = [student for student, details in self.students.items()
            if "Courses" in details and any (course["Course ID"] == course_id for course in details["Courses"])]
            if student_in_course:
                print(f"Students enrolled in course {course_id}:")
                for stud in student_in_course:
                    print(f" - {self.students[stud]["Name"]}")
            else:
                print(f"No students enrolled in course {course_id}")
        except Exception as e:
            print(f"Error: {e}")

student = Student(student_id= "",student_name= "",email= "",courses= [],balance= 0)
registry = RegistrationSystem()

while True:
    print("STUDENT REGISTRATION MAIN MENU :")
    print("1. Register A Student")
    print("2. Show Registered Students")
    print("3. Add A Course")
    print("4. Show Available Courses")
    print("5. Enroll In Course")
    print("6. Show Students in a Course")
    print("7. Check Student Balance")
    print("8. Calculate Payment")
    print("9. EXIT")

    choice = input("Please Enter a Option Number :")
    if choice == "1":
        print("You Chose to 'Register A Student' ")
        while True:
            try:
                student_id = int(input("Please Enter Student ID "))
                break
            except ValueError:
                print("Student ID can only contain numbers ")

        while True:
            first_name = input("Enter Student's First Name ").capitalize()
            last_name = input("Enter Student's Last Name ").capitalize()
            student_name = first_name + " " + last_name
            #check if student name is alphabet letters and space
            if all(char.isalpha() or char.isspace() for char in student_name):
            #if it is break the loop of asking for name
                break
            else:
                print("Student Name can only contain LETTERS ")
        email = input("Please Enter Student Email Address ").lower()
        registry.register_student(student_id, student_name, email)

    elif choice == "2":
        registry.show_registered_students()

    elif choice == "3":
        while True:
            try:
                course_id = int(input("Enter Course ID :"))
                break
            except ValueError:
                print("ID Should only contain Numbers")
        while True:
            name = input("Enter Course Name :").capitalize()
            if all(char.isalpha() or char.isspace() for char in name):
                break
            else:
                print("Course name can only contain letters")
        while True:
            try:
                fee = float(input("Enter Course Fee :"))
                break
            except ValueError:
                print("Cost cannot contain letters")
        registry.add_course(course_id,name,fee)

    elif choice == "4":
        registry.show_courses()

    elif choice == "5":
        while True:
            try:
                student_id = int(input("Enter student ID "))
                course_id = int(input("Enter Course ID "))
                break
            except ValueError:
                print("IDs can only be digits")
        registry.enroll_in_course(student_id, course_id)

    elif choice == "6":
        print("You selected 'Show Students in a Course'")
        while True:
            try:
                course_id = int(input("Enter Course ID"))
                break
            except ValueError:
                print("Course ID can only contain 'NUMBERS'")
        registry.show_students_in_course(course_id)

    elif choice == "7":
        while True:
            try:
                student_id = int(input("Please enter student ID :"))
                break
            except ValueError:
                print("Student ID can only contain numbers!")
        registry.check_student_balance(student_id)

    elif choice == "8":
        while True:
            try:
                student_id = int(input("Please enter student ID"))
                break
            except ValueError:
                print("Student ID can only contain numbers!")
        registry.calculate_payment(student_id)

    elif choice == "9":
        print("Exiting.........")
        exit()
    else:
        print("Please input a Number between 1 & 9")