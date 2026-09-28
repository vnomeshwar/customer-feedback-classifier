import pandas as pd
from preprocessing import clean_text


# Read the original dataset
df = pd.read_csv("data/customer_feedback.csv")

print("Original number of rows:", len(df))


# Remove duplicate feedback
df = df.drop_duplicates(subset=["feedback"])

print("Rows after removing duplicates:", len(df))


# Clean the customer feedback
df["cleaned_feedback"] = df["feedback"].apply(clean_text)


# Display original and cleaned feedback
print("\nOriginal vs Cleaned Feedback:\n")

print(df[["feedback", "cleaned_feedback"]].head(10))


# Save the processed dataset
df.to_csv("data/processed_feedback.csv", index=False)

print("\nProcessed dataset saved successfully!")