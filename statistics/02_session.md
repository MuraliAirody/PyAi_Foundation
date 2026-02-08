# Descriptive Statistics

Descriptive statistics summarize and describe the main features of a dataset. The most common measures are mean, median, mode, and outliers.

## 1. Mean (Average)

The mean is the sum of all values divided by the number of values.

Formula:

Mean=∑x​/n
	​

**Example:**
- Data: 2, 4, 6, 8
- Mean = (2 + 4 + 6 + 8) / 4 = 5

Key points:

- Uses all values

- Highly affected by outliers

- Best for normally distributed data

## 2. Median

The median is the middle value when data is arranged in ascending order.

How to calculate:

Odd count → middle value

Even count → average of two middle values

**Example:**
- Data: 2, 4, 6, 8, 100
- Median = 6

Key points:

Not affected by outliers

Best for skewed data (e.g., income, salaries)

## 3. Mode

The mode is the value that occurs most frequently.

**Example:**
- Data: 1, 2, 2, 3, 4
- Mode = 2

Key points:

Can have no mode, one mode, or multiple modes

Useful for categorical data (e.g., gender, product type)

## 4. Outliers

Outliers are values that are significantly different from the rest of the data.

An outlier is a data value that is much smaller or much larger than most of the other values in a dataset.

**Example:**
Data: 10, 12, 11, 13, 100
Outlier = 100

Common ways to detect outliers

- IQR method

IQR = Q3 − Q1

Lower bound = Q1 − 1.5 × IQR

Upper bound = Q3 + 1.5 × IQR

- Z-score

If |z| > 3 → possible outlier

Why outliers matter:

Can distort the mean

May indicate errors or rare but important events

#### Why outliers matter

- They can distort results, especially the mean

They may indicate:

- Data entry errors

- Measurement errors

- Rare but important events

**Example:**

Salaries: 30k, 32k, 35k, 38k, 5 crore

The mean becomes misleading, but the median stays realistic.