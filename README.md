# 🌍 Climate Forecast & Policy Agent

A fully agentic AI system built using **LangGraph**, **LangChain**, **FastAPI**, and **Streamlit** to predict temperature rise from GHG emissions and generate actionable climate policy recommendations. 

---

## 🧠 Project Overview

This AI-powered app:
- Accepts **natural language input** like "What will be the temperature rise in India by 2050?"
- Extracts relevant details (region, year, task)
- Predicts **temperature change** using a trained ML model (RandomForest)
- Estimates **missing GHG features** from historical data
- Generates **custom climate policies** using an LLM (e.g., Mistral via Ollama)
- Outputs a full **markdown response** for frontend display

---

## 📁 Folder Structure

```bash
climate-agent-app/
├── agent/
│   ├── agent_graph.py           # LangGraph pipeline
│   └── nodes/                   # Individual LangGraph nodes
│       ├── check_data_node.py
│       ├── estimate_data_node.py
│       ├── parse_text_node.py
│       ├── policy_node.py
│       ├── predict_node.py
│       └── response_node.py
├── backend/
│   └── fastapi_api.py          # API endpoint to trigger agent
├── frontend/
│   └── streamlit_app.py        # UI to interact with the agent
├── data/
│   └── df_clean.csv            # Historical GHG dataset
├── models/
│   └── temp_predictor.pkl      # Trained RandomForest model
├── tests/
│   └── test_agent.py           # Agent test script
├── start.sh                    # Startup script for API + frontend
├── requirements.txt            # Dependencies
├── Dockerfile                  # Docker setup
└── README.md                   # You are here ✅
```

---

## 🚀 How to Run (Locally)

### Step 1: Clone and Setup
```bash
git clone https://github.com/your-username/climate-agent-app.git
cd climate-agent-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Start FastAPI + Streamlit
```bash
bash start.sh
```
- FastAPI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Streamlit: [http://localhost:8501](http://localhost:8501)

### Step 3: Query Example
```json
{
  "query": "Forecast climate change in Gujarat for 2040."
}
```

---

## 🧪 Running Tests
```bash
python tests/test_agent.py
```

---

## 🐳 Docker (Optional)
```bash
docker build -t climate-agent .
docker run -p 8000:8000 -p 8501:8501 climate-agent
```

---

## 📊 Powered By
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://www.langchain.com/)
- [Ollama + Mistral](https://ollama.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)

---

## 🌱 SDG 13 Impact
This project contributes to **Sustainable Development Goal 13: Climate Action** by:
- Predicting regional temperature changes based on emissions
- Suggesting proactive policy steps to reduce climate impact
- Enabling data-driven decision making for researchers & policymakers

---

## 🧠 Contributors
Built by Bhavik, guided by Agentic AI principles.

---

## 📬 License
MIT License - free to use, modify, and distribute
