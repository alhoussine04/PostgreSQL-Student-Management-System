import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="Assignment_3",
    user="postgres",
    password="password"
)

# Create a cursor object
cur = conn.cursor()

# Function to create the students table
def createTable():
    create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
)
"""
    cur.execute(create_table_query)
    conn.commit()

# Function to insert the initial data
def insertData():
    insert_data_query = """
INSERT INTO students (first_name, last_name, email, enrollment_date)
VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
"""
    cur.execute(insert_data_query)
    conn.commit()

# Function to retrieve all students
def getAllStudents():
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    for student in students:
        print(student)

# Function to add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    insert_query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
    cur.execute(insert_query, (first_name, last_name, email, enrollment_date))
    conn.commit()
    print("Student added successfully!", (first_name, last_name, email, enrollment_date))

# Function to update a student's email
def updateStudentEmail(student_id, new_email):
    update_query = "UPDATE students SET email = %s WHERE student_id = %s"
    cur.execute(update_query, (new_email, student_id))
    conn.commit()
    print("Student email updated successfully!", student_id)

# Function to delete a student
def deleteStudent(student_id):
    delete_query = "DELETE FROM students WHERE student_id = %s"
    cur.execute(delete_query, (student_id,))
    conn.commit()
    print("Student deleted successfully!", student_id)

# Example usage
createTable()
getAllStudents()
insertData()
getAllStudents()
addStudent("Alice", "Wonder", "alice.wonder@example.com", "2023-09-03")
getAllStudents()
updateStudentEmail(1, "updated.john@example.com")
getAllStudents()
deleteStudent(3)
getAllStudents()

# Close the database connection
cur.close()
conn.close()
