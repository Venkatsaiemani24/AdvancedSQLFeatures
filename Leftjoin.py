import sqlite3
connection = sqlite3.connect('CustomerOrders.db')
cursor = connection.cursor()
# Creating customers table
cursor.execute('''CREATE TABLE IF NOT EXISTS customers ( customer_id INTEGER PRIMARY KEY,customer_name TEXT NOT NULL);''')
# Creating the orders table
cursor.execute('''CREATE TABLE IF NOT EXISTS orders ( order_id INTEGER PRIMARY KEY,customer_id INTEGER,
               product_name TEXT NOT NULL,FOREIGN KEY (customer_id) REFERENCES customers(customer_id));''')
# Inserting records into customer table 
cursor.executemany('''INSERT INTO customers (customer_id, customer_name) VALUES (?, ?);''', [
    (1, 'John Doe'),
    (2, 'Jane Smith'),
    (3, 'Alice Johnson'),
    (4, 'Bob Brown'),
    (5, 'Mary Williams')
])
# Selecting the Records from customers table
cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Inserting records into the orders table
cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, product_name) VALUES (?, ?, ?);''', [
    (101, 1, 'Laptop'),
    (102, 2, 'Smartphone'),
    (103, 1, 'Headphones'),
    (104, 3, 'Tablet'),
    (105, 4, 'Smartwatch'),
    (106, 5, 'Camera'),
    (107, 3, 'Laptop'),
    (108, 2, 'Headphones')
])
# Selecting the Records from orders table
cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.execute('''SELECT customers.customer_name, orders.product_name FROM customers
                  LEFT JOIN orders ON customers.customer_id = orders.customer_id;''')
print("\n Left Join \n")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()