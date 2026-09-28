from fastapi import FastAPI
from pydantic import BaseModel

import sys
import os

# Add the src folder to Python's path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from predict import predict_feedback


# Create FastAPI application
app = FastAPI(
    title="Intelligent Customer Feedback Classification API",
    description="API for classifying and routing customer feedback",
    version="1.0.0"
)


# Define the request format
class FeedbackRequest(BaseModel):
    feedback: str


# Test endpoint
@app.get("/")
def home():
    return {
        "message": "Customer Feedback Classification API is running!"
    }


# Prediction endpoint
@app.post("/predict")
def predict(request: FeedbackRequest):

    result = predict_feedback(
        request.feedback
    )

    return result