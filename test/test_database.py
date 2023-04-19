import sqlite3
import unittest
from data.database import Database

class TestDatabase(unittest.TestCase):
    DB_NAME = "test.db"

    def setUp(self):
        self.db = Database(TestDatabase.DB_NAME)

    def tearDown(self):
        self.db.disconnect()
        conn = sqlite3.connect(TestDatabase.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test_table")
        conn.commit()
        conn.close()

    def test_create_table(self):
        table_name = "test_table"
        sql = f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, name TEXT)"

        # Call the method to create the table
        self.db.create_table(table_name, sql)

        # Open a new connection to check if the table was created
        with sqlite3.connect(TestDatabase.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
            result = cursor.fetchone()

        self.assertIsNotNone(result) # table exists in the database

