import pandas as pd
from preprocess import clean_text
from vectorizer import Vectorizer
import numpy as np

df = pd.read_csv("job_postings.csv", sep=';', encoding="utf-8")
df = df.sample(n=50000, random_state=42)

texts = df["description"].dropna().apply(clean_text).tolist()

vec = Vectorizer(method="tfidf")
vec.fit_corpus(texts)

X = vec.transform(texts)

vec.save("tfidf_model.pkl")
np.save("job_vectors.npy", X)

print("TF-IDF векторы сохранены в job_vectors.npy")
