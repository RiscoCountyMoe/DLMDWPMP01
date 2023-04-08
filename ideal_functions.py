import os
import sys
from data.table_train import TableTrain
from data.database import Database
import numpy as np
import pandas as pd

# create and connect to database
db = Database(Database.DB_NAME)
db.connect()

# create table "train" and insert data from file
train_df = pd.read_csv("data/train.csv")
db_train = TableTrain(Database.DB_NAME)
db_train.connect()
db_train.create_train_table()
db_train.load_train_data(train_df)
