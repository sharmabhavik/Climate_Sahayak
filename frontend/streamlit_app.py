import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import re

st.set_page_config(page_title="🌱 Climate Agentic AI", layout="wide")
st.title("🌍 Climate Forecast & Policy Generator")

# === Agentic Query Section ===
st.markdown("### 💬 Ask Anything About Climate")
user_query = st.text_area("Enter your query:", "What will be the climate in Gujarat in 2050?")

# Extract country/region
region = "India"
match = re.search(r"in\s+([A-Za-z\s]+?)(?:\s+\d{4}|[?.!]|$)", user_query, re.IGNORECASE)
if match:
    region = match.group(1).strip().title()

# Run agent on button click
if st.button("🚀 Run Agent"):
    with st.spinner("Analyzing climate data using agentic reasoning..."):
        try:
            response = requests.post("http://localhost:8000/run-agent", json={"query": user_query})
            if response.status_code == 200:
                result = response.json().get("result", "No result returned.")
                st.success("✅ Agent responded!")
                st.markdown(result, unsafe_allow_html=True)
            else:
                st.error("❌ Agent returned error.")
        except Exception as e:
            st.error(f"❌ Backend not reachable: {e}")

st.markdown("---")

# === Load DataFrame ===
try:
    df = pd.read_csv("data/df_clean.csv")
except Exception as e:
    st.error(f"❌ Could not load data: {e}")
    st.stop()

# === Right Column Only ===
st.subheader("🗺️ Avg Temperature Change by Country")
try:
    world_avg = df[df["year"] > 2000].groupby("country")["temperature_change_from_ghg"].mean().reset_index()
    fig_map = px.choropleth(
        world_avg,
        locations="country",
        locationmode="country names",
        color="temperature_change_from_ghg",
        color_continuous_scale="RdYlBu_r",
        height=500
    )
    st.plotly_chart(fig_map, use_container_width=True)
except Exception as e:
    st.warning(f"Could not load map: {e}")

# === Footer ===
st.markdown("---")
st.markdown("📌 Powered by LangGraph · LangChain · Streamlit · FastAPI · Agentic AI")
