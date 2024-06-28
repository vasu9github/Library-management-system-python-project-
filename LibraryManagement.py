class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available Copies: {self.available_copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book)
            book.available_copies -= 1
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available_copies += 1
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed book: {book.title}")
                return
        print(f"No book found with ISBN: {isbn}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book)
                return
        print(f"No book found with title: {title}")

    def list_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name}")

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Removed member: {member.name}")
                return
        print(f"No member found with ID: {member_id}")

    def list_members(self):
        if not self.members:
            print("No members registered.")
        for member in self.members:
            print(member)

    def borrow_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if member and book:
            member.borrow_book(book)
        else:
            print("Invalid member ID or book ISBN.")

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if member and book:
            member.return_book(book)
        else:
            print("Invalid member ID or book ISBN.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. List Books")
        print("5. Register Member")
        print("6. Remove Member")
        print("7. List Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, isbn, copies)
            library.add_book(book)
        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn)
        elif choice == '3':
            title = input("Enter book title to search: ")
            library.search_book(title)
        elif choice == '4':
            library.list_books()
        elif choice == '5':
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")
            member = Member(member_id, name)
            library.register_member(member)
        elif choice == '6':
            member_id = input("Enter member ID to remove: ")
            library.remove_member(member_id)
        elif choice == '7':
            library.list_members()
        elif choice == '8':
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            library.borrow_book(member_id, isbn)
        elif choice == '9':
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            library.return_book(member_id, isbn)
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
