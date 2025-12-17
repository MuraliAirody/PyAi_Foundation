import pandas as pd

# ----------------------------------------------------
# Conditional Selection (Boolean Indexing)
# ----------------------------------------------------

# Load Citi Bike trip data into a DataFrame
bike_share = pd.read_csv("Datasets/datasets/citibike_tripdata.csv")

# Print the entire DataFrame (useful only for small datasets)
print(bike_share)


# ----------------------------------------------------
# Creating a Boolean Condition
# ----------------------------------------------------

# Create a boolean Series by applying a condition
# This checks whether tripduration > 1000 for the first 10 rows
# Result will be True or False for each row
print(bike_share["tripduration"].head(10) > 1000)


# ----------------------------------------------------
# Applying Boolean Conditions to Filter Data
# ----------------------------------------------------

# Apply condition to the ENTIRE DataFrame using .loc
# Returns all rows where tripduration is greater than 1000
print(bike_share.loc[bike_share["tripduration"] > 1000])


# Apply condition only to the FIRST 10 rows
# Both the DataFrame and condition are limited to the same index range
print(
    bike_share.head(10)[
        bike_share["tripduration"].head(10) > 1000
    ]
)


# ----------------------------------------------------
# Filtering Using a Single Condition
# ----------------------------------------------------

# Select all rows where usertype is 'Customer'
print(bike_share[bike_share["usertype"] == "Customer"])


# ----------------------------------------------------
# Filtering Using Multiple Conditions
# ----------------------------------------------------

# Select rows where:
# - usertype is 'Customer'
# - tripduration is greater than 1000
#
# Note:
# - Use '&' instead of 'and'
# - Parentheses around each condition are mandatory
print(
    bike_share[
        (bike_share["usertype"] == "Customer") &
        (bike_share["tripduration"] > 1000)
    ]
)





# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# Addition and Deletion of Columns in a DataFrame
# ----------------------------------------------------

# Read the CSV file into a DataFrame.
# This loads the data into memory; the source file is not modified.
df_org = pd.read_csv("Datasets/datasets/international_org.csv")

# Print the original DataFrame
print(df_org)


# ----------------------------------------------------
# Adding a New Column using assignment
# ----------------------------------------------------

# Add a new column named 'new_col' and assign scalar value 0
# Pandas broadcasts the scalar value to all rows
df_org["new_col"] = 0
print(df_org)


# ----------------------------------------------------
# Replacing an Existing Column
# ----------------------------------------------------

# Assign a list of values to 'new_col'
# Length of the list must exactly match the number of rows
# This REPLACES the existing 'new_col' values
df_org["new_col"] = [0, 1, 2, 3, 4, 5]
print(df_org)


# ----------------------------------------------------
# Error Case: Length Mismatch
# ----------------------------------------------------

# Attempt to assign a list with fewer elements than rows
# This raises a ValueError because pandas cannot align values to rows
try:
    df_org["new_col"] = [0, 1, 2, 3, 4]  # length = 5, rows = 6
except Exception as e:
    print(e)


# ----------------------------------------------------
# Inserting a Column at a Specific Position
# ----------------------------------------------------

# Insert a new column named 'insert_col' at index position 1
# Value 0 is broadcasted to all rows
# insert() modifies the DataFrame IN PLACE
df_org.insert(1, "insert_col", 0)
print(df_org)


# ----------------------------------------------------
# Error Case: Inserting an Existing Column
# ----------------------------------------------------

# Attempt to insert a column with a name that already exists
# insert() does NOT allow duplicate column names
try:
    df_org.insert(1, "insert_col", 1)
except Exception as e:
    print(e)


# ----------------------------------------------------
# Error Case: Length Mismatch with insert()
# ----------------------------------------------------

# Attempt to insert a column with a list of values
# Length must match number of rows exactly
try:
    df_org.insert(1, "new_insert_col", [1, 2, 3])
except Exception as e:
    print(e)


# ----------------------------------------------------
# Deleting Columns using drop()
# ----------------------------------------------------

