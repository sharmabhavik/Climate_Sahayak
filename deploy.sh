#!/bin/bash

# === deploy.sh ===
# 🌍 Deployment script for Climate Agent AI

echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📥 Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# 🧠 Start FastAPI backend
echo "🚀 Launching FastAPI backend..."
gnome-terminal -- bash -c "source venv/bin/activate && uvicorn backend.fastapi_api:app --reload; exec bash"

# 🌐 Start Streamlit frontend
echo "🖥️ Launching Streamlit frontend..."
gnome-terminal -- bash -c "source venv/bin/activate && streamlit run frontend/streamlit_app.py; exec bash"
