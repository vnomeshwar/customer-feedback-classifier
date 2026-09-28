import sqlite3
import pandas as pd


# Database location
DATABASE_PATH = "database/feedback.db"


def create_database():
    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feedback TEXT NOT NULL,
            cleaned_feedback TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Database and table created successfully!")


def insert_data():
    # Read our processed CSV
    df = pd.read_csv("data/processed_feedback.csv")

    # Connect to database
    connection = sqlite3.connect(DATABASE_PATH)

    # Insert the data into the feedback table
    df.to_sql(
        "feedback",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print(f"{len(df)} records inserted into database!")


if __name__ == "__main__":
    create_database()
    insert_data()