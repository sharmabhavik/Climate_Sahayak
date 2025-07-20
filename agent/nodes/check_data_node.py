# === agent/nodes/check_data_node.py ===
from typing import Dict

REQUIRED_FEATURES = [
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


def check_data_node(state: Dict) -> Dict:
    print("🔁 <NodeName> state:", state)
    """
    LangGraph node to check which key input features are missing.
    Assumes structured keys like emissions, energy, population etc. will be present or missing.
    Appends missing keys into state["missing"]
    """
    missing = []
    for feature in REQUIRED_FEATURES:
        if feature not in state or state[feature] is None:
            missing.append(feature)

    state["missing"] = missing
    return state