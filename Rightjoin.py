import sqlite3
conn = sqlite3.connect('productsuppliers.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE suppliers (
        supplier_id INTEGER PRIMARY KEY,
        supplier_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE product_suppliers (
        product_id INTEGER,
        supplier_id INTEGER,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
    );
''')

cursor.executemany('''
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Laptop'),
    (2, 'Smartphone'),
    (3, 'Tablet'),
    (4, 'Camera'),
    (5, 'Smartwatch')
])

cursor.execute("Select *from products")
print("\n Products Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
 
cursor.executemany('''
    INSERT INTO suppliers (supplier_id, supplier_name) 
    VALUES (?, ?);
''', [
    (1, 'Tech Supplies Inc.'),
    (2, 'Gadget Warehouse'),
    (3, 'Smart Devices Ltd.')
])

cursor.execute("Select *from suppliers")
print("\n Suppliers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.executemany('''
    INSERT INTO product_suppliers (product_id, supplier_id) 
    VALUES (?, ?);
''', [
    (1, 1),  
    (2, 1),  
    (3, 2), 
    (4, 3)  
])

cursor.execute("Select *from product_suppliers")
print("\n Suppliers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT products.product_name, suppliers.supplier_name  FROM products
    LEFT JOIN product_suppliers ON products.product_id = product_suppliers.product_id
    LEFT JOIN suppliers ON product_suppliers.supplier_id = suppliers.supplier_id;
''')

rows = cursor.fetchall()
print("Right Join")
for row in rows:
    print(row)

conn.commit()
conn.close()
