import pandas as pd

# ----------------------------------------------------
# Load weather data CSV into a DataFrame
# ----------------------------------------------------
df = pd.read_csv("Datasets/datasets/weather_data.csv")

# Print the entire DataFrame
# (Useful only for small datasets)
print(df)

# ----------------------------------------------------
# df.shape
# ----------------------------------------------------
# Returns a tuple: (number_of_rows, number_of_columns)
# This helps understand the size of the dataset.
df.shape


# Sample output:
# (6, 4)
# → 6 rows and 4 columns


# ----------------------------------------------------
# Load FIFA 2018 Statistics dataset
# ----------------------------------------------------
# '../' means move one directory up from the current working directory
df = pd.read_csv("Datasets/datasets/FIFA 2018 Statistics.csv")

# ----------------------------------------------------
# df.head()
# ----------------------------------------------------
# Displays the first few rows of the DataFrame
# Default value is 5 rows
# Useful for checking:
# - Column names
# - Data types (rough idea)
# - Data quality
print(df.head())

# Displays the first 10 rows explicitly
print(df.head(10))


# ----------------------------------------------------
# df.tail()
# ----------------------------------------------------
# Displays the last few rows of the DataFrame
# Default value is 5 rows
# Useful for verifying:
# - Data completeness
# - End-of-file records
print(df.tail())

# Displays the last 10 rows explicitly
print(df.tail(10))


# ----------------------------------------------------
# df.columns
# ----------------------------------------------------
# Returns an Index object containing all column names
# Useful for:
# - Iteration
# - Column selection
# - Debugging column mismatches
print(df.columns)


# ----------------------------------------------------
# Reload weather dataset for statistical analysis
# ----------------------------------------------------
df = pd.read_csv("Datasets/datasets/weather_data.csv")

# ----------------------------------------------------
# df.describe()
# ----------------------------------------------------
# Automatically selects ONLY numerical columns
# Applies basic statistical operations:
# - count : number of non-null values
# - mean  : average
# - std   : standard deviation
# - min   : minimum value
# - 25%   : first quartile
# - 50%   : median
# - 75%   : third quartile
# - max   : maximum value
print(df.describe())


# ----------------------------------------------------
# df.describe(include=object)
# ----------------------------------------------------
# Selects ONLY categorical (object/string) columns
# Provides frequency-based statistics:
# - count  : non-null values
# - unique : number of distinct values
# - top    : most frequent value
# - freq   : frequency of the most common value
print(df.describe(include=object))


# ----------------------------------------------------
# df.info()
# ----------------------------------------------------
# Displays a concise summary of the DataFrame:
# - Column names
# - Data types
# - Non-null value counts
# - Memory usage
#
# Very useful for:
# - Identifying missing values
# - Verifying data types
# - Understanding schema before processing
print(df.info())




# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------
# Load Citi Bike trip data into a DataFrame
# ----------------------------------------------------
bike = pd.read_csv("Datasets/datasets/citibike_tripdata.csv")

# Display the first 5 rows of the dataset
# Useful for understanding column names and sample values
print(bike.head(5))





# ----------------------------------------------------
# Column Selection
# ----------------------------------------------------

# Access a single column using dot notation
# Works only if:
# - Column name has no spaces
# - Column name does not conflict with DataFrame methods
print(bike.tripduration)

# Access a single column using dictionary-style indexing
# This is the recommended and safer approach
print(bike["tripduration"])

# Access multiple columns by passing a list of column names
# Returns a new DataFrame with only the selected columns
print(bike[["tripduration", "bikeid", "usertype"]])


# ----------------------------------------------------
# Extracting a Particular Value
# ----------------------------------------------------

# Use .at[] to access a single scalar value
# Syntax: df.at[row_label, column_label]
# This is label-based and very fast for single value lookup
print(bike.at[1, "bikeid"])

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
zero-based indexing and inclusive/exclusive behavior:
Zero-based (positional) indexing:
In zero-based indexing, indexing starts from 0, slicing is position-based, the start index is inclusive, and the end index is exclusive.
Custom (label-based) indexing:
In custom or label-based indexing, selection is done using index labels rather than positions, and slicing is inclusive of both the start and end labels.
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Slicing (Row Selection)
# ----------------------------------------------------
## Pandas supports slicing rows similar to Python lists

# ----------------------------------------------------
# Slice rows using positional indexing
# Syntax: df[start : end : step]
# Note: End index is EXCLUSIVE
# Uses zero-based indexing
print(bike[5:10])


# ----------------------------------------------------
# Create a new DataFrame with first 5 rows
# ----------------------------------------------------
new_bike_share = bike[0:5]

# Assign custom index labels to the new DataFrame
ind = ["ind_1", "ind_2", "ind_3", "ind_4", "ind_5"]
new_bike_share.index = ind

# Display DataFrame with custom index
print(new_bike_share)


# ----------------------------------------------------
# Slicing with Different Indexing Types
# ----------------------------------------------------

# Positional slicing (zero-based)
# Even though index is custom, slicing by position still works
print(new_bike_share[0:5])

# Label-based slicing using custom index
# End label IS INCLUSIVE in label-based slicing
print(new_bike_share["ind_1":"ind_5"])



## ----------------------------------------------------
# .loc → Label-based selection
# ----------------------------------------------------
# .loc can extract BOTH rows and columns
# It works ONLY with LABELS (not positions)
#
# Syntax:
# df.loc[row_start : row_end , column_start : column_end]
#
# IMPORTANT RULES:
# 1. Both row_end and column_end are INCLUSIVE
# 2. Works with default index as well as custom index
# 3. Step value is NOT supported in .loc slicing
# ----------------------------------------------------

# Select rows from 'ind_1' to 'ind_3' (inclusive)
# Select columns from 'tripduration' to 'bikeid' (inclusive)
print(new_bike_share.loc["ind_1":"ind_3", "tripduration":"bikeid"])


# ----------------------------------------------------
# Using .loc with default integer index
# ----------------------------------------------------
# Even though numbers are used, .loc still treats them as LABELS
# NOT as positional indexes
#
# This will select rows with index labels 1, 2, 3, and 4
print(bike.loc[1:4])


# ----------------------------------------------------
# .iloc → Integer-location based indexing
# ----------------------------------------------------
# .iloc is used for selecting rows and columns by
# their INTEGER POSITIONS (not labels).
#
# Key rules:
# - Uses ONLY zero-based indexing
# - Works with row and column positions
# - Start index is INCLUSIVE
# - End index is EXCLUSIVE
# - Step value IS supported
#
# Syntax:
# df.iloc[row_start : row_end : row_step,
#         col_start : col_end : col_step]
# ----------------------------------------------------

# Select rows with positions 1 and 2
# (row_end = 3 is excluded)
#
# Select columns starting from position 0 up to 9
# (column_end = 10 is excluded)
#
# Select every 2nd column using step = 2
print(new_bike_share.iloc[1:3, 0:10:2])
