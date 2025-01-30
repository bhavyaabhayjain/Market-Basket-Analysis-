# Market Basket Analysis

## Overview
This project focuses on **Market Basket Analysis**, a data mining technique used to uncover relationships between products purchased by customers. By analyzing transactional data, we aim to identify patterns, associations, and frequently co-occurring items. This analysis is particularly useful for retailers to optimize product placement, cross-selling, and promotional strategies.

The project is implemented in **Python**, leveraging libraries such as `pandas`, `mlxtend`, and `matplotlib` for data processing, association rule mining, and visualization.

## Table of Contents
1. [Project Description](#project-description)
2. [Dataset](#dataset)
3. [Methodology](#methodology)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Results](#results)
7. [Contributing](#contributing)

---

## Project Description
Market Basket Analysis is a widely used technique in retail and e-commerce to understand customer purchasing behavior. This project applies the **Apriori algorithm** to discover association rules from transactional data. These rules help identify which items are frequently bought together, enabling businesses to make data-driven decisions.

**Key objectives:**
- Preprocess transactional data for analysis.
- Generate frequent itemsets using the Apriori algorithm.
- Extract meaningful association rules.
- Visualize the results for better interpretation.

---

## Dataset
The dataset used in this project contains transactional data from a retail store. Each row represents a transaction, and each column represents an item purchased. The data is in a binary format, where `1` indicates the presence of an item in the transaction and `0` indicates its absence.

---

## Methodology
### Data Preprocessing:
- Load and clean the dataset.
- Transform the data into a suitable format for analysis (e.g., one-hot encoding).

### Frequent Itemset Generation:
- Use the Apriori algorithm to identify frequent itemsets based on a minimum support threshold.

### Association Rule Mining:
- Generate association rules using metrics like support, confidence, and lift.
- Filter rules based on predefined thresholds.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bhavyaabhayjain/Market-Basket-Analysis-.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Market-Basket-Analysis-
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
To perform Market Basket Analysis, follow these steps:

### Load the dataset:
```python
import pandas as pd

# Load the dataset
df = pd.read_csv('retail_data.csv')
print(df.head())
```

### Preprocess the data:
```python
# One-hot encode the data
df_encoded = pd.get_dummies(df)
print(df_encoded.head())
```

### Generate frequent itemsets using the Apriori algorithm:
```python
from mlxtend.frequent_patterns import apriori

# Generate frequent itemsets with a minimum support of 5%
frequent_itemsets = apriori(df_encoded, min_support=0.05, use_colnames=True)
print(frequent_itemsets)
```

### Generate association rules:
```python
from mlxtend.frequent_patterns import association_rules

# Generate association rules with a minimum lift of 1.0
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
print(rules)
```

### Visualize the results:
```python
import matplotlib.pyplot as plt

# Plot the support vs. confidence
plt.scatter(rules['support'], rules['confidence'], alpha=0.5)
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.title('Support vs Confidence')
plt.show()
```

---

## Results
After running the analysis, the following association rules were discovered:

| Antecedents | Consequents | Support | Confidence | Lift |
|------------|------------|---------|------------|------|
| {Product A} | {Product B} | 0.10 | 0.75 | 2.5 |
| {Product C} | {Product D} | 0.08 | 0.80 | 3.0 |
| {Product E, Product F} | {Product G} | 0.05 | 0.90 | 4.2 |

### Key Insights:
- Customers who buy **Product A** are **75% likely** to also buy **Product B**.
- **Product C** and **Product D** are frequently purchased together with a **lift of 3.0**, indicating a strong association.
- The combination of **Product E** and **Product F** has a **high likelihood (90%)** of leading to the purchase of **Product G**.

### These insights can be used to:
- Design targeted marketing campaigns.
- Optimize product bundles.
- Improve store layouts for better cross-selling.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch.
5. Submit a pull request.


