import sqlite3

class Database:
   DB_NAME = 'test.db'

   def __init__(self):
      self.conn = None

   def connect(self):
      try:
        self.conn = sqlite3.connect(Database.DB_NAME)
        print("Verbindung zur Datenbank erfolgreich")
      except sqlite3.Error as e:
            print(e)

   def create_table(self, sql):
      cursor = self.conn.cursor()
      cursor.execute(sql)

   def load_data_to_table(self, sql, values):
      cursor = self.conn.cursor()
      cursor.executemany(sql, values)
      self.conn.commit()