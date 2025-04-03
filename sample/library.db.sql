BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Books" (
	"book_id"	INTEGER,
	"title"	TEXT NOT NULL,
	"author"	TEXT,
	"isbn"	TEXT UNIQUE,
	"category"	TEXT,
	"publication_year"	INTEGER,
	"status"	TEXT DEFAULT 'available' CHECK("status" IN ('available', 'borrowed', 'lost')),
	"borrowed_by"	TEXT,
	"borrow_date"	TEXT,
	"due_date"	TEXT,
	PRIMARY KEY("book_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Members" (
	"member_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"phone"	TEXT,
	"address"	TEXT,
	"membership_date"	DATE DEFAULT CURRENT_DATE,
	PRIMARY KEY("member_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Transactions" (
	"transaction_id"	INTEGER,
	"member_id"	INTEGER,
	"book_id"	INTEGER,
	"borrow_date"	DATE DEFAULT CURRENT_DATE,
	"due_date"	DATE,
	"return_date"	DATE DEFAULT NULL,
	"fine_amount"	REAL DEFAULT 0.00,
	PRIMARY KEY("transaction_id" AUTOINCREMENT),
	FOREIGN KEY("book_id") REFERENCES "Books"("book_id"),
	FOREIGN KEY("member_id") REFERENCES "Members"("member_id")
);
CREATE TABLE IF NOT EXISTS "Fines" (
	"fine_id"	INTEGER,
	"member_id"	INTEGER,
	"transaction_id"	INTEGER,
	"fine_amount"	REAL DEFAULT 0.00,
	"status"	TEXT DEFAULT 'unpaid' CHECK("status" IN ('paid', 'unpaid')),
	PRIMARY KEY("fine_id" AUTOINCREMENT),
	FOREIGN KEY("transaction_id") REFERENCES "Transactions"("transaction_id"),
	FOREIGN KEY("member_id") REFERENCES "Members"("member_id")
);
CREATE TABLE IF NOT EXISTS "Staff" (
	"staff_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"role"	TEXT CHECK("role" IN ('librarian', 'assistant')),
	"email"	TEXT NOT NULL UNIQUE,
	"phone"	TEXT,
	PRIMARY KEY("staff_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "BorrowHistory" (
	"id"	INTEGER,
	"book_id"	INTEGER,
	"book_title"	TEXT,
	"borrower"	TEXT,
	"borrow_date"	TEXT,
	"return_date"	TEXT,
	"late_fee"	REAL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("book_id") REFERENCES "Books"("id")
);
INSERT INTO "Books" ("book_id","title","author","isbn","category","publication_year","status","borrowed_by","borrow_date","due_date") VALUES (1,'The Great Gatsby','F. Scott Fitzgerald','9780743273565','Fiction',1925,'borrowed','charlie brown','2025-04-03','2025-05-03'),
 (2,'1984','George Orwell','9780451524935','Dystopian',1949,'borrowed','charlie brown','2025-04-03','2025-05-03'),
 (3,'To Kill a Mockingbird','Harper Lee','9780061120084','Classic',1960,'available',NULL,NULL,NULL),
 (4,'Moby Dick','Herman Melville','9781503280786','Classic',1851,'available',NULL,NULL,NULL),
 (5,'Pride and Prejudice','Jane Austen','9780141439518','Romance',1813,'borrowed','charlie brown','2025-04-03','2025-05-03'),
 (6,'The Catcher in the Rye','J.D. Salinger','9780316769488','Fiction',1951,'available',NULL,NULL,NULL),
 (7,'The Hobbit','J.R.R. Tolkien','9780261103344','Fantasy',1937,'available',NULL,NULL,NULL);
INSERT INTO "Members" ("member_id","name","email","phone","address","membership_date") VALUES (1,'Alice Johnson','alice@example.com','1234567890','123 Main St','2025-03-31'),
 (2,'Bob Smith','bob@example.com','9876543210','456 Oak St','2025-03-31'),
 (3,'Charlie Brown','charlie@example.com','5551234567','789 Pine St','2025-03-31'),
 (4,'Diana Prince','diana@example.com','4449876543','321 Elm St','2025-03-31'),
 (5,'Ethan Hunt','ethan@example.com','3336789123','567 Maple Ave','2025-03-31');
INSERT INTO "Transactions" ("transaction_id","member_id","book_id","borrow_date","due_date","return_date","fine_amount") VALUES (1,1,2,'2024-03-31','2024-04-07','2025-03-31',0.0),
 (2,2,3,'2024-03-28','2024-04-04',NULL,0.0),
 (3,3,4,'2024-03-30','2024-04-06',NULL,0.0),
 (4,4,5,'2024-03-31','2024-04-07',NULL,0.0);
INSERT INTO "Fines" ("fine_id","member_id","transaction_id","fine_amount","status") VALUES (1,2,1,3.0,'paid'),
 (2,3,2,1.5,'paid');
INSERT INTO "Staff" ("staff_id","name","role","email","phone") VALUES (1,'Emma Watson','librarian','emma@example.com','7771234567'),
 (2,'John Doe','assistant','john@example.com','6669876543');
INSERT INTO "BorrowHistory" ("id","book_id","book_title","borrower","borrow_date","return_date","late_fee") VALUES (1,1,'The Great Gatsby','Alice Smith','2025-03-31','2025-03-31',0.0),
 (2,1,'The Great Gatsby','Alice Smith','2025-03-31','2025-03-31',0.0),
 (3,1,'The Great Gatsby','Alice Smith','2025-03-31','2025-04-03',0.0),
 (4,1,'The Great Gatsby','charlie brown','2025-04-03',NULL,0.0),
 (5,3,'To Kill a Mockingbird','Alice Smith','2025-04-03','2025-04-03',0.0),
 (6,6,'The Catcher in the Rye','josh','2025-04-03','2025-04-03',0.0),
 (7,5,'Pride and Prejudice','charlie brown','2025-04-03',NULL,0.0),
 (8,2,'1984','charlie brown','2025-04-03',NULL,0.0);


INSERT INTO BorrowHistory (book_id, book_title, borrower, borrow_date, return_date)
VALUES (?, ?, ?, ?, NULL);

UPDATE Books 
SET status = 'borrowed', borrowed_by = ?, borrow_date = ?, due_date = ?
WHERE id = ?;


UPDATE BorrowHistory
SET return_date = ?
WHERE book_id = ? AND return_date IS NULL;

UPDATE Books 
SET status = 'available', borrowed_by = NULL, borrow_date = NULL, due_date = NULL
WHERE id = ?;

COMMIT;
