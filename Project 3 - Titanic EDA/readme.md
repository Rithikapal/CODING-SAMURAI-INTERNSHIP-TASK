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


---
*Coding Samurai Data Science Internship — Project 3*

**Dataset:** Download `train.csv` from [Kaggle Titanic](https://www.kaggle.com/c/titanic/data).

---

## Screenshots

<img width="1049" height="924" alt="image" src="https://github.com/user-attachments/assets/b39b43d9-4dbc-44d9-b3bd-e32fc4f489e7" />

<img width="1068" height="702" alt="image" src="https://github.com/user-attachments/assets/ca03af02-77b0-43b3-866b-4c723d568707" />

<img width="1058" height="727" alt="image" src="https://github.com/user-attachments/assets/674c3596-2b1a-449a-9586-3711cad6b4de" />

<img width="1015" height="841" alt="image" src="https://github.com/user-attachments/assets/f0cf9255-d41a-4e98-9283-ad0546b41508" />

<img width="1005" height="830" alt="image" src="https://github.com/user-attachments/assets/ac893ea5-6a0b-4301-8043-50f461fc5281" />

<img width="1086" height="712" alt="image" src="https://github.com/user-attachments/assets/7c28249f-8902-4b89-bad6-5a1d546f5a24" />

<img width="1026" height="879" alt="image" src="https://github.com/user-attachments/assets/11802666-b6e2-44d5-bf09-c6ae930a5d45" />

<img width="539" height="327" alt="image" src="https://github.com/user-attachments/assets/96267ddb-7295-4546-ab34-b2b56a05295a" />

---
