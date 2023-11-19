import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(
    host="cis3368fall.cqbb6zvjwn2s.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Fbp!H#3DTvrpkGwrBnYuSp",
    database="sales"
)

# fetching data from the sales table, storing in a dictionary
cursor = connection.cursor(dictionary = True)

sql = "select * from sales"

cursor.execute(sql)

results = cursor.fetchall()

# Show the User all the available sellers
for row in results:
    print(row['seller'])

print('')
total_sales = 0

# Get User Input for seller, and perform Product and Total Sales Calculations
User_input = input('Enter a seller name: ')
print('Sales Report for', User_input)
for row in results:
    if row['seller'] == User_input:
        total_overall_sales = row['quantity'] * row['price']
        print(f"Product: {row['product']}, Quantity: {row['quantity']}, Price: ${row['price']}, Total: ${total_overall_sales:.2f}")
        total_sales += total_overall_sales

print(f"Total sales for {User_input}: ${total_sales:.2f}")