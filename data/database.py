import sqlite3
import pandas as pd


class Database:
    DB_NAME = "DLMDWPMP01.db"

    def __init__(self, db_name):
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(Database.DB_NAME)
            print("Verbindung zur Datenbank erfolgreich")
        except sqlite3.Error as err:
            print(err)

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print("Verbindung zur Datenbank geschlossen")

    def create_table(self, table_name, sql):
        try:
            with sqlite3.connect(Database.DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                print(f"Tabelle '{table_name}' erfolgreich erstellt")
        except sqlite3.Error as err:
            print(err)
        finally:
            self.disconnect()

    def load_data_to_table(self, table_name, sql, values):
        try:
            with sqlite3.connect(Database.DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.executemany(sql, values)
            print(f"Datensatz '{table_name}' erfolgreich geladen")
        except sqlite3.Error as err:
            print(err)
        finally:
            self.disconnect()

    def load_table_to_dataframe(self, table_name):
        try:
            with sqlite3.connect(Database.DB_NAME) as conn:
                sql = f"SELECT * FROM {table_name}"
                df = pd.read_sql_query(sql, conn)
                return df
        except sqlite3.Error as err:
            print(err)
