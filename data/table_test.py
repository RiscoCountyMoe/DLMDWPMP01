from .database import Database
import pandas as pd


class TableTest(Database):
    def __init__(self, db_name):
        super().__init__(db_name)

    def create_test_table(self):
        sql = """CREATE TABLE IF NOT EXISTS test (x FLOAT, y FLOAT);"""
        self.create_table("Test", sql)

    def load_test_data(self, data):
        sql = """INSERT INTO test (x, y) VALUES (?, ?)"""
        values = [(row["x"], row["y"]) for _, row in data.iterrows()]
        self.load_data_to_table("Test", sql, values)

    def load_test_table_to_dataframe(self):
        return self.load_table_to_dataframe("test")