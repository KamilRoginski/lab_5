"""
Lab5 - Python Data Analysis App

This application allows the user to load one of two CSV files (Population and Housing Data),
perform statistical analysis (count, mean, standard deviation, min, and max) on selected columns,
and display a histogram of the data.

Submission files:
    - data_analysis_app.py      (Python Data Analysis Code)
    - PopChange.csv             (Population Data CSV)
    - Housing.csv               (Housing Data CSV)
    - Lab5_TestResults.pdf      (Document containing the test results including a test table and Pylint results)

Required libraries: pandas, numpy, matplotlib

Make sure to install the necessary modules before running the code:
    pip install pandas numpy matplotlib
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataAnalyzer:
    """
    A simple class for analyzing data from a pandas DataFrame.
    """

    def __init__(self, df):
        """
        Initialize the analyzer with a DataFrame.
        """
        self.df = df

    def compute_statistics(self, column):
        """
        Compute and return statistics for a given column.
        Returns:
            count, mean, standard deviation, min, max
        """
        try:
            # Ensure the column is numeric for calculations.
            series = self.df[column].astype(float)
        except Exception as e:
            print("Error processing column", column, ":", e)
            return None

        count = series.count()
        mean = series.mean()
        std = series.std()
        min_val = series.min()
        max_val = series.max()
        return count, mean, std, min_val, max_val

    def plot_histogram(self, column):
        """
        Generate and display a histogram for the given column.
        """
        try:
            plt.figure()
            # Drop any NaN values and ensure data is numeric.
            data = self.df[column].dropna().astype(float)
            plt.hist(data, bins=10, edgecolor='black')
            plt.title("Histogram of " + column)
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.show()
        except Exception as e:
            print("Error plotting histogram for", column, ":", e)


def main():
    """
    Main function to run the Data Analysis App.
    """
    print("***************** Welcome to the Python Data Analysis App **********")

    while True:
        # Main menu options
        print("\nSelect the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            # Population Data analysis
            try:
                pop_df = pd.read_csv("PopChange.csv")
            except Exception as e:
                print("Error reading Population CSV file:", e)
                continue

            analyzer = DataAnalyzer(pop_df)
            print("You have entered Population Data.")

            while True:
                # Column menu for Population Data
                print("\nSelect the Column you want to analyze:")
                print("a. Pop Apr 1")
                print("b. Pop Jul 1")
                print("c. Change Pop")
                print("d. Exit Column")
                col_choice = input("Enter your choice (a-d): ").strip().lower()

                if col_choice == 'a':
                    column = "Pop Apr 1"
                elif col_choice == 'b':
                    column = "Pop Jul 1"
                elif col_choice == 'c':
                    column = "Change Pop"
                elif col_choice == 'd':
                    print("You selected to exit the column menu.")
                    break
                else:
                    print("Invalid column choice. Please enter a valid option (a, b, c, or d).")
                    continue

                print("You selected", column)
                stats = analyzer.compute_statistics(column)
                if stats is None:
                    continue
                count, mean, std, min_val, max_val = stats
                print("The statistics for this column are:")
                print("Count =", count)
                print("Mean =", mean)
                print("Standard Deviation =", std)
                print("Min =", min_val)
                print("Max =", max_val)
                print("Displaying histogram for", column, "...")
                analyzer.plot_histogram(column)

        elif choice == '2':
            # Housing Data analysis
            try:
                housing_df = pd.read_csv("Housing.csv")
            except Exception as e:
                print("Error reading Housing CSV file:", e)
                continue

            analyzer = DataAnalyzer(housing_df)
            print("You have entered Housing Data.")

            while True:
                # Column menu for Housing Data
                print("\nSelect the Column you want to analyze:")
                print("a. AGE")
                print("b. BEDRMS")
                print("c. BUILT")
                print("d. ROOMS")
                print("e. UTILITY")
                print("f. Exit Column")
                col_choice = input("Enter your choice (a-f): ").strip().lower()

                if col_choice == 'a':
                    column = "AGE"
                elif col_choice == 'b':
                    column = "BEDRMS"
                elif col_choice == 'c':
                    column = "BUILT"
                elif col_choice == 'd':
                    column = "ROOMS"
                elif col_choice == 'e':
                    column = "UTILITY"
                elif col_choice == 'f':
                    print("You selected to exit the column menu.")
                    break
                else:
                    print("Invalid column choice. Please enter a valid option (a, b, c, d, e, or f).")
                    continue

                print("You selected", column)
                stats = analyzer.compute_statistics(column)
                if stats is None:
                    continue
                count, mean, std, min_val, max_val = stats
                print("The statistics for this column are:")
                print("Count =", count)
                print("Mean =", mean)
                print("Standard Deviation =", std)
                print("Min =", min_val)
                print("Max =", max_val)
                print("Displaying histogram for", column, "...")
                analyzer.plot_histogram(column)

        elif choice == '3':
            print("*************** Thanks for using the Data Analysis App **********")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
