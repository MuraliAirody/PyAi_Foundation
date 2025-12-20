
# Pandas mainly gives you three relevant outputs after groupby():
- Series
- DataFrame
- MultiIndex DataFrame

### Series (most common after single aggregation)
Example

```python
result = master_data.groupby("City")["AQI"].mean()
```

What you get

- Type: Series
- Index: City
- No column name (unless you rename it)
```
Output shape:
City
Mumbai     168.2
Delhi      195.4
```
How to recognize

```python
type(result)
#pandas.core.series.Series
```

When this happens
- You select one column
- You apply one aggregation
- Result is 1D

### DataFrame (flat columns, no MultiIndex)
Example
```python
result = master_data.groupby("City")[["AQI", "Rainfall (mm)"]].mean()
```

What you get

- Type: DataFrame
- Index: City
- Columns: AQI, Rainfall (mm)

```
Output:
           AQI   Rainfall (mm)
City
Mumbai     168.2     4.3
Delhi      195.4     1.2
```

When this happens

- Multiple columns selected
- Single aggregation per column

### MultiIndex DataFrame (the confusing one)
Example
```python
result = master_data.groupby("City").agg({
    "AQI": ["mean", "max"],
    "Rainfall (mm)": ["sum", "mean"]
})
```

What you get

- Type: DataFrame
- Index: City
- Columns: MultiIndex
```
Output:
                 AQI                  Rainfall (mm)
                mean   max              sum   mean
City
Mumbai         168.2   312             842.3  4.3
Delhi          195.4   398             412.1  1.2
```

Column structure:
```
MultiIndex([
  ('AQI', 'mean'),
  ('AQI', 'max'),
  ('Rainfall (mm)', 'sum'),
  ('Rainfall (mm)', 'mean')
])
```

### Why MultiIndex appears
You get a MultiIndex DataFrame when:

- Multiple columns
- Multiple aggregations
- OR multiple grouping keys

Example with multiple group keys:
```python
master_data.groupby(["City", "YearMonth"])["AQI"].mean()
```
Index:
```
MultiIndex (City, YearMonth)
```

### How to handle each type
Convert Series → DataFrame
```python
result.reset_index(name="Avg_AQI")
```

Flatten MultiIndex columns (very common requirement)
```python
result.columns = ['_'.join(col) for col in result.columns]
result.reset_index()
```
Or better:
```python
result = result.rename_axis(None, axis=1).reset_index()
```
### How to quickly identify what you have
```python
type(result)
result.index
result.columns
```

### Decision table (memorize this)
| Output        | Index        | Columns    | When                     |
| ------------- | ------------ | ---------- | ------------------------ |
| Series        | Single       | None       | 1 column, 1 agg          |
| DataFrame     | Single       | Flat       | Many columns, 1 agg      |
| MultiIndex DF | Single/Multi | MultiIndex | Many columns + many aggs |

### Golden rule
If you see brackets inside brackets when printing columns → it’s MultiIndex.