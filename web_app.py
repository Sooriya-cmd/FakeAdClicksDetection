"""Local interactive demo for the trained fake-click classifier."""

from bisect import bisect_left
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, jsonify, render_template, request


ROOT = Path(__file__).resolve().parent
TRAIN_DATA_PATH = ROOT / "Data_dir" / "fake_users.csv"
TEST_DATA_PATH = ROOT / "Data_dir" / "fake_users_test.csv"
MODEL_PATH = ROOT / "saved_models" / "click_model" / "1"
EVENTS = (
    "click_ad",
    "click_carrousel",
    "phone_call",
    "send_email",
    "send_sms",
)
CATEGORIES = ("Holidays", "Jobs", "Leisure", "Motor", "Phone", "Real_State")
OUTPUT_NAME = "dense_4"


def create_app() -> Flask:
    """Load the model and data once, then expose the local demo and scorer."""
    if not TRAIN_DATA_PATH.is_file():
        raise FileNotFoundError(f"Training data not found: {TRAIN_DATA_PATH}")
    if not TEST_DATA_PATH.is_file():
        raise FileNotFoundError(f"Test data not found: {TEST_DATA_PATH}")
    if not (MODEL_PATH / "saved_model.pb").is_file():
        raise FileNotFoundError(
            f"Trained model not found at {MODEL_PATH}. "
            "Train it first with `python main.py --train`."
        )

    train_data = pd.read_csv(TRAIN_DATA_PATH)
    test_data = pd.read_csv(TEST_DATA_PATH)
    user_ids = sorted(train_data["UserId"].astype(str).unique().tolist())
    if len(user_ids) < 2:
        raise ValueError("Training data must contain at least two distinct users.")

    loaded_model = tf.saved_model.load(str(MODEL_PATH))
    if "serving_default" not in loaded_model.signatures:
        raise ValueError(f"The saved model at {MODEL_PATH} has no serving_default signature.")
    serving = loaded_model.signatures["serving_default"]
    input_names = serving.structured_input_signature[1]
    if "dense_input" not in input_names:
        raise ValueError(f"Unexpected model input signature: {input_names}")
    if OUTPUT_NAME not in serving.structured_outputs:
        raise ValueError(
            f"Expected model output {OUTPUT_NAME!r}; "
            f"found {tuple(serving.structured_outputs)}."
        )

    app = Flask(__name__)

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/api/summary")
    def summary():
        return jsonify(
            {
                "training_records": int(len(train_data)),
                "test_records": int(len(test_data)),
                "user_profiles": int(len(user_ids)),
                "feature_count": 12,
            }
        )

    @app.get("/api/options")
    def options():
        positions = np.linspace(0, len(user_ids) - 1, num=min(12, len(user_ids)))
        sample_users = [user_ids[int(position)] for position in positions]
        return jsonify(
            {
                "events": EVENTS,
                "categories": CATEGORIES,
                "users": sample_users,
                "default_user": sample_users[len(sample_users) // 2],
            }
        )

    @app.post("/api/predict")
    def predict():
        payload = request.get_json()
        if not isinstance(payload, dict):
            return jsonify({"error": "Send a JSON object with user_id, event, and category."}), 400

        user_id = str(payload.get("user_id", ""))
        event = payload.get("event")
        category = payload.get("category")
        if user_id not in user_ids:
            return jsonify({"error": "Choose a user profile from the training data."}), 400
        if event not in EVENTS:
            return jsonify({"error": "Choose one of the listed click events."}), 400
        if category not in CATEGORIES:
            return jsonify({"error": "Choose one of the listed ad categories."}), 400

        user_rank = bisect_left(user_ids, user_id)
        features = np.zeros(12, dtype=np.float32)
        features[0] = user_rank / (len(user_ids) - 1)
        features[1 + EVENTS.index(event)] = 1.0
        features[6 + CATEGORIES.index(category)] = 1.0
        prediction = serving(
            dense_input=tf.convert_to_tensor(features.reshape(1, -1), dtype=tf.float32)
        )[OUTPUT_NAME]
        score = float(prediction.numpy()[0, 0])
        return jsonify(
            {
                "score": score,
                "prediction": "Fake click" if score >= 0.5 else "Legitimate click",
                "is_fake": score >= 0.5,
                "threshold": 0.5,
                "event": event,
                "category": category,
                "user_id": user_id,
            }
        )

    return app
