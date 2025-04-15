
Movie Rental System

This is a Movie Rental System built as part of my internship. The project allows users to manage customers, movies, and rentals using a simple and interactive web interface built with Flask and SQLite.

---

### Table of Contents:
1. Project Overview
2. Features
3. Technologies Used
4. Setup
5. Database Schema
6. Contributions

---

### Project Overview:
The Movie Rental System allows users to manage movies, customers, rentals, and payments. It provides functionality to add, edit, delete, and search through movies and customers. It also tracks movie rentals and payment records, offering an interface for the admin to manage the system effectively.

---

### Features:
- **Movie Management:** Admin can add, edit, delete, and view movies.
- **Customer Management:** Allows the admin to manage customer records and their rental history.
- **Search Functionality:** Users can search movies by title, genre, release year, and other attributes.
- **Rental System:** Customers can rent movies, and the system tracks rental dates and returns.
- **Payment System:** Payments for rentals can be processed and recorded.
- **User Interface:** An easy-to-navigate front-end built with HTML and CSS with a responsive design and hover effects.

---

### Technologies Used:
- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **Version Control:** GitHub for source code management

---

### Setup:
To run the Movie Rental System locally, follow the steps below:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/movie-rental-system.git
    cd movie-rental-system
    ```

2. **Set Up Virtual Environment:**
    - Install virtualenv if you don’t have it:
        ```bash
        pip install virtualenv
        ```

    - Create a virtual environment:
        ```bash
        virtualenv venv
        ```

    - Activate the virtual environment:
        - On Windows:
            ```bash
            venv\Scripts\activate
            ```
        - On macOS/Linux:
            ```bash
            source venv/bin/activate
            ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    ```bash
    python app.py
    ```

5. **Access the System:**
    Open your browser and visit `http://127.0.0.1:5000/`.

---

### Database Schema:

- **Movies Table:**
    - `movie_id` (Primary Key)
    - `title`
    - `release_year`
    - `genre_id`
    - `rating`
    - `stock`

- **Customers Table:**
    - `customer_id` (Primary Key)
    - `name`
    - `email`
    - `phone`

- **Rentals Table:**
    - `rental_id` (Primary Key)
    - `movie_id` (Foreign Key)
    - `customer_id` (Foreign Key)
    - `rental_date`
    - `return_date`

- **Payments Table:**
    - `payment_id` (Primary Key)
    - `rental_id` (Foreign Key)
    - `amount`
    - `payment_date`

---

### Contributions:
If you have suggestions or improvements for this project, feel free to fork the repository and submit a pull request. You can also open an issue for any bugs or features you'd like to discuss.
