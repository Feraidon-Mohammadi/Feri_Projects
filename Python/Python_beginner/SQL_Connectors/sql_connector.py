import mysql.connector
from typing import Union
import pandas as pd

class MySQL_self:


    def sql_data(self):

        # Connect to MySQL
        connection = mysql.connector.connect(
            host='Localhost',#Localhost
            #port='3306',
            user='root',#your_username
            password='password', # your_password
            database='feraidon' #your_database
        )
        cursor = connection.cursor()





        # variablen for input data
        type_column = input("Type of the column: ")
        max = input("maximum digit: ")
        table_name = input(f"Select table name or create new: ")
        create_column_first_type = f"{type_column}({max})"
        #


        # create a table with an id column with auto increment prime
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY)"
        cursor.execute(sql)
        connection.commit()
        #







        # insert values in to the specifiy columns
        # name = input("insert value to that column: ")
        # insert_sql = f"INSERT INTO {table_name} ({column_name}) VALUES ('{name}')"
        # cursor.execute(insert_sql)

        # cursor.execute("INSERT INTO feri (name) VALUES ('reza')")
        # connection.commit()  # Änderungen in der Datenbank speichern







        def create_colum():

            # create multiple columns
            while True:
                column_name = input("Enter a column name (or press Enter to finish): ")
                name = input("insert value to that column: ")
                if not column_name:
                    break
                alter_table_sql = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {create_column_first_type}"
                cursor.execute(alter_table_sql)


                insert_sql = f"INSERT INTO {table_name} ({column_name}) VALUES ('{name}')"
                cursor.execute(insert_sql)
                connection.commit()
            return connection.commit()
            #
        create_colum()




        """
        # show data in consule and fetch data ,and put data from sql in to the excel file ,
        def selection():
            list_data = []
            select_table = f"SELECT * FROM {table_name} "
            cursor.execute(select_table)
            # Fetch the results

            # Retrieve column names from the cursor's description
            column_names = [desc[0] for desc in cursor.description]
            print( column_names)

            for row in cursor.fetchall():
                list_data.append(row)

            # Print the results
            for data in list_data:
                print(data)


            # put data to the excel
            df = pd.DataFrame(list_data, columns=column_names)
            # Specify the Excel file path where you want to save the data
            excel_file_path = "C:\\Users\\admin\\PycharmProjects\\Py_beginner\\SQL_Connector\\output_data.xlsx"
            # Save the data to an Excel file
            df.to_excel(excel_file_path, index=False)
            # Print a message to indicate where the data is saved
            print(f"Data has been saved to '{excel_file_path}'")

        selection()
        """


        def excel_to_sql():
            excel_file_path = "C:\\Users\\admin\\PycharmProjects\\Py_beginner\\SQL_Connector\\output_data.xlsx"

            # Read data from the Excel file into a DataFrame
            df = pd.read_excel(excel_file_path)

            # Iterate through the DataFrame and insert rows into the database
            for index, row in df.iterrows():
                # Assuming 'your_table_name' is the name of the target table in your database
                insert_sql = f"INSERT INTO your_table_name (column1, column2, column3, ...) VALUES (%s, %s, %s, ...)"
                cursor.execute(insert_sql, tuple(row))
        return connection.commit()






        cursor.close()
        connection.close()

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
#cursor.close()
#connection.close()