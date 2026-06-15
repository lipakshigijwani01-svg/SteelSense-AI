import streamlit as st
from google import genai

# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="SteelSense AI",
    layout="wide"
)

# ------------------------
# GEMINI CLIENT
# ------------------------
try:
    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )
except Exception as e:
    st.error(f"Gemini Setup Error: {e}")
    st.stop()

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

fault = st.text_area(
    "Describe Fault",
    value="Abnormal vibration and overheating"
)

sensor = st.text_area(
    "Sensor Data",
    value="Temperature=110°C, Vibration=High"
)

uploaded_file = st.file_uploader(
    "Upload Maintenance Log / SOP / Manual",
    type=["txt", "pdf"]
)

# ------------------------
# ANALYZE
# ------------------------
if st.button("Analyze"):

    prompt = f"""
You are a senior maintenance engineer in a steel manufacturing plant.

Equipment:
{equipment}

Fault Description:
{fault}

Sensor Data:
{sensor}

Provide:

1. Probable Fault
2. Root Cause Analysis
3. Risk Level (Low / Medium / High / Critical)
4. Immediate Actions
5. Long-Term Recommendations
6. Spare Parts Recommendation
7. Preventive Maintenance Suggestions

Format the response professionally.
"""

    try:

        with st.spinner("Analyzing equipment condition..."):

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            st.success("Analysis Complete")

            st.markdown(response.text)

    except Exception as e:

        st.error(f"Analysis Error: {e}")
