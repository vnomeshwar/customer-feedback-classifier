import sqlite3
import pandas as pd


DATABASE_PATH = "database/feedback.db"


# Connect to the database
connection = sqlite3.connect(DATABASE_PATH)


# Read data from the feedback table
df = pd.read_sql_query(
    "SELECT * FROM feedback",
    connection
)


# Close the connection
connection.close()


# Display the data
print(df.head())

print("\nTotal records:", len(df))

print("\nCategories:")
print(df["category"].value_counts())