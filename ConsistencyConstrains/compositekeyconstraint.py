import sqlite3
conn = sqlite3.connect('compositekeyconstraint.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE students (student_id INTEGER PRIMARY KEY,student_name TEXT NOT NULL);''')
cursor.execute('''CREATE TABLE courses (course_id INTEGER PRIMARY KEY,course_name TEXT NOT NULL);''')
# Creating the student_courses table with a composite key (student_id, course_id)
cursor.execute('''CREATE TABLE student_courses (
    student_id INTEGER,course_id INTEGER,PRIMARY KEY (student_id, course_id),FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id));''')
cursor.execute('INSERT INTO students (student_id, student_name) VALUES (1, "Alice");')
cursor.execute('INSERT INTO students (student_id, student_name) VALUES (2, "Bob");')
cursor.execute('INSERT INTO courses (course_id, course_name) VALUES (101, "Mathematics");')
cursor.execute('INSERT INTO courses (course_id, course_name) VALUES (102, "Physics");')
cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (1, 101);')
cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (2, 102);')

print("\n Current data in the student_courses table:")
cursor.execute('SELECT * FROM student_courses')
for row in cursor.fetchall():
    print(row)
# Try to insert duplicate data with same student_id and course_id combination
try:
    cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (1, 101);') 
except sqlite3.IntegrityError as e:
    print("Error:", e) 
# Trying to insert another valid data with different student_id and course_id combination
cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (1, 102);')
conn.commit()
conn.close()