import sqlite3
conn = sqlite3.connect('aggregationjoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
''')

cursor.executemany('''
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'John Doe'),
    (2, 'Jane Smith'),
    (3, 'Alice Johnson')
])

cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, product_id) 
    VALUES (?, ?, ?);
''', [
    (101, 1, 1),  
    (102, 1, 2),  
    (103, 2, 1), 
    (104, 2, 3),  
    (105, 3, 2),  
    (106, 3, 4)  
])

cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT customers.customer_name, COUNT(orders.product_id) AS total_products_ordered
    FROM customers
    JOIN orders ON customers.customer_id = orders.customer_id
    GROUP BY customers.customer_name;
''')

rows = cursor.fetchall()

print("\n Customer Name | Total Products Ordered")
print("--------------------------------------")
for row in rows:
    customer_name = row[0]
    total_products_ordered = row[1]
    print(f"{customer_name:<13} | {total_products_ordered}")
conn.commit()
conn.close()