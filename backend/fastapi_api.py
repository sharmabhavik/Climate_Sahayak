from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="🌍 Climate Agent API (Dummy Mode)", version="1.0")

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class AgentQuery(BaseModel):
    query: str

@app.post("/run-agent")
async def run_agent(query: AgentQuery):
    return {
        "result": f"""
### 🌍 Climate Forecast for: `{query.query}`

**🌡️ Predicted Temperature Rise**: `2.8°C`

**📊 Key Indicators:**
- Total GHG: 49.1  
- Methane: 8.6  
- Nitrous Oxide: 2.2  
- Population: 1.4B  
- Energy Consumption: High  

---

### 🧠 AI Suggests:
- 🌱 Adopt renewable energy sources  
- 🚴 Promote sustainable transport  
- 🏭 Limit industrial emissions  
- 🌳 Afforestation & carbon credits  

"""
    }