# drop() returns a NEW DataFrame by default
# inplace=True modifies the original DataFrame and returns None
print(df_org.drop(columns=["insert_col", "new_col"], inplace=True))  # Output: None

# Verify that the columns are removed from the original DataFrame
print(df_org)


# ----------------------------------------------------
# Deleting a Column using del
# ----------------------------------------------------

# del removes the column directly from the DataFrame
# This operation is always in-place
del df_org["Headquater"]

# Print the DataFrame after deletion
print(df_org)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# Addition and Deletion of Rows in a DataFrame
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Load the CSV file into a DataFrame (data is loaded into memory)
df_org = pd.read_csv("Datasets/datasets/international_org.csv")

# Print the original DataFrame
print(df_org)


# --------------------------------------------------------------------
# Adding NEW rows using .loc
# --------------------------------------------------------------------

# Add a new row with index label 6
# When assigning a scalar value, pandas fills ALL columns with that value
df_org.loc[6] = "new_value"
print(df_org)

# Add another new row with index label 7
# Values must be provided for ALL columns in the DataFrame
# Empty string "" is treated as a valid value (not NaN)
df_org.loc[7] = ["new_value1", ""]
print(df_org)


# --------------------------------------------------------------------
# Replacing an EXISTING row
# --------------------------------------------------------------------

# Replace values of the row with index label 2
# This overwrites the existing row completely
df_org.loc[2] = ["replace_1", "replace_2"]
print(df_org)


# --------------------------------------------------------------------
# Deleting rows using drop()
# --------------------------------------------------------------------

# drop() removes rows by index label
# inplace=False (default) → returns a NEW DataFrame
# The original df_org remains unchanged
print(df_org.drop(index=[2, 7]))

# Delete rows with index labels 1 and 2 from the ORIGINAL DataFrame
# inplace=True → modifies df_org directly
df_org.drop(index=[1, 2], inplace=True)

# Print DataFrame after deletion
print(df_org)


# --------------------------------------------------------------------
# Difference between .iloc and .loc after row deletion
# --------------------------------------------------------------------

try:
    # .iloc uses POSITIONAL indexing (zero-based)
    # Row at position 1 still exists even if index labels are missing
    print(df_org.iloc[[1]])

    # .loc uses LABEL-based indexing
    # Index label '1' was deleted earlier, so this raises KeyError
    print(df_org.loc[1])

except Exception as e:
    print(f"exception {e}")




# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sorting Data in a DataFrame
# ----------------------------------------------------

# Load the CSV file containing unsorted IMDb ratings
df_sort = pd.read_csv("Datasets/datasets/unsorted_imdb_rating.csv")

# Print the original (unsorted) DataFrame
print(df_sort)


# ----------------------------------------------------
# Sorting rows based on column values
# ----------------------------------------------------

# Sort the DataFrame by the 'star_rating' column in ascending order (default)
# This returns a NEW DataFrame; the original df_sort remains unchanged
print(df_sort.sort_values(by=["star_rating"]))

# Sort the DataFrame by 'star_rating' in descending order
# ascending=False reverses the sort order
# This also returns a NEW DataFrame
print(df_sort.sort_values(by=["star_rating"], ascending=False))


# ----------------------------------------------------
# Sorting in-place
# ----------------------------------------------------

# Sort the DataFrame by 'star_rating' in descending order
# inplace=True modifies the original DataFrame directly and returns None
df_sort.sort_values(by=["star_rating"], ascending=False, inplace=True)

# Print the DataFrame after in-place sorting
print(df_sort)


# ----------------------------------------------------
# Sorting by index
# ----------------------------------------------------

# Sort the DataFrame based on index labels
# This returns a NEW DataFrame; df_sort is not modified
print(df_sort.sort_index())


# ----------------------------------------------------
# Resetting the index
# ----------------------------------------------------

# Reset the index and convert the old index into a new column named 'index'
# This returns a NEW DataFrame
print(df_sort.reset_index())

# Reset the index and DROP the old index completely
# A fresh default zero-based index is assigned
# This returns a NEW DataFrame
print(df_sort.reset_index(drop=True))


