# NumPy and Pandas Revision Lesson Plan

**Class Details:**
- **Grade Level:** 7th Grade
- **Class Size:** 2 students
- **Format:** Online class (Google Colab)
- **Duration:** 60 minutes

## Learning Objectives

By the end of this lesson, students will be able to:
1. Recall the purpose and key features of NumPy and pandas libraries
2. Load and explore datasets using pandas
3. Manipulate data using common pandas functions
4. Perform numerical operations using NumPy
5. Create basic visualizations from data

## Materials Needed

1. Google Colab environment
2. CSV dataset (provided via URL during class)
3. Code examples prepared in Google Colab notebook

## Why We Use These Libraries

### NumPy
- **Purpose:** Efficient numerical computing in Python
- **Key Benefits:**
  - Faster mathematical operations with arrays
  - Uses less memory than Python lists
  - Provides many mathematical functions
  - Makes code more readable for mathematical operations

### Pandas
- **Purpose:** Data manipulation and analysis
- **Key Benefits:**
  - Handles tabular data efficiently
  - Designed for real-world messy data
  - Built-in data cleaning features
  - Easy integration with visualization libraries
  - Better performance than working with raw Python

## Lesson Outline

### 1. Introduction (5 minutes)
- Brief recap of NumPy and pandas libraries
- Overview of the day's activities
- Check students' prior knowledge with quick questions

### 2. Loading and Exploring Data (15 minutes)

#### Setup and Import Libraries
```python
# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

#### Using pandas to load CSV data
```python
# URL for the CSV file
url = "https://drive.google.com/uc?id=1NI1zHuMTh6C9LY20KcM2DHBCXyHODbxH"

# Reading the CSV file
df = pd.read_csv(url)
print("Data loaded successfully!")
```

#### Key pandas methods for exploration
```python
# Display basic information
print(f"Shape: {df.shape}")

# View first 5 rows
print("First 5 rows:")
print(df.head())

# Get column names
print("DataFrame columns:")
print(df.columns.tolist())

# Check data types
print("Data types:")
print(df.dtypes)

# Get summary statistics
print("Basic statistics:")
print(df.describe())
```

### 3. Data Manipulation with pandas (15 minutes)

#### Selecting Data
```python
# Single column selection
single_column = df[df.columns[0]]
print(f"Single column:\n{single_column.head()}")

# Multiple columns selection
if len(df.columns) >= 2:
    two_columns = df[[df.columns[0], df.columns[1]]]
    print(f"\nTwo columns:\n{two_columns.head()}")

# Row selection by index
print(f"\nFirst row using .iloc[0]:\n{df.iloc[0]}")
print(f"\nFirst 5 rows using .iloc[0:5]:\n{df.iloc[0:5]}")
```

#### Filtering Data
```python
# Demonstration of filtering
if df.shape[1] > 0:  # If there are columns
    col = df.columns[0]
    
    if df[col].dtype != 'object':  # Numeric column
        median = df[col].median()
        filtered = df[df[col] > median]
        print(f"\nRows where {col} > {median}:\n{filtered.head()}")
    else:  # String column
        unique_values = df[col].unique()
        if len(unique_values) > 0:
            value = unique_values[0]
            filtered = df[df[col] == value]
            print(f"\nRows where {col} equals '{value}':\n{filtered.head()}")

# Multiple conditions (if applicable)
if df.shape[1] >= 2:
    col1, col2 = df.columns[0], df.columns[1]
    if df[col1].dtype != 'object' and df[col2].dtype != 'object':
        multi_filter = df[(df[col1] > df[col1].median()) & 
                         (df[col2] > df[col2].median())]
        print(f"\nMultiple conditions ({col1} and {col2}):\n{multi_filter.head()}")
```

#### Data Transformation
```python
# Sorting data
if df.shape[1] > 0:
    sort_col = df.columns[0]
    sorted_df = df.sort_values(by=sort_col)
    print(f"\nSorted by {sort_col}:\n{sorted_df.head()}")
    
    # Descending sort
    sorted_desc = df.sort_values(by=sort_col, ascending=False)
    print(f"\nSorted by {sort_col} (descending):\n{sorted_desc.head()}")

# Adding a new calculated column
if df.select_dtypes(include=['number']).shape[1] > 0:
    num_col = df.select_dtypes(include=['number']).columns[0]
    df['doubled'] = df[num_col] * 2
    print(f"\nAdded new column 'doubled':\n{df[['doubled', num_col]].head()}")
```

### 4. NumPy Operations (10 minutes)

#### Working with NumPy Arrays
```python
# Create basic arrays
print("NumPy Array Creation:")
basic_array = np.array([1, 2, 3, 4, 5])
print(f"Basic array: {basic_array}")

