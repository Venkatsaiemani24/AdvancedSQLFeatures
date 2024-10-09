import sqlite3
conn = sqlite3.connect('naturaljoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT NOT NULL,
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
    INSERT INTO orders (order_id, customer_id, order_date) 
    VALUES (?, ?, ?);
''', [
    (101, 1, '2024-01-15'),  
    (102, 2, '2024-01-20'),  
    (103, 1, '2024-02-05'),  
    (104, 3, '2024-02-10')   
])

cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT * 
    FROM customers
    NATURAL JOIN orders;
''')

print("\n Natural Join \n")
rows = cursor.fetchall()
print("Customer Name | Order ID | Order Date")
print("-------------------------------------")
for row in rows:
    customer_name = row[1]  
    order_id = row[2]       
    order_date = row[3]    
    print(f"{customer_name:<14} | {order_id:<8} | {order_date}")

conn.commit()
conn.close()