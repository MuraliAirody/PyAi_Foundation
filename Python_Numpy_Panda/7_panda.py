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