# ------------------------------------------------------------------------------------------------------------------------------------
# Concatenation in pandas
# ----------------------
# pd.concat() is used to combine DataFrames either row-wise (default, axis=0)
# or column-wise (axis=1).


# Creating a DataFrame for India weather data
india_weather = pd.DataFrame({
    "city": ["Mumbai", "Delhi", "Banaglore"],
    "temp": [30, 32, 22],
    "humidity": [70, 60, 40]
})

# Creating a DataFrame for US weather data
us_weather = pd.DataFrame({
    "city": ["NewYork", "Chicago", "Orlando"],
    "temp": [21, 14, 22],
    "humidity": [68, 75, 55]
})

# Printing individual DataFrames
print(india_weather)
print(us_weather)

# ---------------------------------------
# Basic concatenation (row-wise)
# ---------------------------------------
# This stacks us_weather below india_weather.
# Index values from original DataFrames are preserved.
print(pd.concat([india_weather, us_weather]))

# ---------------------------------------
# Concatenation with ignore_index=True
# ---------------------------------------
# ignore_index=True resets the index and creates a new continuous index.
print(pd.concat([india_weather, us_weather], ignore_index=True))

# ---------------------------------------
# Concatenation with keys
# ---------------------------------------
# keys create a MultiIndex (hierarchical index).
# 'india' and 'us' become the outer index labels.
print(pd.concat([india_weather, us_weather], keys=["india", "us"]))

# Storing the concatenated DataFrame with keys
df_weather = pd.concat([india_weather, us_weather], keys=["india", "us"])

# ---------------------------------------
# Accessing data using .loc with MultiIndex
# ---------------------------------------
# This returns all rows belonging to the 'india' key.
print(df_weather.loc["india"])



# ------------------------------------------------------------------------------------------------------------------------
# Merge in pandas
# ---------------
# pd.merge() is used to combine two DataFrames based on one or more common columns.
# It works similar to SQL JOIN operations.

"""
Conditions for merging:
1. There must be at least two DataFrames.
2. At least one column should be common between the DataFrames
   (or explicitly specified using 'on', 'left_on', 'right_on').
"""

# First weather DataFrame
weather_1 = pd.DataFrame({
    "city": ["NewYork", "LOS", "Austin", "Chicago"],
    "temp": [30, 32, 22, 29],
    "humidity": [70, 60, 40, 45]
})

# Second weather DataFrame
weather_2 = pd.DataFrame({
    "city": ["NewYork", "Chicago", "Orlando"],
    "temp": [30, 29, 22],
    "humidity": [68, 75, 55]
})

# Displaying the input DataFrames
print(weather_1)
print(weather_2)

# -------------------------------------------------
# INNER JOIN
# -------------------------------------------------
# Returns only rows where the 'city' value exists in BOTH DataFrames.
# Common cities here: NewYork, Chicago
print(pd.merge(weather_1, weather_2, how="inner", on="city"))

# -------------------------------------------------
# LEFT JOIN
# -------------------------------------------------
# Returns all rows from the LEFT DataFrame (weather_1).
# Matching rows from weather_2 are added.
# If no match is found, NaN is filled for right-side columns.
print(pd.merge(weather_1, weather_2, how="left", on="city"))

# -------------------------------------------------
# RIGHT JOIN
# -------------------------------------------------
# Returns all rows from the RIGHT DataFrame (weather_2).
# Matching rows from weather_1 are added.
# If no match is found, NaN is filled for left-side columns.
print(pd.merge(weather_1, weather_2, how="right", on="city"))

# -------------------------------------------------
# OUTER JOIN
# -------------------------------------------------
# Returns all rows from BOTH DataFrames.
# Non-matching rows from either side will have NaN values.
print(pd.merge(weather_1, weather_2, how="outer", on="city"))

# -------------------------------------------------
# OUTER JOIN with indicator=True
# -------------------------------------------------
# Adds an extra column '_merge' to show the source of each row:
# - 'left_only'  : row exists only in weather_1
# - 'right_only' : row exists only in weather_2
# - 'both'       : row exists in both DataFrames
print(pd.merge(weather_1, weather_2, how="outer", on="city", indicator=True))



