from typing import Dict
import joblib
import numpy as np
import os

# Load trained ML model
MODEL_PATH = "models/temp_predictor.pkl"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("❌ ML model not found at models/temp_predictor.pkl")

model = joblib.load(MODEL_PATH)

# Define the order of input features used during training
FEATURE_ORDER = [
    "temperature_change_from_co2",
    "temperature_change_from_n2o",
    "total_ghg_excluding_lucf",
    "total_ghg",
    "temperature_change_from_ch4",
    "nitrous_oxide",
    "cumulative_co2_including_luc",
    "methane",
    "co2_including_luc",
    "oil_co2",
    "cumulative_co2",
    "cumulative_coal_co2",
    "gas_co2",
    "cumulative_luc_co2",
    "cumulative_oil_co2",
    "primary_energy_consumption",
    "coal_co2",
    "cumulative_flaring_co2",
    "flaring_co2",
    "cumulative_cement_co2",
    "cumulative_gas_co2",
    "population",
    "share_global_flaring_co2",
    "other_industry_co2"
]

def predict_node(state: Dict) -> Dict:
    print("🔁 [PredictNode] State before prediction:")
    for key in FEATURE_ORDER:
        print(f" - {key}: {state.get(key)}")

    try:
        input_vector = []
        for feature in FEATURE_ORDER:
            value = state.get(feature)

            # Validate value type and content
            if value is None:
                raise ValueError(f"❌ Feature '{feature}' is None.")

            str_val = str(value).strip().lower()

            if str_val in ["none", "unknown", "", "nan"]:
                raise ValueError(f"❌ Feature '{feature}' has invalid value: '{str_val}'")

            try:
                input_vector.append(float(value))
            except Exception as convert_error:
                raise ValueError(f"❌ Cannot convert feature '{feature}' to float: {value} — {convert_error}")

        X = np.array(input_vector).reshape(1, -1)
        prediction = model.predict(X)[0]
        state["predicted_temperature"] = round(prediction, 3)

    except Exception as e:
        raise ValueError(f"❌ Prediction failed: {e}")

    return state
