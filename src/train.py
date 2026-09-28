import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# -----------------------------------
# 1. Load processed dataset
# -----------------------------------

df = pd.read_csv("data/processed_feedback.csv")


# -----------------------------------
# 2. Convert text into TF-IDF numbers
# -----------------------------------

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["cleaned_feedback"])


# Target variable
y = df["category"]


# -----------------------------------
# 3. Split data into training/testing
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("Training records:", X_train.shape[0])
print("Testing records:", X_test.shape[0])


# -----------------------------------
# 4. Create Logistic Regression model
# -----------------------------------

model = LogisticRegression(
    max_iter=1000
)


# -----------------------------------
# 5. Train the model
# -----------------------------------

model.fit(X_train, y_train)

print("\nModel training completed!")


# -----------------------------------
# 6. Make predictions
# -----------------------------------

y_pred = model.predict(X_test)


# -----------------------------------
# 7. Evaluate the model
# -----------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the TF-IDF vectorizer
joblib.dump(
    vectorizer,
    "models/tfidf_vectorizer.pkl"
)

# Save the trained model
joblib.dump(
    model,
    "models/classification_model.pkl"
)

print("\nModel and vectorizer saved successfully!")