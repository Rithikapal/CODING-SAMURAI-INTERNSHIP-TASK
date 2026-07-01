# Titanic - Exploratory Data Analysis

Analyzed the Titanic dataset to find patterns in passenger survival based on gender, class, age, and fare.

## About the Project

I explored the Titanic dataset (891 passengers) to understand what factors influenced survival. The analysis includes missing value treatment, distribution plots, group-wise survival comparisons, and a correlation heatmap — all done using Python.

## Dataset

**Source:** [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)  
**File:** Titanic_train.csv — 891 rows, 12 columns

## What I Did

- Filled 177 missing Age values using the median
- Calculated overall survival rate
- Plotted age and fare distributions
- Compared survival rates by gender, class, and SibSp
- Overlaid age distributions for survivors vs non-survivors
- Built a correlation heatmap across all numeric features

## Key Findings

- Overall survival rate: **[FILL IN]%**
- Female survival rate was significantly higher than male
- 1st class passengers survived at a much higher rate than 3rd class
- Fare was positively correlated with survival; Pclass was negatively correlated

## Challenges

The biggest decision was how to handle 177 missing Age values. I used the column median instead of mean since the age data was skewed, and the mean gets pulled by extreme values.

Also ran into a `FutureWarning` with `df.corr()` — fixed by passing `numeric_only=True`.

## How to Run

```bash
pip install pandas matplotlib seaborn
jupyter notebook Titanic.ipynb


