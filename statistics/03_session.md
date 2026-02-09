# Box and Whisker Plot (Box Plot)

A Box and Whisker plot is a graphical method used to display the distribution of data and identify outliers using quartiles.

#### What it shows

A box plot summarizes data using five-number summary:

- Minimum

- Q1 (First Quartile – 25%)

- Median (Q2 – 50%)

- Q3 (Third Quartile – 75%)

- Maximum

##### Structure of a Box Plot


Min ──|────[ Q1 ── Median ── Q3 ]────|── Max

                    ←─── Box ───→


- Box → Q1 to Q3 (IQR)

- Line inside box → Median

- Whiskers → Extend to min and max (excluding outliers)

- Dots/points → Outliers

### Interquartile Range (IQR)
IQR = 𝑄3 − 𝑄1

IQR = Q3 − Q1

Used to detect outliers.

### Outlier Rule (Box Plot Rule)

- Lower bound = Q1 − 1.5 × IQR

- Upper bound = Q3 + 1.5 × IQR

Any value outside this range is plotted as an outlier.

**Example:**

Data: 10, 12, 14, 15, 18, 20, 100

- Q1 = 12

- Median = 15

- Q3 = 20

- IQR = 20 − 12 = 8

- Upper bound = 20 + 1.5×8 = 32

- 100 is an outlier

#### Why box plots are useful

- Quickly identify outliers

- Show data spread and skewness

- Compare multiple datasets easily

- No assumption of normal distribution

#### Skewness in box plot

- Median closer to Q1 → Right-skewed

- Median closer to Q3 → Left-skewed

- Equal spacing → Symmetric

#### One-line definition (exam/interview ready)

A box and whisker plot is a graphical representation of data that shows its spread, central tendency, and outliers using quartiles.