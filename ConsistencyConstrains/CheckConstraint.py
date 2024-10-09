import sqlite3
conn = sqlite3.connect('checkconstraint.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE products ( product_id INTEGER PRIMARY KEY, product_name TEXT NOT NULL, price REAL NOT NULL CHECK (price > 0));''')

cursor.execute(''' INSERT INTO products (product_id, product_name, price) VALUES (1, 'Laptop', 999.99);''')
cursor.execute('''INSERT INTO products (product_id, product_name, price) VALUES (2, 'Smartphone', 0.1);''')

cursor.execute('''select *from products''')
print(cursor.fetchall())

# Trying to insert price =  Zero to raise a error condition
cursor.execute('''INSERT INTO products (product_id, product_name, price) VALUES (2, 'Smartphone', 0);''')

conn.commit()
conn.close()