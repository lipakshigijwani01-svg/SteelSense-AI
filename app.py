import streamlit as st

st.set_page_config(page_title="SteelSense AI", layout="wide")

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

    st.success("Analysis Complete")

    st.markdown("""
### Probable Fault
Bearing Wear

### Risk Level
CRITICAL

### Immediate Action
Inspect bearing and lubrication system immediately.

### Long-Term Recommendation
Replace bearing and monitor vibration trend.

### Spare Parts Advice
Procure replacement bearing within 7 days.
""")
