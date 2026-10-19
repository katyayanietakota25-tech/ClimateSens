from flask import Flask, render_template, request, jsonify
from pathlib import Path
import joblib
from train_model import ensure_model

app = Flask(__name__)
MODEL_PATH = Path("model_pipeline.joblib")

def load_pipeline():
    # Train the included demo model automatically if no saved model exists.
    ensure_model()
    return joblib.load(MODEL_PATH)

pipeline = load_pipeline()

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/predict")
def predict():
    payload = request.get_json(silent=True) or request.form
    text = (payload.get("text") or "").strip()
    if not text:
        return jsonify({"error": "Please enter a climate-related sentence."}), 400
    prediction = pipeline.predict([text])[0]
    confidence = None
    if hasattr(pipeline, "predict_proba"):
        probs = pipeline.predict_proba([text])[0]
        confidence = round(float(max(probs)) * 100, 1)
    return jsonify({
        "sentiment": str(prediction),
        "confidence": confidence,
        "note": "Demo model trained on a small illustrative dataset. Not the original research model."
    })

if __name__ == "__main__":
    app.run(debug=True)
