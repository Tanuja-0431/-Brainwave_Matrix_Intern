from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import sqlite3


app = Flask(__name__)

# Connect to database
def connect_db():
    return sqlite3.connect("library.db")

# Home Page
@app.route('/')
def index():
    return render_template("index.html")

# View Books
@app.route('/books')
def view_books():
    conn = connect_db()
    cursor = conn.cursor()
    
    # ✅ Fix: Ensure the column order matches your table structure!
    cursor.execute("""
        SELECT book_id, title, author, isbn, category, publication_year, status, borrowed_by, borrow_date,  due_date
        FROM Books
    """)
    
    books = cursor.fetchall()
    conn.close()
    
    return render_template('books.html', books=books)

# Add Book Page
@app.route('/add_book', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        isbn = request.form["isbn"]
        category = request.form["category"]
        year = request.form["year"]
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Books (title, author, isbn, category, publication_year, status) VALUES (?, ?, ?, ?, ?, 'available')", 
                       (title, author, isbn, category, year))
        conn.commit()
        conn.close()
        return redirect(url_for("view_books"))

    return render_template("add_book.html")

# Borrow a Book
@app.route('/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    borrower = request.form['borrower']  
    borrow_date = datetime.now().strftime('%Y-%m-%d')

    with connect_db() as conn:  # Ensures connection closes properly
        cursor = conn.cursor()

        # Get book title
        cursor.execute("SELECT title FROM Books WHERE book_id=?", (book_id,))  # FIXED: Correct column name
        book = cursor.fetchone()

        if book:
            book_title = book[0]
            due_date = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')  # Example due date

           
            cursor.execute("""
                INSERT INTO BorrowHistory (book_id, book_title, borrower, borrow_date, return_date)
                VALUES (?, ?, ?, ?, NULL)
            """, (book_id, book_title, borrower, borrow_date))

            cursor.execute("""
                UPDATE Books 
                SET status='borrowed', borrowed_by=?, borrow_date=?, due_date=?
                WHERE book_id=? 
            """, (borrower, borrow_date, due_date, book_id))

        conn.commit() 
    return redirect(url_for('view_books'))  




# Return a Book

@app.route('/return/<int:book_id>', methods=['POST'])
def return_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Get borrow date & borrower
    cursor.execute("SELECT borrowed_by, borrow_date FROM Books WHERE book_id=?", (book_id,))
    result = cursor.fetchone()

    if result:
        borrower, borrow_date = result
        return_date = datetime.now().strftime('%Y-%m-%d')
        
        # Calculate late fee
        borrow_date_obj = datetime.strptime(borrow_date, '%Y-%m-%d')
        due_date = borrow_date_obj + timedelta(days=14)
        return_date_obj = datetime.strptime(return_date, '%Y-%m-%d')

        late_days = (return_date_obj - due_date).days
        late_fee = late_days * 2 if late_days > 0 else 0  # $2 per late day

        # Update BorrowHistory
        cursor.execute("""
            UPDATE BorrowHistory 
            SET return_date=?, late_fee=? 
            WHERE book_id=? AND borrower=? AND return_date IS NULL
        """, (return_date, late_fee, book_id, borrower))

        # Make book available
        cursor.execute("""
            UPDATE Books 
            SET status='available', borrowed_by=NULL, borrow_date=NULL, due_date=NULL 
            WHERE book_id=?
        """, (book_id,))

        conn.commit()
    conn.close()

    return redirect(url_for('view_books'))


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT * FROM Books 
        WHERE title LIKE ? OR author LIKE ?
    """, ('%' + query + '%', '%' + query + '%'))
    
    books = cursor.fetchall()
    conn.close()
    
    return render_template('books.html', books=books)

@app.route('/history')
def view_history():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BorrowHistory ORDER BY id DESC")
    history = cursor.fetchall()
    conn.close()
    
    return render_template('history.html', history=history)


if __name__ == "__main__":
    app.run(debug=True)
