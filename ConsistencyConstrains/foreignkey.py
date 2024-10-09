import sqlite3
conn = sqlite3.connect('foreignkey.db')
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')
cursor.execute('''CREATE TABLE students ( student_id INTEGER PRIMARY KEY, student_name TEXT NOT NULL);''')
cursor.execute(''' CREATE TABLE courses ( course_id INTEGER, course_name TEXT NOT NULL, department_id INTEGER, PRIMARY KEY (course_id, department_id)); ''')
cursor.execute('''CREATE TABLE student_courses (
    student_id INTEGER,
    course_id INTEGER,
    department_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id, department_id) REFERENCES courses(course_id, department_id) ON DELETE CASCADE,
    PRIMARY KEY (student_id, course_id, department_id));''')

cursor.execute('INSERT INTO students (student_id, student_name) VALUES (1, "Alice");')
cursor.execute('INSERT INTO students (student_id, student_name) VALUES (2, "Bob");')
cursor.execute('INSERT INTO courses (course_id, course_name, department_id) VALUES (101, "Database Systems", 1);')
cursor.execute('INSERT INTO courses (course_id, course_name, department_id) VALUES (102, "Algorithms", 1);')
cursor.execute('INSERT INTO student_courses (student_id, course_id, department_id) VALUES (1, 101, 1);')
cursor.execute('INSERT INTO student_courses (student_id, course_id, department_id) VALUES (2, 102, 1);')

print("\nCurrent data in the student_courses table:")
cursor.execute('SELECT * FROM student_courses')
for row in cursor.fetchall():
    print(row)

# Trying to insert invalid data to student_id which  doesn't exist
cursor.execute('INSERT INTO student_courses (student_id, course_id, department_id) VALUES (3, 101, 1);')
# Trying to insert invalid data to course_id which doesn't exist
cursor.execute('INSERT INTO student_courses (student_id, course_id, department_id) VALUES (1, 103, 1);')

conn.commit()
conn.close()