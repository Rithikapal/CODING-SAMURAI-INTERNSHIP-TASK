# Titanic - Survival Prediction with Logistic Regression

Built a classification model to predict Titanic passenger survival using engineered features and Logistic Regression.

## About the Project

Taking the EDA from Project 3 further, I built a machine learning model that predicts whether a passenger survived. The focus was on feature engineering — creating new meaningful columns from existing ones — and then training and evaluating a Logistic Regression model.

## Dataset

**Source:** [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)  
**File:** Titanic_train.csv — 891 rows

## What I Did

- Filled missing Age values using median
- Created `FamilySize` (SibSp + Parch + 1) and `IsAlone` flag
- Extracted passenger `Title` from the Name column using regex, grouped rare titles as 'Other'
- Encoded Sex and Title into numeric values
- Dropped PassengerId, Name, Ticket
- Split 80/20 train-test and trained Logistic Regression
- Evaluated with accuracy score, confusion matrix, and feature coefficient chart

## Key Findings

- Model accuracy: **[FILL IN]%**
- Confusion matrix: **[FILL IN]** correct predictions out of 179 test rows
- Sex and Title were the strongest predictors of survival
- Extracting Title gave the model a richer signal than raw gender alone

## Challenges

The notebook referenced `df["FamilySize"]` before it was ever created — threw a `KeyError` immediately. Fixed by adding `df["FamilySize"] = df["SibSp"] + df["Parch"] + 1` before that cell.

There was also a line-break typo in the barplot cell (`da` on one line, `ta=importance` on the next) that caused a `SyntaxError`. Fixed by putting `data=importance` on one line.

## How to Run

Before running, add this line before the `IsAlone` cell:
```python
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
```

Also fix the barplot typo — `data=importance` should be on one line.

```bash
pip install pandas matplotlib seaborn scikit-learn
jupyter notebook Titanic_Logistic.ipynb
```

---
*Coding Samurai Data Science Internship — Project 4*
