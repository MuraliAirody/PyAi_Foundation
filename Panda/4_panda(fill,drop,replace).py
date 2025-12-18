# ----------------------------------------------------
# Handling Missing Data (NaN) in pandas
# ----------------------------------------------------

import pandas as pd

# Read CSV that contains NaN values
df_w = pd.read_csv("Datasets/datasets/weather_data_nan.csv")
print(df_w)

# ----------------------------------------------------
# Detecting Missing Values
# ----------------------------------------------------

# isnull() returns a DataFrame of the same shape
# True  -> value is NaN
# False -> value is NOT NaN
print(df_w.isnull())

# Count of NaN values per column
# Useful to quickly understand data quality
print(df_w.isnull().sum())

# ----------------------------------------------------
# Strategies for Handling Missing Data
# ----------------------------------------------------
# 1. Replace missing values
# 2. Remove rows or columns containing missing values

# ----------------------------------------------------
# fillna(): Replace NaN with a single value
# ----------------------------------------------------

# Replace all NaN values in the DataFrame with 0
# This does NOT modify the original DataFrame unless inplace=True
print(df_w.fillna(0))

# Replace NaN values column-wise using a dictionary
# Each column gets its own replacement value
print(
    df_w.fillna({
        "temperature": 28,
        "windspeed": 30,
        "event": "no event"
    })
)

# ----------------------------------------------------
# dropna(): Remove rows or columns with NaN values
# ----------------------------------------------------

# axis=1 → drop entire columns if they contain ANY NaN value
print(df_w.dropna(axis=1))

# axis=0 → drop entire rows if they contain ANY NaN value (default behavior)
print(df_w.dropna(axis=0))

# ----------------------------------------------------
# replace(): Replace specific values (not only NaN)
# ----------------------------------------------------

# Read CSV that contains placeholder values instead of NaN
df = pd.read_csv("Datasets/datasets/weather_data_replace.csv")
print(df)

# Replace all occurrences of -99999 with 0 across the DataFrame
print(df.replace(-99999, 0))

# Replace multiple values with a single value
# -99999 and "0" will both be replaced with 20
print(df.replace([-99999, "0"], 20))

# Replace multiple values with corresponding replacement values
# -99999 → 20
# "0"    → "no event"
print(df.replace([-99999, "0"], [20, "no event"]))

# Column-wise replacement using dictionary
# Each column has its own value to replace
print(
    df.replace({
        "temperature": -99999,
        "windspeed": -99999,
        "event": "0"
    }, 0)
)

# Column-wise replacement with different replacement values
print(
    df.replace(
        {
            "temperature": -99999,
            "windspeed": -99999,
            "event": "0"
        },
        {
            "temperature": 5,
            "windspeed": 50,
            "event": "no event"
        }
    )
)

# ----------------------------------------------------
# Group By Operations
# ----------------------------------------------------

# Read dataset used for grouping
df = pd.read_csv("Datasets/datasets/weather_by_cities_group_by.csv")
print(df)

# Group the DataFrame by 'city'
group = df.groupby("city")

'''
Data after grouping:
Each city forms an independent group

         day      city  temperature  windspeed   event
0   1/1/2017  new york           32          6    Rain
1   1/2/2017  new york           36          7   Sunny
2   1/3/2017  new york           28         12    Snow
3   1/4/2017  new york           33          7   Sunny
4   1/1/2017    mumbai           90          5   Sunny
5   1/2/2017    mumbai           85         12     Fog
6   1/3/2017    mumbai           87         15     Fog
7   1/4/2017    mumbai           92          5    Rain
8   1/1/2017     paris           45         20   Sunny
9   1/2/2017     paris           50         13  Cloudy
10  1/3/2017     paris           54          8  Cloudy
11  1/4/2017     paris           42         10  Cloudy
'''

# Fetch all rows belonging to a specific group
print(group.get_group("mumbai"))

# Compute column-wise maximum for each city group
# Numeric columns → numeric max
# Object columns  → lexicographical (alphabetical) max
print(group.max())

# ----------------------------------------------------
# Getting the Row with Maximum Temperature per City
# ----------------------------------------------------

# Select only the temperature column from the group
grp_temp = group["temperature"]

# idxmax() returns the index label of the maximum temperature per city
print(grp_temp.idxmax())

'''
Output:
city
mumbai       7
new york     1
paris       10
'''

# Use iloc with the returned indices to fetch full rows
# iloc works on zero-based positional indices
print(df.iloc[grp_temp.idxmax()])

# Same operation written in a single line
print(df.iloc[group["temperature"].idxmax()])
