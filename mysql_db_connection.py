import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="@python@", database="miracle"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers LIMIT 5 OFFSET 9"

mycursor.execute(sql)

result = mycursor.fetchall()

for row in result:
    print("\n", row)
