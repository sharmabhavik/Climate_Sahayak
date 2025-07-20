#!/bin/bash
echo "🚀 Starting FastAPI and Streamlit..."

# Run FastAPI in background
uvicorn backend.fastapi_api:app --host 0.0.0.0 --port 8000 &

# Run Streamlit (foreground keeps container alive)
streamlit run frontend/streamlit_app.py
