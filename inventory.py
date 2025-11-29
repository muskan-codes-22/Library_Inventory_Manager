import json
from pathlib import Path
from book import Book

class LibraryInventory:
    def __init__(self, file_path="catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    def load_books(self):
        
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    for item in data:
                       
                        book = Book(item["title"], item["author"], item["isbn"], item["status"])
                        self.books.append(book)
        except Exception as e:
            print("Could not load books:", e)

    def save_books(self):
        
        try:
            data = []

            for b in self.books:
                data.append(b.to_dict())

            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)

        except Exception as e:
            print("Could not save books:", e)

    def add_book(self, book):
        
        self.books.append(book)
        self.save_books()

    def search_by_title(self, title):
        
        results = []
        for b in self.books:
            if title.lower() in b.title.lower():
                results.append(b)
        return results

    def search_by_isbn(self, isbn):
        
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        
        if len(self.books) == 0:
            print("No books in inventory.")
        else:
            for b in self.books:
                print(b)
