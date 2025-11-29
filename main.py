from inventory import LibraryInventory
from book import Book

def menu():
    print("\n--- Library Inventory Manager ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()   

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter ISBN number: ")

            new_book = Book(title, author, isbn)
            inventory.add_book(new_book)

            print("Book added.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)

            if book and book.issue():
                inventory.save_books()
                print("Book issued.")
            else:
                print("Book not available to issue.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)

            if book and book.return_book():
                inventory.save_books()
                print("Book returned.")
            else:
                print("Book cannot be returned.")

        elif choice == "4":
            inventory.display_all()

        elif choice == "5":
            title = input("Enter title to search: ")
            results = inventory.search_by_title(title)

            if results:
                for b in results:
                    print(b)
            else:
                print("No matching books found.")

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

    