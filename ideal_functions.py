import os
import sys
from data.table_train import TableTrain
from data.table_ideal import TableIdeal
from data.table_test import TableTest
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

# create table "ideal" and insert data from file
ideal_df = pd.read_csv("data/ideal.csv")
db_ideal = TableIdeal(Database.DB_NAME)
db_ideal.connect()
db_ideal.create_ideal_table()
db_ideal.load_ideal_data(ideal_df)

# create table "test" and insert data from file
test_df = pd.read_csv("data/test.csv")
db_test = TableTest(Database.DB_NAME)
db_test.connect()
db_test.create_test_table()
db_test.load_test_data(test_df)

# create table "results" and insert result data from dataframe