import streamlit as st
import google.generativeai as genai

# Page Setup
st.set_page_config(page_title="SteelSense AI", layout="wide")

# Gemini Setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

# UI
st.title("🏭 SteelSense AI")
st.subheader("AI-Powered Maintenance Wizard for Steel Plants")

# Sidebar
st.sidebar.title("Plant Dashboard")
st.sidebar.metric("Active Alerts", "3")
st.sidebar.metric("Critical Assets", "1")
st.sidebar.metric("Plant Risk", "HIGH")

# Inputs
equipment = st.text_input(
    "Equipment Name",
    placeholder="Rolling Mill Motor"
)

fault = st.text_area(
    "Describe Fault",
    placeholder="Abnormal vibration and overheating"
)

sensor = st.text_area(
    "Sensor Data",
    placeholder="Temperature=110°C, Vibration=High"
)

uploaded_file = st.file_uploader(
    "Upload Maintenance Log / SOP / Manual",
    type=["txt", "pdf"]
)

# Analyze Button
if st.button("Analyze"):

    if not equipment or not fault:
        st.warning("Please enter equipment details and fault description.")
        st.stop()

    with st.spinner("Analyzing equipment..."):

        prompt = f"""
You are a senior maintenance engineer working in a steel manufacturing plant.

Analyze the following issue.

Equipment:
{equipment}

Fault Description:
{fault}

Sensor Data:
{sensor}

Provide your answer in this format:

## Probable Fault

## Root Cause Analysis

## Risk Level
(Low / Medium / High / Critical)

## Immediate Actions

## Long-Term Recommendations

## Spare Parts Recommendation

## Preventive Maintenance Suggestions
"""

        try:
            response = model.generate_content(prompt)

            st.success("Analysis Complete")

            st.markdown(response.text)

        except Exception as e:
            st.error(f"Gemini Error: {str(e)}")
