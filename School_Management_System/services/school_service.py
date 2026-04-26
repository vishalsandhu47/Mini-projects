class SchoolService:
    def __init__(self):
        self.students = {
            101: {
                "name": "vishal",
                "class": "10th",
                "section": "A",
                "age": 16,
                "marks": {
                    "Math": 85,
                    "Science": 90,
                    "English": 78
                }
            }
        }

    def add_student(self):
        roll_no = int(input("Enter roll number: "))

        if roll_no in self.students:
            print("Student with this roll number already exists.")
            return

        name = input("Enter student name: ")
        student_class = input("Enter class: ")
        section = input("Enter section: ")
        age = int(input("Enter age: "))

        self.students[roll_no] = {
            "name": name,
            "class": student_class,
            "section": section,
            "age": age,
            "marks": {}
        }

        print("Student added successfully.")

    def display_students(self):
        print("\n========== Student Records ==========")

        if len(self.students) == 0:
            print("No student records found.")
            return

        for roll_no, student in self.students.items():
            print(f"\nRoll No: {roll_no}")
            print(f"Name: {student['name']}")
            print(f"Class: {student['class']}")
            print(f"Section: {student['section']}")
            print(f"Age: {student['age']}")
            print("----------------------------------")

    def search_student(self):
        roll_no = int(input("Enter roll number to search: "))

        if roll_no not in self.students:
            print("Student not found.")
            return

        student = self.students[roll_no]

        print("\n========== Student Details ==========")
        print(f"Roll No: {roll_no}")
        print(f"Name: {student['name']}")
        print(f"Class: {student['class']}")
        print(f"Section: {student['section']}")
        print(f"Age: {student['age']}")

        print("\nMarks:")
        if len(student["marks"]) == 0:
            print("No marks added yet.")
        else:
            for subject, marks in student["marks"].items():
                print(f"{subject}: {marks}")

    def update_student(self):
        roll_no = int(input("Enter roll number to update: "))

        if roll_no not in self.students:
            print("Student not found.")
            return

        student = self.students[roll_no]

        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Class")
        print("3. Section")
        print("4. Age")

        choice = input("Enter your choice: ")

        if choice == "1":
            student["name"] = input("Enter new name: ")
            print("Name updated successfully.")
        elif choice == "2":
            student["class"] = input("Enter new class: ")
            print("Class updated successfully.")
        elif choice == "3":
            student["section"] = input("Enter new section: ")
            print("Section updated successfully.")
        elif choice == "4":
            student["age"] = int(input("Enter new age: "))
            print("Age updated successfully.")
        else:
            print("Invalid choice.")

    def delete_student(self):
        roll_no = int(input("Enter roll number to delete: "))

        if roll_no not in self.students:
            print("Student not found.")
            return

        del self.students[roll_no]
        print("Student deleted successfully.")

    def add_marks(self):
        roll_no = int(input("Enter roll number: "))

        if roll_no not in self.students:
            print("Student not found.")
            return

        subject = input("Enter subject name: ")
        marks = int(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Invalid marks. Marks should be between 0 and 100.")
            return

        self.students[roll_no]["marks"][subject] = marks
        print("Marks added successfully.")

    def generate_result(self):
        roll_no = int(input("Enter roll number to generate result: "))

        if roll_no not in self.students:
            print("Student not found.")
            return

        student = self.students[roll_no]
        marks = student["marks"]

        if len(marks) == 0:
            print("No marks available for result.")
            return

        total = sum(marks.values())
        percentage = total / len(marks)

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "Fail"

        print("\n========== Result ==========")
        print(f"Roll No: {roll_no}")
        print(f"Name: {student['name']}")
        print(f"Class: {student['class']}")
        print(f"Section: {student['section']}")

        print("\nMarks:")
        for subject, mark in marks.items():
            print(f"{subject}: {mark}")

        print(f"\nTotal Marks: {total}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")