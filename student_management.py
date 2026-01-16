import sqlite3

def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT,
            age INTEGER,
            class TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_student():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    clas = input("Enter Class: ")
    try:
        c.execute("INSERT INTO students (id, name, age, class) VALUES (?, ?, ?, ?)", (sid, name, age, clas))
        conn.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Student ID already exists!")
    conn.close()

def view_students():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    if rows:
        print("\n--- Student Records ---")
        for sid, name, age, clas in rows:
            print(f"ID: {sid}, Name: {name}, Age: {age}, Class: {clas}")
    else:
        print("No records found.")
    conn.close()

def search_student():
    sid = input("Enter Student ID to search: ")
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id = ?", (sid,))
    row = c.fetchone()
    if row:
        print(f"Found → ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Class: {row[3]}")
    else:
        print("Student not found.")
    conn.close()

def delete_student():
    sid = input("Enter Student ID to delete: ")
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id = ?", (sid,))
    if c.rowcount > 0:
        print("Student deleted successfully!")
        conn.commit()
    else:
        print("Student ID not found.")
    conn.close()

def menu():
    init_db()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you! Program closed.")
            break
        else:
            print("Invalid choice! Try again.")


menu()

