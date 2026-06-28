from database import create_students_table
from operations import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

create_students_table()

while True:

    print("\n" + "=" * 40)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\n👋 Thank you for using Student Management System.")
        break

    else:
        print("\n❌ Invalid Choice. Please try again.")