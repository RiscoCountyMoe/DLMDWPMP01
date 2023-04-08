from .database import Database


class TableTest(Database):
    def __init__(self, db_name):
        super().__init__(db_name)

    def create_test_table(self):
        sql= '''CREATE TABLE IF NOT EXISTS test (x FLOAT, y FLOAT);'''
        self.create_table(sql)

    def load_test_data(self, data):
        sql = '''INSERT INTO test (x, y) VALUES (?, ?)'''
        values = [(row['x'], row['y']) for _, row in data.iterrows()]
        self.load_data_to_table(sql, values)
