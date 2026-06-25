# Sales Data Analyzer

## Project Overview

Sales Data Analyzer is a Python-based data analysis and visualization application developed using Object-Oriented Programming (OOP) concepts. The project provides functionalities for loading, cleaning, analyzing, manipulating, and visualizing sales datasets using Pandas, NumPy, Matplotlib, and Seaborn.

The application offers a menu-driven interface that allows users to perform various data analysis tasks efficiently.

---

## Features

### Data Loading

* Load sales data from CSV files.
* Exception handling for invalid file paths or file formats.

### Data Exploration

* Display dataset preview using `head()`.
* Show dataset information using `info()`.
* Generate descriptive statistics using `describe()`.

### Data Cleaning

* Identify missing values.
* Handle missing data using appropriate techniques.
* Remove duplicate records.
* Perform data type conversions.

### NumPy Operations

* Convert DataFrame columns into NumPy arrays.
* Demonstrate array indexing and slicing.
* Perform element-wise mathematical operations.
* Compute square roots, powers, and statistical measures.

### Data Manipulation

* Combine DataFrames using:

  * `concat()`
  * `merge()`
  * `join()`
* Split datasets based on:

  * Region
  * Product
  * Category

### Search, Sort and Filter

* Search specific products or sales records.
* Sort data based on sales, profit, quantity, etc.
* Filter data by region, category, or date range.

### Statistical Analysis

* Mean
* Median
* Standard Deviation
* Variance
* Percentiles
* Correlation Analysis

### Aggregation Functions

* Sum
* Mean
* Count
* Min
* Max

### Pivot Tables

* Generate pivot tables for summarized reports.
* Analyze sales by region, category, or product.

### GroupBy Operations

* Group data by regions or categories.
* Apply aggregate functions.
* Use `transform()` for advanced analysis.

### Data Visualization (Matplotlib)

* Bar Chart
* Line Plot
* Scatter Plot
* Pie Chart
* Histogram
* Stack Plot
* Subplots

### Data Visualization (Seaborn)

* Heatmap
* Box Plot
* Distribution Analysis

### Export Results

* Save processed datasets to CSV files.
* Save generated visualizations as image files.

---

## Technologies Used

* Python 3.x
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Project Structure

```text
SalesDataAnalyzer/
│
├── sales_data_analyzer.py
├── train.csv
├── output/
│   ├── charts/
│   └── reports/
├── README.md
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/sales-data-analyzer.git
cd sales-data-analyzer
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python sales_data_analyzer.py
```

---

## Main Menu

```text
========== Data Analysis & Visualization Program ==========

1. Load Dataset
2. Explore Data
3. Numpy Operations
4. Handle Missing Data
5. Search / Sort / Filter
6. Aggregate Functions
7. Statistical Analysis
8. Pivot Table
9. GroupBy Analysis
10. Data Visualization
11. Export Results
12. Exit
```

---

## Sample Dataset

The project works with any CSV sales dataset containing columns such as:

```text
Order ID
Product Name
Category
Region
Sales
Profit
Quantity
Order Date
```

Example:

```csv
Order_ID,Product,Region,Sales,Profit
1001,Laptop,East,1200,300
1002,Printer,West,400,100
1003,Phone,South,800,200
```

---

## OOP Concepts Implemented

### Encapsulation

All data and functionalities are encapsulated within the `SalesDataAnalyzer` class.

### Constructor

```python
def __init__(self):
```

### Destructor

```python
def __del__(self):
```

### Inheritance (Optional)

The project can be extended using:

```python
class AdvancedSalesAnalyzer(SalesDataAnalyzer):
```

### Method Overriding (Optional)

Override parent methods for advanced functionality.

---

## Future Enhancements

* GUI using Tkinter or PyQt
* Dashboard using Streamlit
* Excel and PDF report generation
* Machine Learning sales prediction
* Database integration

---

## Author

Bhumi Shah

---

## License

This project is developed for educational and academic purposes.
