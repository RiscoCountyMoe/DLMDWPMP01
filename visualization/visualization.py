import matplotlib.pyplot as plt
import seaborn as sns

from data.table_train import TableTrain
from data.table_ideal import TableIdeal
from data.table_test import TableTest
from data.table_results import ResultTable


class Visualization:
    """
    This class visualisizes the training, test, ideal and result data.

    Parameters:
    -----------
    db_name : str
        The name of the database to load the tables from.

    Attributes:
    -----------
    table_train : TableTrain object
        The object representing the training dataset.
    train_df : pandas DataFrame
        The training dataset as a pandas DataFrame.
    table_ideal : TableIdeal object
        The object representing the ideal dataset.
    ideal_df : pandas DataFrame
        The ideal dataset as a pandas DataFrame.
    table_test : TableTest object
        The object representing the test dataset.
    test_df : pandas DataFrame
        The test dataset as a pandas DataFrame.
    table_results : ResultTable
        The object representing the result dataset.
    results : pandas DataFrame
        The result dataset as a pandas DataFrame.

    """
    def __init__(self, db_name):
        self.table_train = TableTrain(db_name)
        self.train_df = self.table_train.load_train_table_to_dataframe()

        self.table_ideal = TableIdeal(db_name)
        self.ideal_df = self.table_ideal.load_ideal_table_to_dataframe()

        self.table_test = TableTest(db_name)
        self.test_df = self.table_test.load_test_table_to_dataframe()

        self.table_results = ResultTable(db_name)
        self.results = self.table_results.load_result_table_to_dataframe()

    def plot_train_data(self):
        """
        Plots the training data for y1 to y4 against x.

        """
        for i in range(1, 5):
            column_name = "y{}".format(i)
            sns.lineplot(x="x", y=column_name, data=self.train_df)

        plt.title("Training data")
        plt.xlabel("x")
        plt.ylabel("y")

        plt.savefig("training_data.png")

        plt.show()

    def plot_test_data(self):
        """
        Plots the test data as a scatter plot.

        """
        sns.scatterplot(x="x", y="y", data=self.test_df)

        plt.title("Test data")
        plt.xlabel("x")
        plt.ylabel("y")

        plt.savefig("test_data.png")

        plt.show()

    def plot_ideal_data(self):
        """
        Plots the ideal functions for y1 to y50 against x.

        """
        for i in range(1, 51):
            column_name = "y{}".format(i)
            sns.lineplot(x="x", y=column_name, data=self.ideal_df)

        plt.title("Ideal functions")
        plt.xlabel("x")
        plt.ylabel("y")

        plt.ylim(-30, 110)

        plt.savefig("ideal_functions.png")

        plt.show()

    def plot_result_data(self):
        """
        Plots the result data as a scatter plot with error bars for deviation.

        """
        sns.scatterplot(x="X", y="Y", hue="Function", data=self.results)

        deviations = self.results["Deviation"]
        plt.errorbar(
            self.results["X"],
            self.results["Y"],
            yerr=deviations,
            fmt="none",
            ecolor="gray",
        )

        for i in range(1, 5):
            column_name = "y{}".format(i)
            sns.lineplot(x="x", y=column_name, data=self.train_df)

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()

        plt.savefig("results.png")

        plt.show()
