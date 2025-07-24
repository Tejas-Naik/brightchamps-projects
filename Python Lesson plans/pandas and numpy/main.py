# Pandas and NumPy Revision Lesson for Google Colab
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# URL for the CSV file
url = "https://drive.google.com/uc?id=1NI1zHuMTh6C9LY20KcM2DHBCXyHODbxH"

# ===================================
# SECTION 1: LOADING DATA WITH PANDAS
# ===================================
print("=== PANDAS AND NUMPY REVISION DEMO ===\n")

# Reading the CSV file
df = pd.read_csv(url)
print("Data loaded successfully!")

# =====================================
# SECTION 2: EXPLORING DATA WITH PANDAS
# =====================================

# Display basic information
print("\n--- Basic DataFrame Information ---")
print(f"Shape: {df.shape}")

# View first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Get column names
print("\nDataFrame columns:")
print(df.columns.tolist())

# Check data types
print("\nData types:")
print(df.dtypes)

# Get summary statistics
print("\nBasic statistics:")
print(df.describe())

# =====================================
# SECTION 3: NUMPY ARRAY OPERATIONS
# =====================================

# Convert a column to numpy array
print("\n--- NumPy Array Operations ---")

# Assuming there's a numeric column to work with
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

if numeric_columns:
    column = numeric_columns[0]
    print(f"Working with column: {column}")
    
    # Convert to numpy array
    data_array = df[column].to_numpy()
    
    print(f"\nNumPy array shape: {data_array.shape}")
    print(f"Array mean: {np.mean(data_array):.2f}")
    print(f"Array standard deviation: {np.std(data_array):.2f}")
    print(f"Array min: {np.min(data_array)}")
    print(f"Array max: {np.max(data_array)}")
    
    # Demonstrate array operations
    print("\nArray manipulations:")
    print(f"Original first 5 elements: {data_array[:5]}")
    print(f"Multiplied by 2: {data_array[:5] * 2}")
    print(f"Plus 10: {data_array[:5] + 10}")
    print(f"Squared: {np.square(data_array[:5])}")
    
    # Convert a range of values to numpy array
    print("\nCreate array with evenly spaced values:")
    print(f"np.arange(1, 10): {np.arange(1, 10)}")
    print(f"np.linspace(0, 1, 5): {np.linspace(0, 1, 5)}")
    
    # Create arrays with specific values
    print("\nCreate special arrays:")
    print(f"np.zeros(5): {np.zeros(5)}")
    print(f"np.ones(5): {np.ones(5)}")
    print(f"np.eye(3) (identity matrix):\n{np.eye(3)}")
    
    # Array reshaping
    print("\nArray reshaping:")
    arr = np.arange(12)
    print(f"Original array: {arr}")
    reshaped = arr.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{reshaped}")
    
    # Array operations across axes
    print("\nOperations across axes:")
    print(f"Sum of all elements: {np.sum(reshaped)}")
    print(f"Sum across rows (axis=1): {np.sum(reshaped, axis=1)}")
    print(f"Sum across columns (axis=0): {np.sum(reshaped, axis=0)}")

else:
    print("No numeric columns found to demonstrate NumPy operations")

# =====================================
# SECTION 4: DATA FILTERING WITH PANDAS
# =====================================

print("\n--- Data Filtering Examples ---")
# Get column names for demonstration
columns = df.columns.tolist()

if len(columns) > 0:
    # Basic filtering examples (using first column as example)
    col = columns[0]
    print(f"Filtering examples using column: {col}")
    
    if df[col].dtype == 'object':  # String column
        unique_values = df[col].unique()[:3]  # Get first 3 unique values
        if len(unique_values) > 0:
            value = unique_values[0]
            print(f"\nRows where {col} equals '{value}':")
            print(df[df[col] == value].head())
    else:  # Numeric column
        median = df[col].median()
        print(f"\nRows where {col} > {median}:")
        print(df[df[col] > median].head())

# Demonstrate multiple conditions if possible
if len(columns) > 1:
    col1 = columns[0]
    col2 = columns[1]
    print(f"\nFilter with multiple conditions ({col1} and {col2}):")
    # Adjust conditions based on column types
    if df[col1].dtype != 'object' and df[col2].dtype != 'object':
        print(df[(df[col1] > df[col1].median()) & (df[col2] > df[col2].median())].head())

# Demonstrate sorting
if len(columns) > 0:
    sort_col = columns[0]
    print(f"\nSorting by {sort_col}:")
    print(df.sort_values(by=sort_col).head())
    print(f"\nSorting by {sort_col} (descending):")
    print(df.sort_values(by=sort_col, ascending=False).head())

# Demonstrate more pandas operations
print("\nUsing .loc and .iloc for selection:")
print(f"First row using .iloc[0]: \n{df.iloc[0]}")

if len(columns) > 0:
    print(f"\nSelected columns using .loc[:, ['{columns[0]}']]: \n{df.loc[:, [columns[0]]].head()}")

# =====================================
# SECTION 5: DATA VISUALIZATION
# =====================================

print("\n--- Data Visualization ---")
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

if len(numeric_columns) >= 2:
    x_col = numeric_columns[0]
    y_col = numeric_columns[1]
    
    print(f"Creating scatter plot of {x_col} vs {y_col}")
    plt.figure(figsize=(8, 5))
    plt.scatter(df[x_col], df[y_col], alpha=0.5)
    plt.title(f'{x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    # plt.show()  # Uncomment during class
    print("Scatter plot created (uncomment plt.show() to display)")
    
    # Histogram
    print(f"\nCreating histogram of {x_col}")
    plt.figure(figsize=(8, 5))
    plt.hist(df[x_col], bins=15, alpha=0.7)
    plt.title(f'Histogram of {x_col}')
    plt.xlabel(x_col)
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    # plt.show()  # Uncomment during class
    print("Histogram created (uncomment plt.show() to display)")
    
    # Line plot if applicable (for time series or sequential data)
    if df.shape[0] > 5:  # Only if we have enough rows
        print(f"\nCreating line plot of first 10 values in {x_col}")
        plt.figure(figsize=(8, 5))
        plt.plot(range(10), df[x_col].head(10), marker='o')
        plt.title(f'Line plot of {x_col} (first 10 values)')
        plt.xlabel('Index')
        plt.ylabel(x_col)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        # plt.show()  # Uncomment during class
        print("Line plot created (uncomment plt.show() to display)")

print("\n=== Demo completed successfully! ===")
