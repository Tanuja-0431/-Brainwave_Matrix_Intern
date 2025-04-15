from flask import Flask, render_template
import sqlite3
from flask import request

app = Flask(__name__)
db_path = r'E:\Task 2\movie_rental.db'

def get_data(query, params=None):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows


@app.route('/')
def home():
    data = {
        'customers': get_data("SELECT COUNT(*) AS count FROM Customers")[0]['count'],
        'movies': get_data("SELECT COUNT(*) AS count FROM Movies")[0]['count'],
        'rentals': get_data("SELECT COUNT(*) AS count FROM Rentals")[0]['count'],
        'payments': get_data("SELECT COUNT(*) AS count FROM Payments")[0]['count']
    }
    return render_template('home.html', data=data)


@app.route('/customers')
def customers():
    rows = get_data("SELECT * FROM Customers")
    return render_template('customers.html', customers=rows)

@app.route('/movies')
def movies():
    search = request.args.get('q', '')
    if search:
        query = """
        SELECT m.movie_id, m.title, m.release_year, g.name as genre, m.rating, m.stock
        FROM Movies m
        JOIN Genres g ON m.genre_id = g.genre_id
        WHERE LOWER(m.title) LIKE ? OR LOWER(g.name) LIKE ? OR LOWER(m.rating) LIKE ?
        """
        like_query = f'%{search.lower()}%'
        rows = get_data(query, [like_query, like_query, like_query])
    else:
        rows = get_data("""
        SELECT m.movie_id, m.title, m.release_year, g.name as genre, m.rating, m.stock
        FROM Movies m
        JOIN Genres g ON m.genre_id = g.genre_id
        """)
    return render_template('movies.html', movies=rows, search=search)



@app.route('/rentals')
def rentals():
    rows = get_data("""
        SELECT r.rental_id, c.name as customer, m.title as movie, r.rental_date, r.return_date
        FROM Rentals r
        JOIN Customers c ON r.customer_id = c.customer_id
        JOIN Movies m ON r.movie_id = m.movie_id
    """)
    return render_template('rentals.html', rentals=rows)

@app.route('/payments')
def payments():
    rows = get_data("""
        SELECT p.payment_id, c.name as customer, m.title as movie, p.amount, p.payment_date
        FROM Payments p
        JOIN Rentals r ON p.rental_id = r.rental_id
        JOIN Customers c ON r.customer_id = c.customer_id
        JOIN Movies m ON r.movie_id = m.movie_id
    """)
    return render_template('payments.html', payments=rows)

if __name__ == '__main__':
    app.run(debug=True)


