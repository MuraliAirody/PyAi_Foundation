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


# ----------------------------------------------------
# Addition and Deletion (Covered Conceptually Below)
# ----------------------------------------------------
