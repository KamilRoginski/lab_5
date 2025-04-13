#Name: Kamil Roginski
#Date: 13 APR 2025
#Professor: Mark Babcock
#Course: CYOP 300

"""
LAB 5: Python Data Analysis App

1. Data Analysis and Visualization:
   - Loads two CSV files: Population Data (PopChange.csv) and Housing Data (Housing.csv).
   - For Population Data, supports analysis on columns 'Pop Apr 1', 'Pop Jul 1', and 'Change Pop'.
   - For Housing Data, supports analysis on columns 'AGE', 'BEDRMS',
     'BUILT', 'ROOMS', and 'UTILITY'.
   - Computes essential statistics including count, mean, standard deviation, min, and max.
   - Generates and displays histograms for the selected columns using matplotlib.

2. User Interaction and Error Handling:
   - Provides a text-based menu interface for file and column selection.
   - Validates user input with prompts to correct invalid entries, ensuring robust error handling.
   - Maintains continuous interaction until the user opts to exit the program.

3. Object-Oriented Programming:
   - Implements a DataAnalyzer class to encapsulate data processing functionalities.
   - Uses methods for computing statistics and plotting histograms.

CSV files used:
    - PopChange.csv             (Population Data CSV)
    - Housing.csv               (Housing Data CSV)
"""

import pandas as pd
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
        except KeyError as e:
            print(f"Error: Column '{column}' not found in DataFrame. ({e})")
            return None
        except ValueError as e:
            print(f"Error: Cannot convert data in column '{column}' to float. ({e})")
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
        except KeyError as e:
            print(f"Error: Column '{column}' not found in DataFrame. ({e})")
        except ValueError as e:
            print(f"Error: Cannot convert data in column '{column}' "
                  f"to float for histogram plotting. ({e})")

def display_main_menu():
    """
    Displays the main menu and returns the user's choice.
    """
    print("\nSelect the file you want to analyze:")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")
    return input("Enter your choice (1-3): ").strip()


def display_population_menu():
    """
    Displays the population column menu and returns the user's choice.
    """
    print("\nSelect the Column you want to analyze:")
    print("a. Pop Apr 1")
    print("b. Pop Jul 1")
    print("c. Change Pop")
    print("d. Exit Column")
    return input("Enter your choice (a-d): ").strip().lower()

def display_housing_menu():
    """
    Displays the housing column menu and returns the user's choice.
    """
    print("\nSelect the Column you want to analyze:")
    print("a. AGE")
    print("b. BEDRMS")
    print("c. BUILT")
    print("d. ROOMS")
    print("e. UTILITY")
    print("f. Exit Column")
    return input("Enter your choice (a-f): ").strip().lower()

def handle_population_data():
    """
    Handles the loading and processing of Population Data.
    """
    try:
        pop_df = pd.read_csv("PopChange.csv")
    except FileNotFoundError as e:
        print(f"Error reading Population CSV file: File not found. ({e})")
        return
    except pd.errors.EmptyDataError as e:
        print(f"Error reading Population CSV file: No data found. ({e})")
        return

    analyzer = DataAnalyzer(pop_df)
    print("You have entered Population Data.")

    while True:
        col_choice = display_population_menu()
        if col_choice == 'd':
            print("Exiting Population Data column menu.")
            break

        # Map user choice to the appropriate column name.
        column = {"a": "Pop Apr 1", "b": "Pop Jul 1", "c": "Change Pop"}.get(col_choice)
        if column is None:
            print("Invalid column choice. Please enter a valid option (a, b, c, or d).")
            continue

        print(f"You selected {column}")
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


def handle_housing_data():
    """
    Handles the loading and processing of Housing Data.
    """
    try:
        housing_df = pd.read_csv("Housing.csv")
    except FileNotFoundError as e:
        print(f"Error reading Housing CSV file: File not found. ({e})")
        return
    except pd.errors.EmptyDataError as e:
        print(f"Error reading Housing CSV file: No data found. ({e})")
        return

    analyzer = DataAnalyzer(housing_df)
    print("You have entered Housing Data.")

    while True:
        col_choice = display_housing_menu()
        if col_choice == 'f':
            print("Exiting Housing Data column menu.")
            break

        # Map user choice to the appropriate column name.
        column = {"a": "AGE", "b": "BEDRMS", "c": "BUILT",
                  "d": "ROOMS", "e": "UTILITY"}.get(col_choice)
        if column is None:
            print("Invalid column choice. Please enter a valid option (a, b, c, d, e, or f).")
            continue

        print(f"You selected {column}")
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

def main():
    """
    Main function to run the Data Analysis App.
    """
    print("***************** Welcome to the Python Data Analysis App **********")
    while True:
        choice = display_main_menu()
        if choice == '1':
            handle_population_data()
        elif choice == '2':
            handle_housing_data()
        elif choice == '3':
            print("*************** Thanks for using the Data Analysis App **********")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
