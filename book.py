from library_item import LibraryItem

class Book(LibraryItem):  
    def __init__(self, title, author, isbn, status="available"):
        self._title = title       
        self._author = author
        self._isbn = isbn
        self._status = status

    
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def status(self):
        return self._status

    def is_available(self):
        return self._status == "available"

    def issue(self):
        if self.is_available():
            self._status = "issued"
            return True
        return False

    def return_book(self):
        if not self.is_available():
            self._status = "available"
            return True
        return False

    
    def to_dict(self):
        return {
            "title": self._title,
            "author": self._author,
            "isbn": self._isbn,
            "status": self._status
        }

    def __str__(self):
        return f"{self._title} by {self._author} | ISBN: {self._isbn} | Status: {self._status}"
