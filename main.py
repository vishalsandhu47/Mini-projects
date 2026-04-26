from services.school_service import SchoolService

school = SchoolService()

while True:
    print("\n========== SCHOOL MANAGEMENT MENU ==========")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add Marks")
    print("7. Generate Result")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        school.add_student()
    elif choice == "2":
        school.display_students()
    elif choice == "3":
        school.search_student()
    elif choice == "4":
        school.update_student()
    elif choice == "5":
        school.delete_student()
    elif choice == "6":
        school.add_marks()
    elif choice == "7":
        school.generate_result()
    elif choice == "8":
        print("Thank you for using School Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
