import re
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in ENGLISH_STOP_WORDS]
    return " ".join(tokens)
