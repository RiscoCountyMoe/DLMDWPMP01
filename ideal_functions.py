import os
import sys
from data.table_train import TableTrain
from data.table_ideal import TableIdeal
from data.table_test import TableTest
from data.table_results import ResultTable
from data.database import Database
from visualization.visualization import Visualization
from model.best_function_finder import BestFunctionFinder
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

# print dataframe containing the four best fit functions vom dataset ideal
finder = BestFunctionFinder(Database.DB_NAME)
best_functions = finder.find_best_function()

results = finder.evaluate_test_data(best_functions)

# create table 'results' and insert data from resulting dataframe
db_results = ResultTable(Database.DB_NAME)
db_results.connect()
db_results.create_result_table()
db_results.load_result_data(results)

# show train_df plot
visualization = Visualization(Database.DB_NAME)
visualization.plot_all()

# show test_df plot
visualization.plot_test_data()

# show ideal_df plot
visualization.plot_ideal_data()

# show resulting mapping of data points and functions with error bars
visualization.plot_result_data()
