import sqlite3
import os

# Use the correct database file
db_path = "E:/library.db"  # Make sure this file exists

# Debugging: Print the correct path
print(f"Using database at: {db_path}")

# Connect to the correct database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check if the database has tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)


# Function to display all books
def view_books():
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    for book in books:
        print(book)

# Function to add a new book
def add_book(title, author, isbn, category, year):
    cursor.execute("INSERT INTO Books (title, author, isbn, category, publication_year, status) VALUES (?, ?, ?, ?, ?, 'available')", 
                   (title, author, isbn, category, year))
    conn.commit()
    print("✅ Book added successfully!")

# Function to borrow a book
def borrow_book(member_id, book_id):
    cursor.execute("UPDATE Books SET status = 'borrowed' WHERE book_id = ?", (book_id,))
    cursor.execute("INSERT INTO Transactions (member_id, book_id, borrow_date, due_date) VALUES (?, ?, DATE('now'), DATE('now', '+7 days'))", 
                   (member_id, book_id))
    conn.commit()
    print("✅ Book borrowed successfully!")

# Function to return a book
def return_book(transaction_id):
    cursor.execute("UPDATE Transactions SET return_date = DATE('now') WHERE transaction_id = ?", (transaction_id,))
    cursor.execute("UPDATE Books SET status = 'available' WHERE book_id = (SELECT book_id FROM Transactions WHERE transaction_id = ?)", 
                   (transaction_id,))
    conn.commit()
    print("✅ Book returned successfully!")

# Main menu
while True:
    print("\n📚 Library Management System")
    print("1. View Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_books()
    elif choice == "2":
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        category = input("Enter category: ")
        year = int(input("Enter publication year: "))
        add_book(title, author, isbn, category, year)
    elif choice == "3":
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))
        borrow_book(member_id, book_id)
    elif choice == "4":
        transaction_id = int(input("Enter Transaction ID: "))
        return_book(transaction_id)
    elif choice == "5":
        print("Exiting... 📕")
        break
    else:
        print("Invalid choice! Try again.")

conn.close()
