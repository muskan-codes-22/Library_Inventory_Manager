# 📚 Library Inventory Manager  
A Python mini project demonstrating Object-Oriented Programming, JSON file handling, and a menu-driven command-line interface.

---

## 📌 Overview  
This project is a simple Library Inventory Manager that helps track books in a campus library. It supports adding books, issuing and returning them, searching the catalog, and saving all records in a JSON file.

The project follows modular programming and applies all **four OOP pillars** as required.

---

## 🎯 Learning Objectives  
- Implement classes using attributes and methods  
- Use all 4 OOP pillars: Abstraction, Encapsulation, Inheritance, Polymorphism  
- Handle JSON file I/O safely  
- Use try–except for error handling  
- Build a menu-driven CLI  
- Organize code in modular Python files  

---

## 🧱 OOP Pillars Demonstrated  

### **1. Abstraction**  
Implemented using an abstract base class `LibraryItem` (in `library_item.py`).  
This class forces all library items to provide `to_dict()` and `__str__()` methods.

---

### **2. Encapsulation**  
In `book.py`, attributes are private:  
`_title`, `_author`, `_isbn`, `_status`  

Values are accessed through getter methods using `@property`.

---

### **3. Inheritance**  
`Book` inherits from `LibraryItem`, gaining a shared structure with all library items.

---

### **4. Polymorphism**  
`Book` class overrides abstract methods:  
- `to_dict()`  
- `__str__()`  

This allows different library items to be printed and saved in their own way.

---

## 📁 Project Structure  
```
LIBRARY_INVENTORY_MANAGER/
│
├── book.py 
├── library_item.py 
├── inventory.py 
├── main.py 
├── catalog.json 
└── README.md 
```

---


---

## ⚙️ Features  

### ✔ Add Book  
Input title, author, ISBN → saved to JSON.

### ✔ Issue Book  
If available, status becomes `"issued"`.

### ✔ Return Book  
If issued, status becomes `"available"`.

### ✔ Search Book  
Search by title (case-insensitive, partial match).

### ✔ View All Books  
Displays the entire catalog using `__str__()`.

### ✔ JSON Persistence  
Automatically loads and saves data to `catalog.json`.

### ✔ Error Handling  
- Handles corrupted/missing JSON  
- Prevents crashes from bad inputs  

---

## ▶️ How to Run  

Open terminal in the project folder and run:

---

Use the menu to choose actions:

Add Book

Issue Book

Return Book

View All Books

Search Book

Exit

---


---

## 🗂 JSON File Format  

Example of `catalog.json`:

```json
[
    {
        "title": "harry potter",
        "author": "rowling",
        "isbn": "12345",
        "status": "available"
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "isbn": "101",
        "status": "available"
    }
]
```
---

##  👩‍💻 Author

Muskan Kumari
Programming for Problem Solving using Python
Mini Project: Library Inventory Manager

