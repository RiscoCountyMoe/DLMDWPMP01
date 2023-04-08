import os
import sys
from data.database import Database
from data.table_train import TableTrain
import numpy as np
import pandas as pd

# create and connect to database
db = Database()
db.connect()

# create table "train" and insert data from file
train_df = pd.read_csv("train.csv")
db_train = TableTrain(Database.DB_NAME)
db_train.connect()
db.create_train_table()
db_train.load_train_data(train_df)
