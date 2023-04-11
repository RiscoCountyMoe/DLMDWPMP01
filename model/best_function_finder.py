import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from data.table_train import TableTrain
from data.table_ideal import TableIdeal

class BestFunctionFinder:
    def __init__(self, db_name):
        self.table_train = TableTrain(db_name)
        self.train_df = self.table_train.load_train_table_to_dataframe()

        self.table_ideal = TableIdeal(db_name)
        self.ideal_df = self.table_ideal.load_ideal_table_to_dataframe()

        self.results = pd.DataFrame()

    def find_best_function(self):
        # train linear regression model with train dataset
        best_functions = []
        for i in range(1, 5):
            x_train = self.train_df['x'].values.reshape(-1, 1)
            y_train = self.train_df[f'y{i}'].values.reshape(-1, 1)
            model = LinearRegression()
            model.fit(x_train, y_train)

            # compare predicted values with values from ideal dataset and store in dataframe
            mse_df = pd.DataFrame({'Function': [], 'MSE': []})
            for j in range(1, 51):
                y_ideal = self.ideal_df[f'y{j}'].values.reshape(-1, 1)
                y_pred = model.predict(x_train)
                mse = mean_squared_error(y_ideal, y_pred)
                new_row = pd.DataFrame({'Function': [f'y{j}'], 'MSE': [mse]})
                mse_df = pd.concat([mse_df, new_row], ignore_index=True)

            # find functions with least MSE and save names into list 
            best_func = mse_df.loc[mse_df['MSE'].idxmin()]['Function']
            best_functions.append(best_func)

        # write those columns containg the data for the four best functions to new dataframe
        best_func_values = self.ideal_df[best_functions].copy()
        best_func_values = pd.concat([self.train_df['x'], best_func_values], axis=1)

        return best_func_values

