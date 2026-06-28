import mysql.connector
from database import connect_db
from student import Student


def add_student():

    print("\n========== ADD STUDENT ==========\n")

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    gender = input("Enter Gender : ")
    department = input("Enter Department : ")
    email = input("Enter Email : ")
    phone = input("Enter Phone Number : ")
    cgpa = float(input("Enter CGPA : "))

    student = Student(
        name,
        age,
        gender,
        department,
        email,
        phone,
        cgpa
    )

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    query = """
    INSERT INTO students
    (name, age, gender, department, email, phone, cgpa)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        student.name,
        student.age,
        student.gender,
        student.department,
        student.email,
        student.phone,
        student.cgpa
    )

    try:
        cursor.execute(query, values)
        connection.commit()
        print("\n✅ Student Added Successfully!\n")

    except mysql.connector.Error as err:
        connection.rollback()
        print(f"\n❌ Failed to add student: {err}\n")

    finally:
        if cursor:
           cursor.close()
        if connection.is_connected():
           connection.close()
#--------------------------------------------------------

def view_students():
    """
    Display all students from the database.
    """

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    query = "SELECT * FROM students"

    try:
        cursor.execute(query)

        students = cursor.fetchall()

        if not students:
            print("\n❌ No students found.\n")
            return

        print("\n" + "=" * 55)
        print("               STUDENT LIST")
        print("=" * 55)

        for student in students:

            (
                student_id,
                name,
                age,
                gender,
                department,
                email,
                phone,
                cgpa,
                created_at
            ) = student

            print(f"Student ID : {student_id}")
            print(f"Name       : {name}")
            print(f"Age        : {age}")
            print(f"Gender     : {gender}")
            print(f"Department : {department}")
            print(f"Email      : {email}")
            print(f"Phone      : {phone}")
            print(f"CGPA       : {cgpa}")
            print(f"Created At : {created_at}")

            print("-" * 55)

        print(f"\n📌 Total Students : {len(students)}")

    except mysql.connector.Error as err:
        print(f"\n❌ Database Error: {err}")

    finally:
        if cursor:
            cursor.close()

        if connection.is_connected():
            connection.close()
#------------------------------------------------------------
def search_student():
    """
    Search and display a student by Student ID.
    """

    print("\n" + "=" * 55)
    print("             SEARCH STUDENT")
    print("=" * 55)

    student_id = int(input("Enter Student ID : "))

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    query = """
    SELECT * FROM students
    WHERE student_id = %s
    """

    try:

        cursor.execute(query, (student_id,))

        student = cursor.fetchone()

        if student is None:
            print("\n❌ Student Not Found.\n")
            return

        (
            student_id,
            name,
            age,
            gender,
            department,
            email,
            phone,
            cgpa,
            created_at
        ) = student

        print("\n" + "=" * 55)
        print("             STUDENT DETAILS")
        print("=" * 55)

        print(f"Student ID : {student_id}")
        print(f"Name       : {name}")
        print(f"Age        : {age}")
        print(f"Gender     : {gender}")
        print(f"Department : {department}")
        print(f"Email      : {email}")
        print(f"Phone      : {phone}")
        print(f"CGPA       : {cgpa}")
        print(f"Created At : {created_at}")

        print("-" * 55)

    except mysql.connector.Error as err:
        print(f"\n❌ Database Error: {err}")

    finally:

        if cursor:
            cursor.close()

        if connection.is_connected():
            connection.close()
#------------------------------------------------------------

def update_student():
    """
    Update an existing student's information.
    """

    print("\n" + "=" * 55)
    print("             UPDATE STUDENT")
    print("=" * 55)

    student_id = int(input("Enter Student ID : "))

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    check_query = """
    SELECT * FROM students
    WHERE student_id = %s
    """

    update_query = """
    UPDATE students
    SET
        name = %s,
        age = %s,
        gender = %s,
        department = %s,
        email = %s,
        phone = %s,
        cgpa = %s
    WHERE student_id = %s
    """

    try:

        # Check whether the student exists
        cursor.execute(check_query, (student_id,))
        student = cursor.fetchone()

        if student is None:
            print("\n❌ Student Not Found.\n")
            return

        print("\nEnter New Student Details\n")

        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        gender = input("Enter Gender : ")
        department = input("Enter Department : ")
        email = input("Enter Email : ")
        phone = input("Enter Phone Number : ")
        cgpa = float(input("Enter CGPA : "))

        values = (
            name,
            age,
            gender,
            department,
            email,
            phone,
            cgpa,
            student_id
        )

        cursor.execute(update_query, values)

        connection.commit()

        print("\n✅ Student Updated Successfully!\n")

    except mysql.connector.Error as err:

        connection.rollback()

        print(f"\n❌ Database Error: {err}\n")

    finally:

        if cursor:
            cursor.close()

        if connection.is_connected():
            connection.close()
#-----------------------------------------------------------

def delete_student():
    """
    Delete a student from the database using Student ID.
    """

    print("\n" + "=" * 55)
    print("             DELETE STUDENT")
    print("=" * 55)

    student_id = int(input("Enter Student ID : "))

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    check_query = """
    SELECT * FROM students
    WHERE student_id = %s
    """

    delete_query = """
    DELETE FROM students
    WHERE student_id = %s
    """

    try:

        # Check whether the student exists
        cursor.execute(check_query, (student_id,))
        student = cursor.fetchone()

        if student is None:
            print("\n❌ Student Not Found.\n")
            return

        confirm = input(
            f"\nAre you sure you want to delete '{student[1]}'? (yes/no): "
        ).strip().lower()

        if confirm != "yes":
            print("\n❌ Deletion Cancelled.\n")
            return

        cursor.execute(delete_query, (student_id,))

        connection.commit()

        print("\n✅ Student Deleted Successfully!\n")

    except mysql.connector.Error as err:

        connection.rollback()

        print(f"\n❌ Database Error: {err}\n")

    finally:

        if cursor:
            cursor.close()

        if connection.is_connected():
            connection.close()