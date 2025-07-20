# === agent/nodes/parse_text_node.py ===
from typing import Dict
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json

# Initialize LLM (you can switch model as needed)
llm = Ollama(model="mistral")

# Prompt to extract region and year from free text
prompt = PromptTemplate.from_template(
    """
    You are a helpful AI assistant. Extract the following from user query:
    - region_name (state, country, or city)
    - year (numerical, like 2050)
    - task (either "predict", "recommend", or both)

    User query: {query}

    Respond ONLY in valid JSON format:
    {{"region_name": "<region>", "year": <year>, "task": ["predict", "recommend"]}}
    """
)

extract_chain = LLMChain(llm=llm, prompt=prompt)

def parse_text_node(state: Dict) -> Dict:
    print("🔁 <NodeName> state:", state)
    """
    LangGraph node: parses free text query and extracts structured info
    Required input: { "query": "..." }
    """
    query = state.get("query")
    if not query:
        raise ValueError("Missing user query.")

    response = extract_chain.run({"query": query})
    try:
        parsed = json.loads(response)  # Safer than eval()
        if not all(key in parsed for key in ["region_name", "year", "task"]):
            raise ValueError("Missing one or more required fields in parsed output")
        state.update(parsed)
    except Exception as e:
        raise ValueError(f"❌ Could not parse agent input: {e}\nRaw LLM Output: {response}")

    return state
