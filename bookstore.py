#Name:Tawonga Taibu
#Task Name: Capstone Project Databases
#Task Number: 13

#In this task, we're going also to use functions to perform specific tasks for our programs 

import sqlite3

# This function makes sure that we create our table if it does not exist
# Additionally, the table is populated with different books
def initialize_db():
    db = sqlite3.connect('database/ebookstore.db')
    cursor = db.cursor()
    
    # Create the book table if it doesn't exist
    # NB: id is the primary key
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        qty INTEGER NOT NULL
    )
    ''')
    
    # Populate the table with initial values
    books = [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12),
        (3006, 'In Search of the Elusive Zimbabwean Dream', 'Professor Mutambara', 45),
        (3007, 'Conversations with Myself', 'Nelson Mandela', 32),
        (3008, 'Battlefield of the Mind', 'Joyce Meyer', 34)
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)', books)
    db.commit()
    db.close()

# Connect to the database
def connect_db():
    return sqlite3.connect('database/ebookstore.db')

#This function allows the user to add a new book 
def add_book():
    db = connect_db()
    cursor = db.cursor()
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    cursor.execute('INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', (id, title, author, qty))
    db.commit()
    db.close()
    print("Book added successfully.")

# Update book information
def update_book():
    db = connect_db()
    cursor = db.cursor()
    id = int(input("Enter book ID to update: "))
    title = input("Enter new title (leave empty to keep current): ")
    author = input("Enter new author (leave empty to keep current): ")
    qty = input("Enter new quantity (leave empty to keep current): ")
    
    if title:
        cursor.execute('UPDATE book SET title = ? WHERE id = ?', (title, id))
    if author:
        cursor.execute('UPDATE book SET author = ? WHERE id = ?', (author, id))
    if qty:
        cursor.execute('UPDATE book SET qty = ? WHERE id = ?', (qty, id))
    
    db.commit()
    db.close()
    print("Book updated successfully.")

#This fucntion allows the user to delete a book by prompting them to enter a book's ID
def delete_book():
    db = connect_db()
    cursor = db.cursor()
    id = int(input("Enter book ID to delete: "))
    cursor.execute('DELETE FROM book WHERE id = ?', (id,))
    db.commit()
    db.close()
    print("Book deleted successfully.")

#This function allows the user to search for a certain book
#Specifically through the author or title of the book
def search_books():
    db = connect_db()
    cursor = db.cursor()
    search_term = input("Enter title or author to search: ")
    cursor.execute('SELECT * FROM book WHERE title LIKE ? OR author LIKE ?', ('%' + search_term + '%', '%' + search_term + '%'))
    results = cursor.fetchall()
    if results:
        print(f"{'ID':<10} {'Title':<40} {'Author':<30} {'Quantity':<10}")
        print('-' * 90)
        for row in results:
            print(f"{row[0]:<10} {row[1]:<40} {row[2]:<30} {row[3]:<10}")
    else:
        print("No books found.")
    db.close()

#This is the menu function which pops up first when a user has visited the program
def menu():
    initialize_db()  #Initialize database and table
    while True:
        print("\nMenu:")
        print("1.Enter to add a new book")
        print("2.Update a book")
        print("3.Delete a book")
        print("4.Search for a book")
        print("0.Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()

#References
#https://www.w3schools.com/sql/sql_ref_database.asp
#https://www.w3schools.com/python/python_functions.asp
