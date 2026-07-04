"""
==========================================
Create Database
==========================================
"""

import sqlite3
import random

from datetime import datetime
from datetime import timedelta

conn = sqlite3.connect(

    "sample_database/sales.db"

)

cursor = conn.cursor()

# -----------------------------------
# Drop Tables
# -----------------------------------

cursor.execute("DROP TABLE IF EXISTS Orders")

cursor.execute("DROP TABLE IF EXISTS Customers")

cursor.execute("DROP TABLE IF EXISTS Products")

cursor.execute("DROP TABLE IF EXISTS Employees")

# -----------------------------------
# Customers
# -----------------------------------

cursor.execute("""

CREATE TABLE Customers(

CustomerID INTEGER PRIMARY KEY,

CustomerName TEXT,

Gender TEXT,

Age INTEGER,

City TEXT,

State TEXT

)

""")

# -----------------------------------
# Products
# -----------------------------------

cursor.execute("""

CREATE TABLE Products(

ProductID INTEGER PRIMARY KEY,

ProductName TEXT,

Category TEXT,

Price REAL

)

""")

# -----------------------------------
# Employees
# -----------------------------------

cursor.execute("""

CREATE TABLE Employees(

EmployeeID INTEGER PRIMARY KEY,

EmployeeName TEXT,

Department TEXT

)

""")

# -----------------------------------
# Orders
# -----------------------------------

cursor.execute("""

CREATE TABLE Orders(

OrderID INTEGER PRIMARY KEY,

CustomerID INTEGER,

ProductID INTEGER,

EmployeeID INTEGER,

Quantity INTEGER,

Total REAL,

OrderDate TEXT,

FOREIGN KEY(CustomerID)
REFERENCES Customers(CustomerID),

FOREIGN KEY(ProductID)
REFERENCES Products(ProductID),

FOREIGN KEY(EmployeeID)
REFERENCES Employees(EmployeeID)

)

""")

# -----------------------------------
# Customers
# -----------------------------------

customers = [

("Rahul","Male",28,"Hyderabad","Telangana"),

("Priya","Female",24,"Chennai","Tamil Nadu"),

("Ajay","Male",23,"Visakhapatnam","Andhra Pradesh"),

("Sneha","Female",30,"Bangalore","Karnataka"),

("Arjun","Male",35,"Mumbai","Maharashtra"),

("Kiran","Male",27,"Pune","Maharashtra"),

("Divya","Female",31,"Delhi","Delhi"),

("Anjali","Female",29,"Kolkata","West Bengal"),

("Vikram","Male",38,"Ahmedabad","Gujarat"),

("Neha","Female",26,"Jaipur","Rajasthan")

]

cursor.executemany("""

INSERT INTO Customers

(CustomerName,Gender,Age,City,State)

VALUES(?,?,?,?,?)

""", customers)

# -----------------------------------
# Products
# -----------------------------------

products = [

("Laptop","Electronics",65000),

("Phone","Electronics",25000),

("Tablet","Electronics",30000),

("TV","Electronics",55000),

("Headphones","Accessories",2500),

("Mouse","Accessories",900),

("Keyboard","Accessories",1500),

("Printer","Office",12000),

("Monitor","Office",18000),

("Camera","Electronics",45000)

]

cursor.executemany("""

INSERT INTO Products

(ProductName,Category,Price)

VALUES(?,?,?)

""", products)

# -----------------------------------
# Employees
# -----------------------------------

employees = [

("Ajay","Sales"),

("Ramesh","Sales"),

("Priya","Marketing"),

("Kiran","Support"),

("Suresh","Sales")

]

cursor.executemany("""

INSERT INTO Employees

(EmployeeName,Department)

VALUES(?,?)

""", employees)

# -----------------------------------
# Orders
# -----------------------------------

start = datetime(2025,1,1)

orders = []

for _ in range(500):

    customer = random.randint(1,10)

    product = random.randint(1,10)

    employee = random.randint(1,5)

    quantity = random.randint(1,5)

    cursor.execute(

        "SELECT Price FROM Products WHERE ProductID=?",

        (product,)

    )

    price = cursor.fetchone()[0]

    total = price * quantity

    date = start + timedelta(

        days=random.randint(0,500)

    )

    orders.append(

        (

            customer,

            product,

            employee,

            quantity,

            total,

            date.strftime("%Y-%m-%d")

        )

    )

cursor.executemany("""

INSERT INTO Orders

(

CustomerID,

ProductID,

EmployeeID,

Quantity,

Total,

OrderDate

)

VALUES

(?,?,?,?,?,?)

""", orders)

conn.commit()

conn.close()

print("Database Created Successfully")