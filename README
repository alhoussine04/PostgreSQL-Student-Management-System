# Assignment 3: PostgreSQL Student Management System

This Python script provides functionalities to manage student data in a PostgreSQL database. It allows you to create a table for storing student information, insert initial data, retrieve all students, add new students, update student emails, and delete students.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system.
- psycopg2 library installed. You can install it via pip:
  ```
  pip install psycopg2
  ```

- PostgreSQL server installed and running.

## Usage

1. Clone or download the script.

2. Open the script in a text editor.

3. Update the PostgreSQL connection details in the script if needed:
   - `host`: Hostname of your PostgreSQL server (default is "localhost").
   - `database`: Name of your PostgreSQL database (default is "Assignment_3").
   - `user`: PostgreSQL user with access to the database (default is "postgres").
   - `password`: Password for the PostgreSQL user (default is "password").

4. Run the script using Python:
   ```
   python Assignment_3.py
   ```

## Functions

- `createTable()`: Creates a table named "students" in the database if it does not exist already.

- `insertData()`: Inserts initial data into the "students" table.

- `getAllStudents()`: Retrieves and prints all students' information from the "students" table.

- `addStudent(first_name, last_name, email, enrollment_date)`: Adds a new student to the "students" table with the provided information.

- `updateStudentEmail(student_id, new_email)`: Updates the email of a student with the given student ID.

- `deleteStudent(student_id)`: Deletes a student from the "students" table based on the student ID.

## Example Usage

The script demonstrates example usage of the functions:
- It creates the table.
- Inserts initial data.
- Retrieves all students.
- Adds a new student.
- Updates the email of a student.
- Deletes a student.

Please feel free to modify the script according to your specific requirements.

## Note

- Ensure that your PostgreSQL server is running and accessible.
- Handle sensitive information (like passwords) securely, especially in production environments.
- Customize the script as needed for your specific database schema and requirements.
