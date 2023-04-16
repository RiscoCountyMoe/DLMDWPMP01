import matplotlib.pyplot as plt
import seaborn as sns

from data.table_train import TableTrain
from data.table_ideal import TableIdeal
from data.table_test import TableTest
from data.table_results import ResultTable

class Visualization:
    def __init__(self, db_name):
        self.table_train = TableTrain(db_name)
        self.train_df = self.table_train.load_train_table_to_dataframe()

        self.table_ideal = TableIdeal(db_name)
        self.ideal_df = self.table_ideal.load_ideal_table_to_dataframe()

        self.table_test = TableTest(db_name)
        self.test_df = self.table_test.load_test_table_to_dataframe()