def add_student():
    with open("students.txt", "a") as f:
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        clas = input("Enter Class: ")
        f.write(f"{sid},{name},{age},{clas}\n")
    print("Student added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as f:
            print("\n--- Student Records ---")
            for line in f:
                sid, name, age, clas = line.strip().split(",")
                print(f"ID: {sid}, Name: {name}, Age: {age}, Class: {clas}")
    except FileNotFoundError:
        print("No records found.")


def search_student():
    sid = input("Enter Student ID to search: ")
    found = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == sid:
                    print(f"Found → ID: {data[0]}, Name: {data[1]}, Age: {data[2]}, Class: {data[3]}")
                    found = True
        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("File not found.")


def delete_student():
    sid = input("Enter Student ID to delete: ")
    lines = []
    deleted = False

    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()

        with open("students.txt", "w") as f:
            for line in lines:
                if not line.startswith(sid + ","):
                    f.write(line)
                else:
                    deleted = True

        if deleted:
            print("Student deleted successfully!")
        else:
            print("Student ID not found.")

    except FileNotFoundError:
        print("File not found.")


def menu():
    
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
