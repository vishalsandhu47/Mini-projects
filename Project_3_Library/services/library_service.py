from datetime import datetime

class LibraryService:
    def __init__(self):
        self.books = {
            101: {
                "title": "Python Programming",
                "author": "Guido van Rossum",
                "available": True,
                "issued_to": None,
                "issue_date": None,
                "days_allowed": None
            },
            102: {
                "title": "Data Structures",
                "author": "Mark Allen",
                "available": True,
                "issued_to": None,
                "issue_date": None,
                "days_allowed": None
            },
            103: {
                "title": "Machine Learning Basics",
                "author": "Andrew Ng",
                "available": True,
                "issued_to": None,
                "issue_date": None,
                "days_allowed": None
            }
        }

    def display_books(self):
        print("\n========== Available Books ==========")

        for book_id, book in self.books.items():
            status = "Available" if book["available"] else "Issued"
            print(f"Book ID: {book_id}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Status: {status}")
            print("-----------------------------------")

    def issue_book(self):
        book_id = int(input("Enter Book ID to issue: "))

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if not book["available"]:
            print("Sorry, this book is already issued.")
            return

        student_name = input("Enter student name: ")
        days_allowed = int(input("Enter number of days for issuing book: "))

        issue_date = datetime.now()

        book["available"] = False
        book["issued_to"] = student_name
        book["issue_date"] = issue_date
        book["days_allowed"] = days_allowed

        print("\nBook issued successfully.")
        print(f"Book Name: {book['title']}")
        print(f"Issued To: {student_name}")
        print(f"Issue Date: {issue_date.strftime('%d-%m-%Y')}")
        print(f"Allowed Days: {days_allowed}")

        print("\nFine Notice:")
        print("After allowed days, fine will be applied.")
        print("1st week late fine: Rs. 10/day/book")
        print("2nd week late fine: Rs. 20/day/book")
        print("3rd week late fine: Rs. 60/day/book")
        print("Fine will increase week by week.")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if book["available"]:
            print("This book was not issued.")
            return

        return_date = datetime.now()
        issue_date = book["issue_date"]

        total_days = (return_date - issue_date).days
        late_days = total_days - book["days_allowed"]

        print("\n========== Return Details ==========")
        print(f"Book Name: {book['title']}")
        print(f"Issued To: {book['issued_to']}")
        print(f"Issue Date: {issue_date.strftime('%d-%m-%Y')}")
        print(f"Return Date: {return_date.strftime('%d-%m-%Y')}")

        if late_days <= 0:
            print("Book returned on time.")
            print("Fine: Rs. 0")
        else:
            fine = self.calculate_fine(late_days)
            print(f"Late Days: {late_days}")
            print(f"Fine Applied: Rs. {fine}")

        book["available"] = True
        book["issued_to"] = None
        book["issue_date"] = None
        book["days_allowed"] = None

        print("Book returned successfully.")

    def calculate_fine(self, late_days):
        total_fine = 0

        for day in range(1, late_days + 1):
            week = (day - 1) // 7 + 1
            daily_fine = 10

            for multiplier in range(2, week + 1):
                daily_fine *= multiplier

            total_fine += daily_fine

        return total_fine

    def add_book(self):
        book_id = int(input("Enter new Book ID: "))
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        if book_id in self.books:
            print("Book ID already exists.")
            return

        self.books[book_id] = {
            "title": title,
            "author": author,
            "available": True,
            "issued_to": None,
            "issue_date": None,
            "days_allowed": None
        }

        print("Book added successfully.")