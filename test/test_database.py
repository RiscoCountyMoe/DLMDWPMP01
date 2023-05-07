import sqlite3
import unittest
from data.database import Database


class TestDatabase(unittest.TestCase):
    DB_NAME = "DLMDWPMP01.db"

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
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, column TEXT)"

        self.db.create_table(table_name, sql)

        with sqlite3.connect(TestDatabase.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (table_name,),
            )
            result = cursor.fetchone()

        self.assertIsNotNone(result)

    def test_load_data_to_table(self):
        table_name = "test_table"
        sql = f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, function TEXT)"

        self.db.create_table(table_name, sql)

        data = [(1, "y1"), (2, "y2"), (3, "y3")]

        self.db.load_data_to_table(
            table_name, f"INSERT INTO {table_name} VALUES (?, ?)", data
        )

        with sqlite3.connect(TestDatabase.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            result = cursor.fetchall()

        expected = [(1, "y1"), (2, "y2"), (3, "y3")]

        self.assertEqual(result, expected)

    def test_load_table_to_dataframe(self):
        table_name = "test_table"
        sql = f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, function TEXT)"

        self.db.create_table(table_name, sql)

        data = [(1, "y1"), (2, "y2"), (3, "y3")]

        self.db.load_data_to_table(
            table_name, f"INSERT INTO {table_name} VALUES (?, ?)", data
        )

        df = self.db.load_table_to_dataframe(table_name)

        expected_columns = ["id", "function"]
        expected_values = [(1, "y1"), (2, "y2"), (3, "y3")]

        self.assertEqual(list(df.columns), expected_columns)
        self.assertEqual(list(df.itertuples(index=False, name=None)), expected_values)
