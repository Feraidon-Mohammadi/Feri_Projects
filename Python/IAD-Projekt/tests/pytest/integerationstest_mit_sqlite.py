# integerationstest mit sqlite

import sqlite3
import unittest

class TestSQLiteIntegration(unittest.TestCase):
    def setUp(self):
        # Verbindung zur SQLite-Datenbank herstellen (wird im Speicher erstellt, für den Test)
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        
        # Tabelle für den Test erstellen
        self.cursor.execute('''CREATE TABLE users
                               (id INTEGER PRIMARY KEY, name TEXT NOT NULL)''')
        self.connection.commit()
    
    
    def tearDown(self):
        # Schließen der Verbindung am Ende jedes Tests
        self.connection.close()
    
    
    def test_user_insertion_and_retrieval(self):
        # Einen Nutzer in die Datenbank einfügen
        self.cursor.execute("INSERT INTO users (name) VALUES (?)", ('TestUser',))
        self.connection.commit()
        
        # Nutzer abrufen und überprüfen, ob die Daten korrekt eingefügt wurden
        self.cursor.execute("SELECT * FROM users WHERE name=?", ('TestUser',))
        user = self.cursor.fetchone()
        
        self.assertIsNotNone(user)  # Überprüfen, ob ein Nutzer gefunden wurde
        self.assertEqual(user[1], 'TestUser')  # Überprüfen des Namens des Nutzers

if __name__ == '__main__':
    unittest.main()
