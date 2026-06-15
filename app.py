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
# ANALYSIS
# ------------------------
if st.button("Analyze"):

    risk_level = "CRITICAL"

    if "temperature" in sensor.lower() or "110" in sensor:
        risk_level = "CRITICAL"

    st.success("Analysis Complete")

    st.markdown(f"""
# 🔍 Maintenance Analysis Report

## Equipment
**{equipment}**

## Probable Fault
Bearing wear, lubrication failure, or shaft misalignment.

## Root Cause Analysis
The reported overheating combined with excessive vibration suggests abnormal mechanical stress on rotating components. This is commonly caused by:

- Bearing degradation
- Poor lubrication
- Shaft misalignment
- Rotor imbalance
- Excessive load conditions

## Risk Level
🔴 **{risk_level}**

## Immediate Actions
- Stop equipment if vibration increases further.
- Inspect bearings immediately.
- Verify lubrication condition.
- Check shaft alignment.
- Perform thermal inspection.

## Long-Term Recommendations
- Implement predictive maintenance.
- Install vibration monitoring sensors.
- Schedule monthly thermal inspections.
- Track historical maintenance logs.

## Spare Parts Recommendation
- Bearing replacement kit
- Lubrication assembly
- Coupling components
- Alignment tools

## Preventive Maintenance Suggestions
- Weekly vibration inspection
- Monthly temperature analysis
- Quarterly bearing health check
- Semi-annual alignment verification

## Estimated Downtime Risk
High probability of equipment failure within the next maintenance cycle if corrective action is not taken.

## Executive Summary
The equipment is operating under potentially unsafe conditions. Immediate inspection and corrective maintenance are recommended to avoid unexpected downtime and production losses.
""")

# ------------------------
# FOOTER
# ------------------------
st.markdown("---")
st.caption("SteelSense AI | Hackathon Demo Project")
