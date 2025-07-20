from typing import Dict

def response_node(state: Dict) -> Dict:
    print("🔁 ResponseNode state:", state)

    """
    Final LangGraph node to generate Markdown response.
    Combines prediction and policy into a rich result for frontend display.
    """

    # Fallbacks for missing values
    region = state.get("region_name", "Unknown Region")
    year = state.get("year", "Unknown Year")
    predicted_temp = state.get("predicted_temperature", "N/A")
    policy_suggestions = state.get("policy_suggestions", "⚠️ No suggestions generated.")

    response_md = f"""
### 🌍 Climate Forecast Summary: `{region}` ({year})

**🌡️ Predicted Temperature Rise**: `{predicted_temp}°C`

**📊 Key Contributing Factors:**
- Temperature Change from CO₂: `{state.get('temperature_change_from_co2', 'N/A')}`
- Temperature Change from CH₄: `{state.get('temperature_change_from_ch4', 'N/A')}`
- Temperature Change from N₂O: `{state.get('temperature_change_from_n2o', 'N/A')}`
- Total GHG: `{state.get('total_ghg', 'N/A')}`
- Methane: `{state.get('methane', 'N/A')}`
- Nitrous Oxide: `{state.get('nitrous_oxide', 'N/A')}`
- CO₂ Including LUC: `{state.get('co2_including_luc', 'N/A')}`
- Population: `{state.get('population', 'N/A')}`
- Energy Consumption: `{state.get('primary_energy_consumption', 'N/A')}`
- Oil CO₂: `{state.get('oil_co2', 'N/A')}`
- Gas CO₂: `{state.get('gas_co2', 'N/A')}`
- Coal CO₂: `{state.get('coal_co2', 'N/A')}`

---

### 🧠 AI-Recommended Policy:
{policy_suggestions}
""".strip()

    state["result"] = response_md
    return state
