import mysql.connector






# Connect to MySQL
connection = mysql.connector.connect(
    host='Localhost',#Localhost
    #port='3306',
    user='root',#your_username
    password='password', # your_password
    database='feraidon' #your_database
)

cursor = connection.cursor()

table_name = str(input(f"Enter your table name: "))
sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"

cursor.execute(sql)
connection.commit()

#table_list = [] # a list that can keep the current  list thet recently created
#table_list.append(table_name)


name = input("the value name: ")
insert_sql = f"INSERT INTO {table_name} (name) VALUES ('{name}')"
cursor.execute(insert_sql)



# cursor.execute("INSERT INTO feri (name) VALUES ('reza')")
# cursor.execute("INSERT INTO feri (name) VALUES ('hasan')")
# cursor.execute("INSERT INTO feri (name) VALUES ('goli')")
connection.commit()  # Änderungen in der Datenbank speichern
cursor.close()
connection.close()



