from database import Database


class TableTrain(Database):
    def __init__(self, db_name):
        super().__init__(db_name)

    def create_train_table(self):
        sql_train = """CREATE TABLE IF NOT EXISTS train (x FLOAT, y1 FLOAT, y2 FLOAT, y3 FLOAT, y4 FLOAT);"""
        self.create_table(sql_train)

    def load_train_data(self, data):
        sql = """INSERT INTO train (x, y1, y2, y3, y4) VALUES (?, ?, ?, ?, ?);"""
        values = [
            (row["x"], row["y1"], row["y2"], row["y3"], row["y4"])
            for _, row in data.iterrows()
        ]
        self.load_data_to_table(sql, values)
