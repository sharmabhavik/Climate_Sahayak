# === agent/nodes/policy_node.py ===
from typing import Dict
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize LLM
llm = Ollama(model="mistral")

# Prompt for policy suggestions
prompt = PromptTemplate.from_template(
    """
    You are a climate policy advisor. Based on the following data, suggest 3 practical, region-specific policy actions to mitigate the predicted temperature rise:

    Region: {region}
    Year: {year}
    Predicted Temperature Rise: {temp}°C

    Greenhouse Gas Data:
    - Temperature Change from CO2: {co2_delta}
    - Temperature Change from CH4: {ch4_delta}
    - Temperature Change from N2O: {n2o_delta}
    - Total GHG: {total_ghg}
    - Methane: {methane}
    - Nitrous Oxide: {n2o}
    - CO2 Including LUC: {co2_incl_luc}

    Energy & Population Data:
    - Population: {population}
    - Energy Use: {energy_use}
    - Oil CO2: {oil_co2}, Gas CO2: {gas_co2}, Coal CO2: {coal_co2}

    Your response must be markdown formatted with a heading and a numbered list.
    """
)

chain = LLMChain(llm=llm, prompt=prompt)

def policy_node(state: Dict) -> Dict:
    print("🔁 <NodeName> state:", state)
    """
    LangGraph node: Generate region-specific climate policy recommendations using LLM.
    Requires all core GHG, energy, and temperature features.
    """
    response = chain.run({
        "region": state["region_name"],
        "year": state["year"],
        "temp": state["predicted_temperature"],
        "co2_delta": state.get("temperature_change_from_co2", "unknown"),
        "ch4_delta": state.get("temperature_change_from_ch4", "unknown"),
        "n2o_delta": state.get("temperature_change_from_n2o", "unknown"),
        "total_ghg": state.get("total_ghg", "unknown"),
        "methane": state.get("methane", "unknown"),
        "n2o": state.get("nitrous_oxide", "unknown"),
        "co2_incl_luc": state.get("co2_including_luc", "unknown"),
        "population": state.get("population", "unknown"),
        "energy_use": state.get("primary_energy_consumption", "unknown"),
        "oil_co2": state.get("oil_co2", "unknown"),
        "gas_co2": state.get("gas_co2", "unknown"),
        "coal_co2": state.get("coal_co2", "unknown")
    })

    state["policy_suggestions"] = response.strip()
    return state
