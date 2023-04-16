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

        self.table_results = ResultTable(db_name)
        self.results = self.table_results.load_result_table_to_dataframe()

    def plot_train_data(self):
        for i in range(1, 5):
            column_name = "y{}".format(i)
            sns.lineplot(x="x", y=column_name, data=self.train_df)

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

    def plot_ideal_data(self):
        for i in range(1, 51):
            column_name = 'y{}'.format(i)
            sns.lineplot(x='x', y=column_name, data=self.ideal_df)
    
        plt.title('Ideal functions')
        plt.xlabel('x')
        plt.ylabel('y')
    
        plt.ylim(-30, 110)

        plt.show()

# hier stimmt was nicht und ich kapiere es nicht! siehe Jupyter notebook, da ist es perfekt!
    def plot_result_data(self):
       # Scatterplot erstellen
        sns.scatterplot(x='X', y='Y', hue='Function', data=self.results)
        # Deviation als Fehlerbalken hinzufügen
        deviations = self.results['Deviation']
        plt.errorbar(self.results['X'], self.results['Y'], yerr=deviations, fmt='none', ecolor='gray')
        # Linienplot erstellen
        for i in range(1, 5):
            column_name = 'y{}'.format(i)
            sns.lineplot(x='x', y=column_name, data=self.train_df)
    
        # Achsenbeschriftungen
        plt.xlabel('x')
        plt.ylabel('y')

        # Legende erstellen
        plt.legend()

        # Diagramm anzeigen
        plt.show()

