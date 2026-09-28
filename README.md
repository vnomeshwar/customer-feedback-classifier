# Intelligent Customer Feedback Classification and Routing System

An end-to-end Machine Learning and NLP project that automatically classifies customer feedback, assigns priority, and routes the feedback to the appropriate department.

## Overview

The system takes customer feedback as input and performs:

```text
Customer Feedback
       ↓
Text Preprocessing
       ↓
TF-IDF Feature Extraction
       ↓
Logistic Regression
       ↓
Category Prediction
       ↓
Priority & Department Routing
       ↓
FastAPI
```

### Example

**Input:**

```text
"My payment was deducted twice"
```

**Output:**

```text
Category: Refund
Priority: High
Department: Finance
```

## Categories

| Category        | Priority | Department       |
| --------------- | -------- | ---------------- |
| Technical Issue | High     | Tech Support     |
| Refund          | High     | Finance          |
| Complaint       | Medium   | Customer Success |
| Praise          | Low      | Customer Success |

## Tech Stack

* Python
* Pandas
* NLTK
* Scikit-learn
* TF-IDF
* Logistic Regression
* SQLite
* FastAPI
* Uvicorn
* Joblib

## Project Structure

```text
customer-feedback-classifier/
│
├── api/
│   └── main.py
├── data/
│   ├── customer_feedback.csv
│   └── processed_feedback.csv
├── database/
├── models/
├── src/
│   ├── preprocessing.py
│   ├── etl.py
│   ├── database.py
│   ├── train.py
│   ├── predict.py
│   ├── routing.py
│   └── check_database.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## How to Run

### 1. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the pipeline

```bash
python src/etl.py
python src/database.py
python src/train.py
```

### 4. Start the API

```bash
uvicorn api.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Dataset

The current dataset contains **40 customer feedback records** across four categories, with 10 examples per category. It is designed to demonstrate the complete ML pipeline.

## Key Concepts Demonstrated

* Data preprocessing and ETL
* NLP text preprocessing
* TF-IDF feature extraction
* Machine Learning classification
* Business-rule based routing
* SQLite database integration
* REST API development with FastAPI


