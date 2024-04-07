import mysql.connector

# Replace these with your actual MySQL server details
host = "your_mysql_host"
user = "your_mysql_user"
password = "your_mysql_password"
database = "your_mysql_database"

# Create a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor to interact with the database
cursor = connection.cursor()

# Example: Execute a simple query
cursor.execute("SELECT * FROM your_table")
result = cursor.fetchall()

# Example: Insert data into a table
insert_query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
data_to_insert = ("value1", "value2")
cursor.execute(insert_query, data_to_insert)

# Commit changes and close the connection
connection.commit()
connection.close()