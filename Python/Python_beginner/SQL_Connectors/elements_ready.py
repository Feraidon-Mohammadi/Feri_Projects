
import mysql.connector
from typing import Union


class MySQL_self:


    def sql_data(self):



        # Connect to MySQL
        connection = mysql.connector.connect(
            host='Localhost'  ,  # Localhost
            # port='3306',
            user='root'  ,  # your_username
            password='password', # your_password
            database='feraidon'  # your_database
        )

        cursor = connection.cursor()


        type_column = input("Type of the column: ")
        max = input("maximum digit: ")
        table_name = input(f"Enter your table name:")
        column_name = input(f"column name: ")
        create_column_first_type = f"{type_column}({max})"



        alter_table_sql = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {create_column_first_type}"
        cursor.execute(alter_table_sql)
        connection.commit()



        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, {column_name} {create_column_first_type})"
        cursor.execute(sql)
        connection.commit()



        name = input("insert value to that column: ")
        insert_sql = f"INSERT INTO {table_name} ({column_name}) VALUES ('{name}')"
        cursor.execute(insert_sql)

        # cursor.execute("INSERT INTO feri (name) VALUES ('reza')")
        connection.commit()  # Änderungen in der Datenbank speichern





instance = MySQL_self()
instance.sql_data()











































"""
class SQL_test:
    def __init__(self, length, max, min, null_attr, forign_key, primary_key, auto_increment, int_attr, tinyint_attr, smallint_attr,
                 mediumint_attr, bigint_attr,
                 decimal_attr, float_attr, double_attr, date_attr, time_attr,
                 datetime_attr, timestamp_attr, year_attr, char_attr, varchar_attr, text_attr,
                 blob_attr, enum_attr, set_attr, boolean_attr):

"""
"""
# with value annotations

def __init__(self, length:int, max:int, min: int, null_attr:None, forign_key: Union[str ,int], primary_key: Union[str ,int], auto_increment:str, int_attr:int, tinyint_attr:int, smallint_attr:int,
                 mediumint_attr:int, bigint_attr:int,
                 decimal_attr:float, float_attr:float, double_attr:float, date_attr:str, time_attr:str,
                 datetime_attr:str, timestamp_attr:str, year_attr:int, char_attr:str, varchar_attr:str, text_attr:str,
                 blob_attr:bytes, enum_attr:str, set_attr:str, boolean_attr:bool)-> None:






"""





"""
new -> 
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





olds 


        self.null = None
        self.max = int(input())
        self.length = int(input())
        self.int_attr = int(input())
        self.tinyint_attr = int(input())
        self.smallint_attr = int(input())
        self.mediumint_attr = int(input())
        self.bigint_attr = int(input())
        self.year_attr = int(input())

        self.decimal_attr = float(input())
        self.float_attr = float(input())
        self.double_attr = float(input())

        self.date_attr = str(input())
        self.time_attr = str(input())
        self.datetime_attr = str(input())
        self.timestamp_attr = str(input())
        self.char_attr = str(input())
        self.varchar_attr = str(input())
        self.text_attr = str(input())
        self.enum_attr = str(input())
        self.set_attr = str(input())


        self.blob_attr = bytes(input())
        self.boolean_attr = bool(input())









"""


"""











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


        # def list_columns():
        #     columns = []
        #     while True:
        #         column_name = input("Enter a column name (or press Enter to finish): ")
        #         if not column_name:
        #             break
        #         columns.append(f"{column_name} VARCHAR(255)")
        #     return ", ".join(columns)
        # 












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
        new_column = str(input(f"add a column(name): "))
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"

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
cursor.close()
connection.close()












































"""