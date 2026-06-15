import streamlit as st

# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="SteelSense AI",
    layout="wide"
)

# ------------------------
# HEADER
# ------------------------
st.title("🏭 SteelSense AI")
st.subheader("AI-Powered Maintenance Wizard for Steel Manufacturing Plants")

# ------------------------
# SIDEBAR
# ------------------------
st.sidebar.title("Plant Dashboard")
st.sidebar.metric("Active Alerts", "3")
st.sidebar.metric("Critical Assets", "1")
st.sidebar.metric("Plant Risk", "HIGH")

# ------------------------
# INPUTS
# ------------------------
equipment = st.text_input(
    "Equipment Name",
    value="Rolling Mill Motor"
)

fault = st.text
