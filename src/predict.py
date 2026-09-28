import joblib

from preprocessing import clean_text
from routing import assign_priority, assign_department


# Load the saved TF-IDF vectorizer
vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

# Load the trained Logistic Regression model
model = joblib.load(
    "models/classification_model.pkl"
)


def predict_feedback(feedback):

    # Step 1: Clean the customer feedback
    cleaned_feedback = clean_text(feedback)

    # Step 2: Convert the cleaned text into TF-IDF numbers
    feedback_vector = vectorizer.transform(
        [cleaned_feedback]
    )

    # Step 3: Predict the category
    category = model.predict(
        feedback_vector
    )[0]

    # Step 4: Assign priority
    priority = assign_priority(category)

    # Step 5: Assign department
    department = assign_department(category)

    # Step 6: Return the complete result
    return {
        "feedback": feedback,
        "category": category,
        "priority": priority,
        "department": department
    }


# Test the prediction system directly
if __name__ == "__main__":

    feedback = "My payment was deducted twice"

    result = predict_feedback(feedback)

    print("\nPrediction Result:")
    print(result)