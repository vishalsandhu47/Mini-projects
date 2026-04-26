from services.library_service import LibraryService

library = LibraryService()

while True:
    print("\n========== LIBRARY MENU ==========")
    print("1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Add Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        library.issue_book()
    elif choice == "3":
        library.return_book()
    elif choice == "4":
        library.add_book()
    elif choice == "5":
        print("Thank you for using Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")