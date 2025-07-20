# === agent/nodes/estimate_data_node.py ===
from typing import Dict
import pandas as pd
import os

# Load historical reference data
DATA_PATH = "data/df_clean.csv"
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError("❌ df_clean.csv not found in /data/")

df_ref = pd.read_csv(DATA_PATH)


def estimate_data_node(state: Dict) -> Dict:
    print("🔁 <NodeName> state:", state)
    """
    Estimate missing feature values for a region using the closest available year's data.
    If no exact year match, fallback to mean across the region.
    """
    region = state.get("region_name")
    year = state.get("year")
    missing = state.get("missing", [])

    if not region or not year:
        raise ValueError("Region name or year missing from state")

    region_df = df_ref[df_ref["country"].str.lower() == region.lower()]
    if region_df.empty:
        raise ValueError(f"No reference data found for region: {region}")

    for feature in missing:
        if feature not in region_df.columns:
            state[feature] = "unknown"
            continue

        # Get closest year
        region_df = region_df.dropna(subset=[feature])
        if region_df.empty:
            state[feature] = "unknown"
            continue

        closest_year_row = region_df.iloc[(region_df["year"] - year).abs().argsort()[:1]]
        est_value = closest_year_row[feature].values[0]

        state[feature] = round(est_value, 4) if pd.notnull(est_value) else "unknown"

    return state
