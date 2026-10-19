<<<<<<< HEAD
# ClimateSense — Climate Change Sentiment Analysis Demo

This starter project provides a simple HTML/CSS/JavaScript front-end connected to a Python Flask API and a TF-IDF + Logistic Regression classifier.

## Important academic note
The research paper describes Logistic Regression, SVM, Naive Bayes, XGBoost, stacking, and BiLSTM, and reports BiLSTM accuracy of 96% and stacking accuracy of 95%. This starter application does **not** reproduce the original experiment: the original dataset and trained model were not supplied. It trains a small illustrative demo model from `data/demo_climate_sentiment.csv` so you can test the website end-to-end. Do not report the demo model's score as the paper's result.

## Run on Windows
1. Install Python 3.10 or newer.
2. Extract this ZIP to a folder.
3. Open Command Prompt in that folder.
4. Create a virtual environment (recommended):
   `python -m venv .venv`
5. Activate it:
   `.venv\\Scripts\\activate`
6. Install libraries:
   `pip install -r requirements.txt`
7. Start the website:
   `python app.py`
8. Open the local address shown in the terminal, usually `http://127.0.0.1:5000`.
9. Try the example buttons and enter your own climate-related sentence.

The first run automatically creates `model_pipeline.joblib`. You can also run `python train_model.py` to print a demo-only evaluation report.

## How the connection works
- `templates/index.html`: website layout.
- `static/style.css`: page styling.
- `static/script.js`: sends text to `/predict` using `fetch()`.
- `app.py`: Flask receives the text and invokes the trained pipeline.
- `train_model.py`: trains TF-IDF + Logistic Regression and saves the pipeline.
- `data/demo_climate_sentiment.csv`: small example dataset, created only to make the demo runnable.

## To use your real research dataset
Prepare a CSV with two columns named `text` and `sentiment`; labels must be `Positive`, `Negative`, or `Neutral`. Replace or rename the demo dataset and update `DATA_PATH` in `train_model.py`. Ensure the dataset is permitted for your use and has enough representative examples. Delete `model_pipeline.joblib` and run `python train_model.py` again after replacing data. Use a separate held-out test set for valid metrics.

## Suggested final-year project improvements
- Train and compare the models described in the paper.
- Use a fixed, documented train/test split (the paper describes 80:20).
- Report accuracy, precision, recall, F1-score, and confusion matrix from your actual experiments.
- Add data validation, model versioning, and tests.
- For deployment, turn off Flask debug mode and use a production WSGI server.

## Limitations
The included dataset is tiny and illustrative. Model confidence is a classifier probability, not a guarantee that the prediction is correct. Predictions can be wrong, especially for sarcasm, mixed opinions, abbreviations, or text outside the demo examples.
=======
# ClimateSens
>>>>>>> 0e82ad9651eb9ae834d60a1cd27f630db0e60591
