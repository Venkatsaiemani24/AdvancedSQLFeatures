import sqlite3
conn = sqlite3.connect('employees_departments.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name TEXT NOT NULL,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(department_id)
    );
''')

cursor.execute('''
    CREATE TABLE departments (
        department_id INTEGER PRIMARY KEY,
        department_name TEXT NOT NULL
    );
''')

cursor.executemany('''
    INSERT INTO departments (department_id, department_name) 
    VALUES (?, ?);
''', [
    (1, 'HR'),
    (2, 'Engineering'),
    (3, 'Marketing'),
    (4, 'Sales')
])

cursor.execute("Select *from departments")
print("\n Departments Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.executemany('''
    INSERT INTO employees (employee_id, employee_name, department_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'John Doe', 1),      
    (2, 'Jane Smith', 2),     
    (3, 'Alice Johnson', None),  
    (4, 'Bob Brown', 3)      
])

cursor.execute("Select *from employees")
print("\n Employees Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT employees.employee_name, departments.department_name
    FROM employees
    LEFT JOIN departments ON employees.department_id = departments.department_id

    UNION

    SELECT employees.employee_name, departments.department_name
    FROM departments
    LEFT JOIN employees ON employees.department_id = departments.department_id;
''')

print("\n Full Outer Join \n")
rows = cursor.fetchall()
for row in rows:
    print(rows)

conn.commit()
conn.close()