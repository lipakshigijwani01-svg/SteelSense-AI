import streamlit as st
import google.generativeai as genai

# --------------------
# PAGE CONFIG
# --------------------
st.set_page_config(
    page_title="SteelSense AI",
    layout="wide"
)

# --------------------
# GEMINI SETUP
# --------------------
try:
    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )

except Exception as e:
    st.error(f"Gemini Setup Error: {e}")
    st.stop()

# --------------------
# UI
# --------------------
st.title("🏭 SteelSense AI")
st.subheader(
    "AI-Powered Maintenance Wizard for Steel Manufacturing Plants"
)

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

# --------------------
# ANALYZE BUTTON
# --------------------
if st.button("Analyze"):

    with st.spinner("Analyzing equipment condition..."):

        prompt = f"""
You are a senior maintenance engineer working in a steel manufacturing plant.

Analyze the following equipment issue.

Equipment:
{equipment}

Fault Description:
{fault}

Sensor Data:
{sensor}

Provide a detailed report in the following format:

## Probable Fault

## Root Cause Analysis

## Risk Level
(Low / Medium / High / Critical)

## Immediate Actions

## Long-Term Recommendations

## Spare Parts Recommendation

## Preventive Maintenance Suggestions

## Maintenance Summary
"""

        try:

            response = model.generate_content(
                prompt
            )

            st.success(
                "Analysis Complete"
            )

            st.markdown(
                response.text
            )

        except Exception as e:

            st.error(
                f"Analysis Error: {str(e)}"
            )
