# Loading libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Loading dataset
df = pd.read_csv("Titanic_train.csv")

# Display first 5 rows
print(df.head())

print(df.columns.tolist())

# Fill missing age values using median age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Create IsAlone feature from FamilySize
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

# Extract passenger title from the Name column
df["Title"] = df["Name"].str.extract(" ([A-Za-z]+)\\.")

# Replace uncommon titles with 'Other' to reduce categories
df["Title"] = df["Title"].replace(
    ["Dr","Rev","Col","Major","Lady","Countess",
     "Jonkheer","Sir","Don","Capt"],
    "Other"
)

# Convert categorical gender values into numeric form
df["Sex"] = df["Sex"].map({
    "male":0,
    "female":1
})

# Convert title categories into numbers
title_map = {
    "Mr":0,
    "Miss":1,
    "Mrs":2,
    "Master":3,
    "Other":4
}
df["Title"] = df["Title"].map(title_map)
df["Title"] = df["Title"].fillna(4)

# Drop columns not required for prediction
df.drop(
    ["PassengerId","Name","Ticket"],
    axis=1,
    inplace=True
)

# Separate input features and target variable
X = df.drop("Survived", axis=1)
y = df["Survived"]
print(X.columns)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Generate predictions on test data
y_pred = model.predict(X_test)

# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", round(accuracy * 100, 2), "%")

# Visualize model performance using confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# Analyze which features influence predictions most
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

importance = importance.sort_values(
    by="Coefficient",
    ascending=False
)

print(importance)

# Create a bar chart to compare feature importance values
plt.figure(figsize=(8,5))
sns.barplot(
    x="Coefficient",
    y="Feature",
    data=importance
)
plt.title("Feature Importance")
plt.show()
