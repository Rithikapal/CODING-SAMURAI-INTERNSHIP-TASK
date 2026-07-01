# Twitter Sentiment Analysis

Classified 10,000 tweets as Positive, Negative, or Neutral using TextBlob and measured accuracy against real labels from the Sentiment140 dataset.

## About the Project

I built a sentiment analysis pipeline on a sample of the Sentiment140 dataset — 1.6 million tweets, of which I used 10,000. Each tweet gets scored for polarity using TextBlob, classified into a sentiment category, and the predictions are compared against the original human labels to measure accuracy.

## Dataset

**Source:** [Kaggle — Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140)  
**File:** training.1600000.processed.noemoticon.csv  
**Sample used:** 10,000 tweets (random_state=42)

## What I Did

- Loaded the dataset with `encoding='latin-1'` and manually assigned column names (no header row in file)
- Sampled 10,000 rows for faster processing
- Remapped label 4 → 1 (original uses 0 and 4, not 0 and 1)
- Defined a `get_sentiment()` function using TextBlob polarity
- Applied it to every tweet and stored predictions
- Visualized sentiment distribution with a count plot
- Compared predictions against original labels to calculate accuracy

## Key Findings

- Sentiment breakdown: **[FILL IN]** Positive / **[FILL IN]** Negative / **[FILL IN]** Neutral
- Accuracy vs original labels: **[FILL IN]%**
- TextBlob on raw uncleaned tweets typically lands around 60–68% — expected for rule-based scoring on informal text

## Challenges

First load threw a `UnicodeDecodeError` — fixed with `encoding='latin-1'`. Then accessing `df['text']` gave a `KeyError` because the file has no headers — fixed by passing column names manually in `read_csv`.

The accuracy result initially made no sense (near 50%) — turns out the original labels use 0 and 4, not 0 and 1. Added `df['sentiment'].replace(4, 1)` before the accuracy check and it worked correctly.

There's also a `train_test_split` cell in the notebook that references undefined variables — skip that cell, it doesn't belong in a TextBlob pipeline.

## How to Run

Skip the `train_test_split` cell — it will throw a `NameError`.

```bash
pip install pandas matplotlib seaborn textblob
jupyter notebook Sentiment_Analysis.ipynb
```

---
*Coding Samurai Data Science Internship — Project 6*
