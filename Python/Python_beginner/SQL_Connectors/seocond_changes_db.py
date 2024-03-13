import mysql.connector
from typing import Union


class MySQL_self:
    def __init__(self, length:int, max:int, min: int, null_attr:None, forign_key: Union[str ,int], primary_key: Union[str ,int], auto_increment:str, int_attr:int, tinyint_attr:int, smallint_attr:int,
                 mediumint_attr:int, bigint_attr:int,
                 decimal_attr:float, float_attr:float, double_attr:float, date_attr:str, time_attr:str,
                 datetime_attr:str, timestamp_attr:str, year_attr:int, char_attr:str, varchar_attr:str, text_attr:str,
                 blob_attr:bytes, enum_attr:str, set_attr:str, boolean_attr:bool)-> None:

        self.null = null_attr
        self.max = max
        self.length = length
        self.int_attr = int_attr
        self.tinyint_attr = tinyint_attr
        self.smallint_attr = smallint_attr
        self.mediumint_attr = mediumint_attr
        self.bigint_attr = bigint_attr
        self.year_attr = year_attr

        self.decimal_attr = decimal_attr
        self.float_attr = float_attr
        self.double_attr = double_attr

        self.date_attr = date_attr
        self.time_attr = time_attr
        self.datetime_attr = datetime_attr
        self.timestamp_attr = timestamp_attr
        self.char_attr = char_attr
        self.varchar_attr = varchar_attr
        self.text_attr = text_attr
        self.enum_attr = enum_attr
        self.set_attr = set_attr

        self.blob_attr = blob_attr
        self.boolean_attr = boolean_attr




    def sql_data(self,anzahl_columns:int,anzahl_rows:int)-> None:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host='Localhost',#Localhost
            #port='3306',
            user='root',#your_username
            password='password', # your_password
            database='feraidon' #your_database
        )

        cursor = connection.cursor()
        # Beispiel: Eine Tabelle erstellen und Daten einfügen
        #cursor.execute("INSERT INTO feri (id) VALUES ('1')")
        table_name = input(f"Enter your table name:")
        new_column = str(input(f"add a column(name): ")).lower()
        number_of_comulmn = int(input())
        anzahl_columns = new_column * number_of_comulmn
        list_columns = []
        list_columns.append(anzahl_columns)
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, {list_columns} VARCHAR(255))"

        table_list = [] # a list that can keep the current  list thet recently created
        table_list.append(table_name)

        cursor.execute(sql)
        connection.commit()

        name = input("the value name: ")
        insert_sql = f"INSERT INTO {table_list} (name) VALUES ('{name}')"
        cursor.execute(insert_sql)



        # cursor.execute("INSERT INTO feri (name) VALUES ('reza')")
        # cursor.execute("INSERT INTO feri (name) VALUES ('hasan')")
        # cursor.execute("INSERT INTO feri (name) VALUES ('goli')")
        connection.commit()  # Änderungen in der Datenbank speichern



instance = MySQL_self()
instance.sql_data()












#
# try:
#     if connection.is_connected():
#         print("Connected to MySQL")
#
#         # Create a cursor
#         #cursor = connection.cursor()
#
#         # Execute a SQL query
#         sql4 = "SELECT * FROM %s"
#         cursor.execute(sql4, table_name)
#
#         # Fetch and print results
#         for row in cursor.fetchall():
#             print(row)
#
# except mysql.connector.Error as e:
#     print(f"Error: {e}")
#
# finally:
#     # Close the cursor and connection
#     if 'cursor' in locals():
#         cursor.close()
#     if connection.is_connected():
#         connection.close()
#         print("MySQL connection closed")
#



# Close the cursor and connection when done
# cursor.close()
# connection.close()