import sqlite3
conn = sqlite3.connect('Exisitingtable_checkconstrain.db')
cursor = conn.cursor()
cursor.execute('select *from employees')
print(cursor.fetchall())
try:
    cursor.execute('INSERT INTO employees (employee_id, employee_name, salary) VALUES (3, "Charlie", -1000);')
except sqlite3.IntegrityError as e:
    print("Error:", e) 
conn.commit()
conn.close()