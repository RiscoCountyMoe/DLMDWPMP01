import unittest
from model.best_function_finder import BestFunctionFinder
import pandas as pd
import numpy as np


class TestBestFunctionFinder(unittest.TestCase):
    def setUp(self):
        # Set up test dataframes
        train_data = {
            "x": [1, 2, 3, 4, 5],
            "y1": [2, 3, 4, 5, 6],
            "y2": [3, 4, 5, 6, 7],
            "y3": [4, 5, 6, 7, 8],
            "y4": [5, 6, 7, 8, 9],
        }
        self.train_df = pd.DataFrame(train_data)

        ideal_data = {
            "x": [1, 2, 3, 4, 5],
            "y1": [2, 3, 4, 5, 6],
            "y2": [3, 4, 5, 6, 7],
            "y3": [4, 5, 6, 7, 8],
            "y4": [5, 6, 7, 8, 9],
        }
        self.ideal_df = pd.DataFrame(ideal_data)

        test_data = {
            "x": [1, 2, 3, 4, 5],
            "y": [2, 3, 4, 5, 6],
        }
        self.test_df = pd.DataFrame(test_data)

    def test_find_best_function(self):
        finder = BestFunctionFinder("db_name")
        finder.train_df = self.train_df
        finder.ideal_df = self.ideal_df
        best_func_values = finder.find_best_function()
        expected_columns = ["y1", "y2", "y3", "y4"]
        self.assertListEqual(best_func_values.columns.tolist(), expected_columns)

    def test_evaluate_test_data(self):
        finder = BestFunctionFinder("db_name")
        finder.train_df = self.train_df
        finder.ideal_df = self.ideal_df
        finder.test_df = self.test_df
        best_func_values = finder.find_best_function()


        evaluation_results = finder.evaluate_test_data(best_func_values, max_deviation_factor=np.sqrt(2))
        expected_y = [2, 3, 4, 5, 6]
        expected_function = ["y1", "y1", "y1", "y1", "y1"]
        expected_deviation = [0, 0, 0, 0, 0]

        self.assertListEqual(evaluation_results["y"].tolist(), expected_y)
        self.assertListEqual(evaluation_results["function"].tolist(), expected_function)
        self.assertListEqual(evaluation_results["deviation"].tolist(), expected_deviation)