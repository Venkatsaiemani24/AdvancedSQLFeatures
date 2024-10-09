import sqlite3
conn = sqlite3.connect('violatingforeignkeyconstraint.db')
cursor = conn.cursor()

# Enabling foreign key constrain
cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute('''CREATE TABLE customers (customer_id INTEGER PRIMARY KEY, customer_name TEXT NOT NULL);''')
cursor.execute('''CREATE TABLE orders ( order_id INTEGER PRIMARY KEY, customer_id INTEGER, order_date TEXT, FOREIGN KEY (customer_id) REFERENCES customers(customer_id));''')
cursor.execute(''' INSERT INTO customers (customer_id, customer_name) VALUES (1, 'John Doe');''')
cursor.execute('''INSERT INTO customers (customer_id, customer_name) VALUES (2, 'Jane Smith');''')
cursor.execute('''select *from customers;''')
print(cursor.fetchall())

cursor.execute('''INSERT INTO orders (order_id, customer_id, order_date) VALUES (1, 5, '2024-10-09');''')  
cursor.execute('''select *from orders;''')
print(cursor.fetchall())

conn.commit()
conn.close()