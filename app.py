import streamlit as st
import sqlite3
import pandas as pd

# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Hospital Management Dashboard",
    page_icon="🏥",
    layout="wide"
)

# -------------------------
# Title
# -------------------------

st.title("🏥 Hospital Management Dashboard")

st.markdown(
    """
This dashboard provides an overview of hospital performance,
patient demand, staffing, and operational efficiency.
"""
)

# -------------------------
# Connect to Database
# -------------------------

connection = sqlite3.connect("database/hospital.db")

# -------------------------
# Load Tables
# -------------------------

patients = pd.read_sql(
    "SELECT * FROM patients",
    connection
)

staff = pd.read_sql(
    "SELECT * FROM staff",
    connection
)

staff_schedule = pd.read_sql(
    "SELECT * FROM staff_schedule",
    connection
)

services = pd.read_sql(
    "SELECT * FROM services_weekly",
    connection
)

# -------------------------
# Hospital KPIs
# -------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Patients",
    len(patients)
)

col2.metric(
    "Average Stay",
    round(patients["length_of_stay"].mean(), 1)
)

col3.metric(
    "Average Satisfaction",
    round(patients["satisfaction"].mean(), 1)
)

col4.metric(
    "Total Staff",
    len(staff)
)

st.subheader("Patients by Service")

service_counts = (
    patients["service"]
    .value_counts()
)

st.bar_chart(service_counts)

st.subheader("Average Satisfaction by Service")

satisfaction = (
    patients.groupby("service")["satisfaction"]
    .mean()
)

st.bar_chart(satisfaction)

st.subheader("Average Length of Stay")

stay = (
    patients.groupby("service")["length_of_stay"]
    .mean()
)

st.bar_chart(stay)

st.subheader("Patient Refusals")

refused = (
    services.groupby("service")["patients_refused"]
    .sum()
)

st.bar_chart(refused)
