from pathlib import Path
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

DATA_PATH = Path("data/demo_climate_sentiment.csv")
MODEL_PATH = Path("model_pipeline.joblib")

def ensure_model():
    if MODEL_PATH.exists():
        return
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=["text", "sentiment"])
    X = df["text"].astype(str)
    y = df["sentiment"].astype(str)
    # Demo-only baseline: this does NOT reproduce the paper's BiLSTM/stacking results.
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2), sublinear_tf=True)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ])
    pipeline.fit(X, y)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Saved demo model to {MODEL_PATH}")
    print("IMPORTANT: trained on a small illustrative dataset, not the original research dataset.")

if __name__ == "__main__":
    ensure_model()
    df = pd.read_csv(DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["sentiment"], test_size=0.2, random_state=42, stratify=df["sentiment"]
    )
    evaluation_pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2), sublinear_tf=True)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ])
    evaluation_pipeline.fit(X_train, y_train)
    predictions = evaluation_pipeline.predict(X_test)
    print("Demo test accuracy:", round(accuracy_score(y_test, predictions), 3))
    print(classification_report(y_test, predictions, zero_division=0))
