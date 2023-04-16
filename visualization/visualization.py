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

    def plot_train_data(self):
        for i in range(1, 5):
            column_name = "y{}".format(i)
            sns.scatterplot(x="x", y=column_name, data=self.train_df)

        plt.title("Training data")
        plt.xlabel("x")
        plt.ylabel("y")

        plt.show()

    def plot_test_data(self):
        sns.scatterplot(x="x", y="y", data=self.test_df)

        plt.title("Test data")
        plt.xlabel("x")
        plt.ylabel("y")

        plt.show()
