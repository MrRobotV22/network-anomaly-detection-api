from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Logging setup
logging.basicConfig(level=logging.INFO)

# Load model pipeline and default values
model = joblib.load("/Users/mohit/Documents/VS Code/DS_Project/models/rf_model.pkl")
defaults = joblib.load("/Users/mohit/Documents/VS Code/DS_Project/models/default_values.pkl")

# Column definitions
num_cols = ["count", "serrorrate", "srcbytes", "dstbytes", "duration"]
cat_cols = ["protocoltype", "service", "flag"]
expected_cols = num_cols + cat_cols


@app.route("/")
def home():
    return "Network Anomaly Detection API is running 🚀"


@app.route("/health")
def health():
    return {"status": "ok"}


# View expected features + defaults
@app.route("/defaults", methods=["GET"])
def get_defaults():
    return jsonify({
        "expected_features": expected_cols,
        "default_values": defaults
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        df = pd.DataFrame([data])

        # Identify missing columns
        missing = [col for col in expected_cols if col not in df.columns]
        if missing:
            app.logger.warning(f"Missing columns: {missing}")

        # Fill using trained defaults (median/mode)
        for col in expected_cols:
            if col not in df.columns:
                df[col] = defaults[col]

        # Ensure correct order
        df = df[expected_cols]

        # Prediction (pipeline handles preprocessing)
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0].max()

        result = {
            "prediction": "Anomaly" if prediction == 1 else "Normal",
            "confidence": round(float(probability), 4),
            "used_defaults_for": missing
        }

        return jsonify(result)

    except Exception as e:
        app.logger.error(str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)