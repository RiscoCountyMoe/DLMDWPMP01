from .database import Database
import pandas as pd


class ResultTable(Database):
    def __init__(self, db_name):
        super().__init__(db_name)

    def create_test_table(self):
        sql = """CREATE TABLE IF NOT EXISTS results (X VARCHAR(20), Y VARCHAR(20), 'Deviation' VARCHAR(20), 'Ideal Function' VARCHAR(20));"""
        self.create_table("Results", sql)