import re
import nltk
from nltk.corpus import stopwords

# Download English stopwords
nltk.download("stopwords")

# Get the list of English stopwords
stop_words = set(stopwords.words("english"))

# Keep important negation words
negation_words = {"not", "no", "never"}

stop_words = stop_words - negation_words


def clean_text(text):

    # 1. Convert text to lowercase
    text = text.lower()

    # 2. Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # 3. Split the sentence into individual words
    words = text.split()

    # 4. Remove stopwords
    words = [word for word in words if word not in stop_words]

    # 5. Join the words back together
    text = " ".join(words)

    # 6. Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# Test the function
if __name__ == "__main__":

    test_text = "The payment is not working for my account!"

    cleaned_text = clean_text(test_text)

    print("Original:", test_text)
    print("Cleaned :", cleaned_text)