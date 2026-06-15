import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")
st.title("🏭 SteelSense AI")
st.subheader("AI-Powered Maintenance Wizard for Steel Plants")

st.sidebar.title("Plant Dashboard")
st.sidebar.metric("Active Alerts", "3")
st.sidebar.metric("Critical Assets", "1")
st.sidebar.metric("Plant Risk", "HIGH")

equipment = st.text_input("Equipment Name")

fault = st.text_area(
    "Describe Fault",
    placeholder="Motor overheating and excessive vibration"
)

sensor = st.text_area(
    "Sensor Data",
    placeholder="Temperature=110°C, Vibration=High"
)

uploaded_file = st.file_uploader(
    "Upload Maintenance Log / SOP / Manual",
    type=["txt", "pdf"]
)

if st.button("Analyze"):

    prompt = f"""
    You are a maintenance engineer in a steel manufacturing plant.

    Equipment: {equipment}

    Fault: {fault}

    Sensor Data:
    {sensor}

    Provide:

    1. Probable Fault
    2. Root Cause Analysis
    3. Risk Level (Low/Medium/High/Critical)
    4. Immediate Actions
    5. Long-Term Recommendations
    6. Spare Parts Recommendation
    """

    response = model.generate_content(prompt)

    st.markdown(response.text)
