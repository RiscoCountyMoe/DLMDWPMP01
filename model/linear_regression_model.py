import numpy as np
import pandas as pd
from data.table_train import TableTrain
from sklearn.linear_model import LinearRegression

class LinearRegressionModel:
    def __init__(self, db_name):
        self.table_train = TableTrain(db_name)
        self.train_df = self.table_train.load_train_table_to_dataframe()

    def train_model(self):
        for i in range(1, 5):
            x_train = self.train_df['x'].values.reshape(-1, 1)
            y_train = self.train_df[f'y{i}'].values.reshape(-1, 1)
            model = LinearRegression()
            model.fit(x_train, y_train)