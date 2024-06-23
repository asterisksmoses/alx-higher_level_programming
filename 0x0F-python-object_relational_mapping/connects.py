import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="asterisksmoses",
        password="StrongP@ssword1",
        database="hbtn_0e_0_usa"
    )
    print("Connection successful!")
    connection.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")

