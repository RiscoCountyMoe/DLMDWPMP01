import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from data.table_train import TableTrain
from data.table_ideal import TableIdeal
from data.table_test import TableTest


class BestFunctionFinder:
    def __init__(self, db_name):
        self.table_train = TableTrain(db_name)
        self.train_df = self.table_train.load_train_table_to_dataframe()

        self.table_ideal = TableIdeal(db_name)
        self.ideal_df = self.table_ideal.load_ideal_table_to_dataframe()

        self.table_test = TableTest(db_name)
        self.test_df = self.table_test.load_test_table_to_dataframe()

    def find_best_function(self):
        # train linear regression model with training functions from train dataset
        best_functions = []
        num_cols = len(self.train_df.columns) - 1  # Subtract 1 for 'x' column
        for i in range(1, num_cols+1):
            x_train = self.train_df["x"].values.reshape(-1, 1)
            y_train = self.train_df.iloc[:, i].values.reshape(-1, 1)
            model = LinearRegression()
            model.fit(x_train, y_train)

            # compare predicted values with values from ideal dataset and store function with mean squared error in dataframe
            mse_df = pd.DataFrame({"Function": [], "MSE": []})
            for col in self.ideal_df.columns[1:]:  # start at index 1 to exclude 'x' column
                y_ideal = self.ideal_df[col].values.reshape(-1, 1)
                y_pred = model.predict(x_train)
                mse = mean_squared_error(y_ideal, y_pred)
                new_row = pd.DataFrame({"Function": [col], "MSE": [mse]})
                mse_df = pd.concat([mse_df, new_row], ignore_index=True)
            # find functions with least MSE and save names into list
            best_func = mse_df.loc[mse_df["MSE"].idxmin()]["Function"]
            best_functions.append(best_func)

        # write those columns containg the data for the four best fitting functions to new dataframe
        best_func_values = self.ideal_df[best_functions].copy()

        return best_func_values

    def evaluate_test_data(self, best_func_values, max_deviation_factor=np.sqrt(2)):
        # create empty DataFrame to store evaluation results
        evaluation_results = pd.DataFrame(columns=["x", "y", "function", "deviation"])

        best_func_columns = best_func_values.columns.tolist()

        # copy functions from training data set and rename according to names of best fitting functions
        new_train_df = self.train_df[["x", "y1", "y2", "y3", "y4"]].copy()

        new_train_df = new_train_df.rename(
            columns={
                "y1": best_func_values.columns[0],
                "y2": best_func_values.columns[1],
                "y3": best_func_values.columns[2],
                "y4": best_func_values.columns[3],
            }
        )

        # iterate over test dataset
        for i in range(len(self.test_df)):
            x_test = self.test_df.loc[i]["x"]
            y_test = self.test_df.loc[i]["y"]

            # iterate over the columns in best_func_values
            for col_name in best_func_columns:
                y_pred = best_func_values.loc[i][col_name]
                deviation = abs(y_test - y_pred)

                # check if deviation exceeds the maximum allowed deviation and store results in dataframe
                max_deviation = max_deviation_factor * new_train_df[col_name].std()
                if deviation <= max_deviation:
                    df = pd.DataFrame(
                        {
                            "x": [x_test],
                            "y": [y_test],
                            "function": [col_name],
                            "deviation": [deviation],
                        }
                    )
                    evaluation_results = pd.concat(
                        [evaluation_results, df], ignore_index=True
                    )
                    break

        return evaluation_results
