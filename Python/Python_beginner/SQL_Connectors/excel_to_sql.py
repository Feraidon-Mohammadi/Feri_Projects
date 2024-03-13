import mysql.connector
from typing import Union
import pandas as pd


class MySQL_self:
    def sql_data(self):
        # Connect to MySQL
        connection = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='password',
            database='feraidon'
        )
        cursor = connection.cursor()

        type_column = input("Type of the column: ")
        max = input("maximum digit: ")
        table_name = input("Select table name or create a new one: ")
        create_column_first_type = f"{type_column}({max})"

        # Create a table with an id column with auto-increment primary key
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY)"
        cursor.execute(sql)
        connection.commit()

        self.create_columns_and_insert_data(connection, cursor, table_name, create_column_first_type)
        self.excel_to_sql(table_name, cursor, connection)

    def create_columns_and_insert_data(self, connection, cursor, table_name, create_column_first_type):
        while True:
            column_name = input("Enter a column name (or press Enter to finish): ")
            if not column_name:
                break
            alter_table_sql = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {create_column_first_type}"
            cursor.execute(alter_table_sql)

            name = input(f"Insert value for the column '{column_name}': ")
            insert_sql = f"INSERT INTO {table_name} ({column_name}) VALUES ('{name}')"
            cursor.execute(insert_sql)
            connection.commit()

    def excel_to_sql(self, table_name, cursor, connection):
        excel_file_path = "C:\\Users\\admin\\PycharmProjects\\Py_beginner\\SQL_Connector\\output_data.xlsx"

        # Read data from the Excel file into a DataFrame
        df = pd.read_excel(excel_file_path)

        # Get the column names from the DataFrame and create a string
        columns = list(df.columns)
        column_string = ", ".join(columns)  # Create a string with column names

        # Construct the SQL statement and parameter placeholders dynamically
        insert_sql = f"INSERT INTO {table_name} ({column_string}) VALUES ({', '.join(['%s'] * len(columns))})"

        # Iterate through the DataFrame and insert rows into the database
        for index, row in df.iterrows():
            cursor.execute(insert_sql, tuple(row))

        connection.commit()
        cursor.close()
        connection.close()

instance = MySQL_self()
instance.sql_data()










