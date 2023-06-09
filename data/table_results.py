from .database import Database
import pandas as pd


class ResultTable(Database):
    def __init__(self, db_name):
        super().__init__(db_name)

    def create_result_table(self):
        sql = """CREATE TABLE IF NOT EXISTS results (X FLOAT, Y FLOAT, 'Function' VARCHAR(20), 'Deviation' FLOAT);"""
        self.create_table("Results", sql)

    def load_result_data(self, data):
        sql = """INSERT INTO results (x, y, 'function', 'deviation') VALUES (?, ?, ?, ?)"""
        values = [
            (row["x"], row["y"], row["function"], row["deviation"])
            for _, row in data.iterrows()
        ]
        self.load_data_to_table("Results", sql, values)

    def load_result_table_to_dataframe(self):
        return self.load_table_to_dataframe("results")
