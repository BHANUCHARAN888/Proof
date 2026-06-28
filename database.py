import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def connect_db():
    """
    Connect to MySQL Database
    Returns:
        connection object
    """

    try:
        connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

        if connection.is_connected():
            print("✅ Connected to MySQL Successfully!")

        return connection

    except mysql.connector.Error as err:
        print("❌ Error:", err)
        return None


def create_students_table():

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS students(
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        gender VARCHAR(10),
        department VARCHAR(50),
        email VARCHAR(100) UNIQUE,
        phone VARCHAR(15),
        cgpa DECIMAL(4,2),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    try:
        cursor.execute(create_table_query)
        connection.commit()

        print("✅ Students table is ready.")

    except mysql.connector.Error as err:
        print("❌ Error:", err)

    finally:
        cursor.close()
        connection.close()
        print("🔒 Connection Closed.")