# Create arrays with specific patterns
print(f"\nArray of zeros: {np.zeros(5)}")
print(f"Array of ones: {np.ones(5)}")
print(f"Range array: {np.arange(1, 10)}")
print(f"Evenly spaced array: {np.linspace(0, 1, 5)}")

# Array operations
print("\nArray Operations:")
print(f"Original array: {basic_array}")
print(f"Array + 5: {basic_array + 5}")
print(f"Array * 2: {basic_array * 2}")
print(f"Array squared: {np.square(basic_array)}")

# Converting pandas column to numpy
if df.select_dtypes(include=['number']).shape[1] > 0:
    num_col = df.select_dtypes(include=['number']).columns[0]
    numpy_col = df[num_col].to_numpy()
    print(f"\nPandas column as NumPy array: {numpy_col[:5]}")
    print(f"Mean: {np.mean(numpy_col):.2f}")
    print(f"Standard deviation: {np.std(numpy_col):.2f}")
    print(f"Min: {np.min(numpy_col)}")
    print(f"Max: {np.max(numpy_col)}")

# Array reshaping
reshaping_array = np.arange(12)
reshaped = reshaping_array.reshape(3, 4)
print(f"\nOriginal flat array: {reshaping_array}")
print(f"Reshaped to 3x4:\n{reshaped}")

# Operations across axes
print(f"\nSum of all elements: {np.sum(reshaped)}")
print(f"Sum across rows (axis=1): {np.sum(reshaped, axis=1)}")
print(f"Sum across columns (axis=0): {np.sum(reshaped, axis=0)}")
```

### 5. Data Visualization (10 minutes)

#### Creating different types of plots
```python
# Setup for visualization
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

if len(numeric_columns) >= 2:
    x_col = numeric_columns[0]
    y_col = numeric_columns[1]
    
    # Scatter plot
    plt.figure(figsize=(8, 5))
    plt.scatter(df[x_col], df[y_col], alpha=0.5)
    plt.title(f'{x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df[x_col], bins=15, alpha=0.7)
    plt.title(f'Histogram of {x_col}')
    plt.xlabel(x_col)
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # Line plot
    if df.shape[0] > 5:  # Only if we have enough rows
        plt.figure(figsize=(8, 5))
        plt.plot(range(10), df[x_col].head(10), marker='o')
        plt.title(f'Line plot of {x_col} (first 10 values)')
        plt.xlabel('Index')
        plt.ylabel(x_col)
        plt.grid(True, alpha=0.3)
        plt.show()
```

### 6. Hands-on Exercise (10 minutes)

Students will work directly in Google Colab to:

1. Load the provided CSV file
   ```python
   url = "https://drive.google.com/uc?id=1NI1zHuMTh6C9LY20KcM2DHBCXyHODbxH"
   df = pd.read_csv(url)
   ```

2. Use pandas methods to answer specific questions about the data:
   - What is the average value of a specific column?
   - How many unique values are in a specific column?
   - Filter the data to find specific rows

3. Create at least one visualization from the data
   ```python
   # Example task: Create a histogram of one column
   plt.figure(figsize=(8, 5))
   plt.hist(df['column_name'], bins=10)
   plt.title('Distribution of values')
   plt.show()
   ```

4. Use NumPy to perform calculations on a data column
   ```python
   # Example task: Calculate statistics with NumPy
   arr = df['column_name'].to_numpy()
   print(f"Mean: {np.mean(arr):.2f}")
   print(f"Standard deviation: {np.std(arr):.2f}")
   ```

### 7. Closing and Review (5 minutes)
- Quick quiz on key methods and their purpose
- Address any remaining questions
- Suggest resources for further practice

## Most Frequently Used Methods Reference

### pandas
- **Data Loading:** `read_csv()`, `read_excel()`, `read_json()`
- **Exploration:** `head()`, `tail()`, `shape`, `describe()`, `info()`
- **Selection:** `loc[]`, `iloc[]`, column indexing `df['column']`
- **Filtering:** Boolean indexing, `query()`
- **Reshaping:** `pivot()`, `melt()`
- **Aggregation:** `groupby()`, `agg()`, `value_counts()`
- **Cleaning:** `dropna()`, `fillna()`, `drop_duplicates()`
- **Merging:** `merge()`, `concat()`

### NumPy
- **Array Creation:** `array()`, `zeros()`, `ones()`, `arange()`, `linspace()`
- **Math Operations:** `mean()`, `sum()`, `std()`, `min()`, `max()`
- **Array Manipulation:** `reshape()`, `transpose()`, `concatenate()`
- **Random Numbers:** `random.rand()`, `random.randint()`

## Assessment Strategy
- Observe students as they execute the code in Google Colab
- Ask them to modify the examples on their own
- Check if they can correctly interpret the output of pandas and NumPy operations

## Differentiation Strategies
- For advanced students: Add challenges like more complex data filtering or combination of multiple operations
- For struggling students: Provide additional explanations and simpler examples to work with
