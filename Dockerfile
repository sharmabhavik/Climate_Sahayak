# === Dockerfile ===
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose backend (FastAPI) and frontend (Streamlit) ports
EXPOSE 8000 8501

# Launch both backend and frontend using a shell script
CMD ["bash", "./start.sh"]
