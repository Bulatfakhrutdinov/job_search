import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class Vectorizer:
    def __init__(self, method='tfidf', max_features=10000):
        self.method = method
        self.vectorizer = None
        self.max_features = max_features

    def fit_corpus(self, texts):
        if self.method == 'tfidf':
            self.vectorizer = TfidfVectorizer(max_features=self.max_features)
            self.vectorizer.fit(texts)
        else:
            raise NotImplementedError(f"Method {self.method} not supported yet.")

    def transform(self, texts):
        if self.vectorizer is None:
            raise ValueError("Vectorizer is not fitted.")
        return self.vectorizer.transform(texts).toarray()

    def save(self, path):
        joblib.dump(self.vectorizer, path)

    def load(self, path):
        self.vectorizer = joblib.load(path)
