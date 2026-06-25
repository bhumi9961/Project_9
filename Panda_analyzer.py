# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python [conda env:base] *
#     language: python
#     name: conda-base-py
# ---

# %%
pip install pandas matplotlib seaborn

# %%
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

# %%
print("------------------- Data Analysis and Visualization program -------------------")


# %%
class SalesDataAnalyzer:
    """
    Parent Class
    """

    def __init__(self, file_path):
        self.data = None

        try:
            self.data = pd.read_csv(file_path)
            print("Sales data loaded successfully.")
        except Exception as e:
            print(f"Error loading file: {e}")

    def display_summary(self):
        """
        Display basic dataset summary.
        """
        if self.data is not None:
            print("\n===== Dataset Summary =====")
            print(self.data.describe(include='all'))

    def clean_data(self):
        """
        Handle missing values.
        """
        if self.data is None:
            return

        numeric_cols = self.data.select_dtypes(
            include=['number']
        ).columns

        for col in numeric_cols:
            self.data[col] = self.data[col].fillna(
                self.data[col].median()
            )

        print("Data cleaning completed.")

    def __add__(self, other):
        """
        Operator Overloading
        Combine two SalesDataAnalyzer objects.
        """
        combined_df = pd.concat(
            [self.data, other.data],
            ignore_index=True
        )

        new_obj = SalesDataAnalyzer.__new__(
            SalesDataAnalyzer
        )
        new_obj.data = combined_df

        return new_obj

    def __del__(self):
        print("Cleaning up resources...")

    def visualize(self):
        if self.data is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Data Visualization ==")
            print("1. Bar chart")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Back")

            choice = input("Enter your choice: ")

            # ---------------- BAR CHART ----------------
            if choice == "1":
                col = self.data.select_dtypes(include=numpy.number).columns[0]
                self.data[col].plot(kind='bar')
                plt.title("Bar Chart")
                plt.show()

            # ---------------- LINE ----------------
            elif choice == "2":
                col = self.data.select_dtypes(include=numpy.number).columns[0]
                self.data[col].plot(kind='line')
                plt.title("Line Plot")
                plt.show()

            # ---------------- SCATTER (YOUR CHOICE 3) ----------------
            elif choice == "3":
                num_cols = self.data.select_dtypes(include=numpy.number).columns

                if len(num_cols) >= 2:
                    x = num_cols[0]
                    y = num_cols[1]

                    plt.scatter(self.data[x], self.data[y])
                    plt.title("Scatter Plot")
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.show()
                else:
                    print("Need at least 2 numeric columns")

            # ---------------- PIE ----------------
            elif choice == "4":
                col = self.data.select_dtypes(include=numpy.number).columns[0]
                data = self.data[col].head(5)
                plt.pie(data, labels=data.index, autopct='%1.1f%%')
                plt.title("Pie Chart")
                plt.show()

            # ---------------- HISTOGRAM ----------------
            elif choice == "5":
                col = self.data.select_dtypes(include=numpy.number).columns[0]
                plt.hist(self.data[col], bins=10)
                plt.title("Histogram")
                plt.show()

            # ---------------- STACK PLOT ----------------
            elif choice == "6":
                num_cols = self.data.select_dtypes(include=numpy.number).columns[:3]

                if len(num_cols) >= 2:
                    plt.stackplot(range(len(self.df)),
                                  [self.df[col] for col in num_cols])
                    plt.legend(num_cols)
                    plt.title("Stack Plot")
                    plt.show()
                else:
                    print("Need at least 2 numeric columns")

            elif choice == "7":
                break

            else:
                print("Invalid choice")




# %%
# -------------------------------------
# Child Class (Inheritance)
# -------------------------------------
class AdvancedSalesAnalyzer(SalesDataAnalyzer):

    def __init__(self, file_path):
        # Call Parent Constructor
        super().__init__(file_path)

    def display_summary(self):
        """
        Overridden Method
        """
        print("\n===== Advanced Summary =====")

        if self.data is not None:
            print(self.data.describe(include='all'))

            print("\nDataset Shape:")
            print(self.data.shape)

            print("\nMissing Values:")
            print(self.data.isnull().sum())

    def split_by_region(self):
        """
        Additional functionality.
        """
        if 'Region' not in self.data.columns:
            print("Region column not found.")
            return

        groups = self.data.groupby('Region')

        for region, df in groups:
            print(f"\nRegion: {region}")
            print(df.head())


# %%
###### -------------------------------------
# Menu-Driven User Interface
# -------------------------------------
def main():

    file_path = input(
        "Enter sales CSV file path: "
    )

    analyzer = AdvancedSalesAnalyzer(
        file_path
    )

    while True:

        print("\n")
        print("================================")
        print("      SALES DATA ANALYZER")
        print("================================")
        print("1. View First 5 Rows")
        print("2. Dataset Information")
        print("3. Statistical Summary")
        print("4. Clean Data")
        print("5. Split Data By Region")
        print("6. Convert Column To NumPy Array")
        print("7. Data Visualization")
        print("8. Exit")
        print("================================")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            print(analyzer.data.head())

        elif choice == "2":

            analyzer.data.info()

        elif choice == "3":

            analyzer.display_summary()

        elif choice == "4":

            analyzer.clean_data()

        elif choice == "5":

            analyzer.split_by_region()


        elif choice == "6":

            column = input(
                "Enter column name: "
            )

            if column in analyzer.data.columns:

                arr = analyzer.data[
                    column
                ].to_numpy()

                print("\nNumPy Array:")
                print(arr)

                print("\nFirst Element:")
                print(arr[0])

                print("\nFirst Five Elements:")
                print(arr[:5])

            else:
                print("Column not found.")

        elif choice == "7": 
            analyzer.visualize()
        
        elif choice == "8":

            print(
                "\nThank you for using "
                "Sales Data Analyzer!"
            )
            break

        else:

            print(
                "Invalid choice. "
                "Please try again."
            )


# -------------------------------------
# Program Entry Point
# -------------------------------------
if __name__ == "__main__":
    main()


# %%
