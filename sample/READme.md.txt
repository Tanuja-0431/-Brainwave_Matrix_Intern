
📚 Library Management System
🚀 Overview
This is a web-based Library Management System built using Flask and SQLite. It allows users to view books, add books, borrow & return books, and track borrowing history with a clean and modern UI.

✨ Features
✅ Book Management – Add, view, and search books in the library.
✅ Borrow & Return System – Users can borrow books, set due dates, and return them.
✅ Borrow History Tracking – View the history of borrowed books.
✅ Database-Driven – Uses SQLite for efficient data storage.
✅ Modern UI – Styled with Bootstrap for a responsive and clean design.

🛠️ Tech Stack
Frontend: HTML, CSS, Bootstrap

Backend: Flask (Python)

Database: SQLite

Version Control: Git

📂 Project Structure
graphql
Copy
Edit
📂 library-management-system  
 ├── 📁 static/              # CSS & JavaScript files  
 ├── 📁 templates/           # HTML templates  
 │   ├── index.html          # Home page  
 │   ├── books.html          # View books page  
 │   ├── add_book.html       # Add book page  
 │   ├── history.html        # Borrow history  
 ├── app.py                  # Flask backend  
 ├── library.db               # SQLite database  
 ├── schema.sql               # Database schema  
 ├── README.md                # Project documentation  
 ├── requirements.txt         # Dependencies  
🚀 Installation & Setup
🔹 Prerequisites
Ensure you have Python 3 installed.

🔹 Step 1: Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
🔹 Step 2: Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
🔹 Step 3: Set Up Database
Run the following command to create the SQLite database:

sh
Copy
Edit
sqlite3 library.db < schema.sql
🔹 Step 4: Run the Flask Application
sh
Copy
Edit
python app.py
The app will be running at http://127.0.0.1:5000 🚀

📸 Screenshots
✨ Home Page

✨ View Books

✨ Borrow & Return

🏆 Future Enhancements
✅ Add user authentication for admin and members.
✅ Implement email notifications for due dates.
✅ Integrate a cloud database for scalability.

🤝 Contributing
Want to improve this project? Feel free to fork and contribute! Open an issue or submit a pull request.

📜 License
This project is licensed under the MIT License.

💡 Connect With Me
🔗 LinkedIn | 🐙 GitHub