# === agent/agent_graph.py ===
from langgraph.graph import StateGraph, END
from agent.nodes.parse_text_node import parse_text_node
from agent.nodes.check_data_node import check_data_node
from agent.nodes.estimate_data_node import estimate_data_node
from agent.nodes.predict_node import predict_node
from agent.nodes.policy_node import policy_node
from agent.nodes.response_node import response_node

# Define the shared state type
State = dict

# Create the LangGraph workflow
workflow = StateGraph(State)

# Register nodes
workflow.add_node("ParseText", parse_text_node)
workflow.add_node("CheckData", check_data_node)
workflow.add_node("EstimateMissing", estimate_data_node)
workflow.add_node("PredictTemp", predict_node)
workflow.add_node("GeneratePolicy", policy_node)
workflow.add_node("RespondFinal", response_node)

# Define the flow
workflow.set_entry_point("ParseText")
workflow.add_edge("ParseText", "CheckData")
workflow.add_edge("CheckData", "EstimateMissing")
workflow.add_edge("EstimateMissing", "PredictTemp")
workflow.add_edge("PredictTemp", "GeneratePolicy")
workflow.add_edge("GeneratePolicy", "RespondFinal")
workflow.add_edge("RespondFinal", END)

# Compile the agent
climate_agent = workflow.compile()
