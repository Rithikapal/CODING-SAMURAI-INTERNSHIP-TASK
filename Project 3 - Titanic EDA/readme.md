# Titanic - Exploratory Data Analysis 🚢

Exploratory data analysis on the Titanic passenger dataset to uncover which demographic and ticket-related factors most influenced survival, using missing value treatment, distribution plots, group-wise survival comparisons, and a correlation heatmap.

---

## Problem Statement

The Titanic disaster is one of history's most documented maritime tragedies — but numbers tell a story that headlines don't. Did wealth determine who lived? Did age matter less than gender? Did having family aboard change your odds? This analysis goes beyond surface-level observations and lets the data answer those questions directly through visual and statistical exploration.

---

## Dataset

- **Source:** [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)
- **File used:** `Titanic_train.csv`
- **Size:** 891 rows × 12 columns
- **Key columns used:**

| Column | Description |
|--------|-------------|
| `Survived` | 0 = Died, 1 = Survived (target variable) |
| `Pclass` | Passenger class (1st, 2nd, 3rd) |
| `Sex` | Gender |
| `Age` | Age in years (177 missing values — filled with median) |
| `SibSp` | Number of siblings/spouses aboard |
| `Fare` | Ticket price paid |

---

## Approach

1. **Loaded the dataset** using `pandas`, printed shape, column names, and missing value counts
2. **Handled missing values** — filled the 177 missing `Age` values using the overall column median
3. **Calculated overall survival rate** — `df['Survived'].mean() * 100`
4. **Plotted age distribution** — histogram of all passengers (bins=20)
5. **Plotted fare distribution** — histogram of ticket prices (bins=20)
6. **Compared survival by gender** — grouped bar chart of survival rate for male vs female
7. **Compared survival by class** — grouped bar chart of survival rate across 1st, 2nd, 3rd class
8. **Compared age distribution** — overlapping histogram for survived vs not-survived passengers
9. **Analyzed survival by SibSp** — bar chart of survival rate by number of siblings/spouses aboard
10. **Built a correlation heatmap** — across all numeric features using seaborn

---

## Key Findings

- **Overall survival rate:** [FILL IN — run `round(df['Survived'].mean() * 100, 2)` from your output]
- **Female survival rate:** [FILL IN] vs **Male survival rate:** [FILL IN]
- **Survival by class:** 1st class [FILL IN]%, 2nd class [FILL IN]%, 3rd class [FILL IN]%
- **SibSp = 0 (alone) survival rate:** [FILL IN] — passengers with 1 sibling/spouse had a [higher/lower] rate
- **Age distribution:** Most passengers were between 20–40 years old; the age distributions of survivors and non-survivors overlapped significantly with children showing slightly better survival
- **Fare:** Positively correlated with survival — higher-paying passengers survived at higher rates
- **Pclass:** Negatively correlated with survival — higher class number (3rd) means lower survival odds

---

## What I Learned

[Write 3–5 sentences in your own words after running the notebook. Prompts: Were the gender and class findings as stark as expected? What did the SibSp survival chart show — did having family help or hurt? Did the correlation heatmap confirm or contradict what the individual charts showed?]

---

## Challenges Faced

> This section documents real decisions and errors during the project — the kind that don't show up in clean tutorials.

- **`df.corr()` deprecation warning**
  When I ran `sns.heatmap(df.corr())`, pandas raised a `FutureWarning` about `numeric_only` defaulting to False. Fixed by explicitly passing `df.corr(numeric_only=True)` — without it the heatmap threw an error on the non-numeric columns like `Sex` and `Name`.

- **Age missing values — why median and not mean?**
  I first tried `df['Age'].mean()` to fill missing ages. The mean is pulled upward by a few older passengers with high ages, so using the median (which is the middle value, not affected by extremes) felt more accurate for imputation. Switched to `df['Age'].median()` after checking both values.

- **`plt.show()` placement — charts appearing blank**
  On the first few charts I forgot to call `plt.show()` after setting the title/labels. The chart either appeared blank or got merged with the next one. Fixed by making sure every chart block ends with `plt.show()` before starting a new `plt.figure()`.

- **Reading `df.isnull().sum()` output**
  The output lists every column — I initially only looked at `Age` and missed `Cabin` (687 missing) and `Embarked` (2 missing) which appear lower in the list. Learned to read the full output, not just the top.

- [Add your own — e.g. a chart axis label that was wrong, a column you printed and misread, something you had to re-run]

---

## How to Run

```bash
pip install pandas matplotlib seaborn
```

Update the file path in the notebook (cell 2) from the original Windows path to wherever you saved the CSV:
```python
df = pd.read_csv("Titanic_train.csv")
```

Then run all cells top to bottom:
```bash
jupyter notebook Titanic.ipynb
```

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
