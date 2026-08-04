import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
DB_DIR = ROOT / "database"
DB_PATH = DB_DIR / "hospital.db"

# -------------------------
# Helpers
# -------------------------

def build_database_from_csv():
    DB_DIR.mkdir(parents=True, exist_ok=True)

    patients = pd.read_csv(DATA_DIR / "patients.csv")
    patients["arrival_date"] = pd.to_datetime(patients["arrival_date"])
    patients["departure_date"] = pd.to_datetime(patients["departure_date"])
    patients["length_of_stay"] = (
        patients["departure_date"] - patients["arrival_date"]
    ).dt.days

    staff = pd.read_csv(DATA_DIR / "staff.csv")
    staff_schedule = pd.read_csv(DATA_DIR / "staff_schedule.csv")
    services = pd.read_csv(DATA_DIR / "services_weekly.csv")

    connection = sqlite3.connect(DB_PATH)
    patients.to_sql("patients", connection, if_exists="replace", index=False)
    staff.to_sql("staff", connection, if_exists="replace", index=False)
    staff_schedule.to_sql(
        "staff_schedule", connection, if_exists="replace", index=False
    )
    services.to_sql("services_weekly", connection, if_exists="replace", index=False)
    connection.close()


def load_database():
    if not DB_PATH.exists():
        build_database_from_csv()

    connection = sqlite3.connect(DB_PATH)
    try:
        patients = pd.read_sql("SELECT * FROM patients", connection)
        staff = pd.read_sql("SELECT * FROM staff", connection)
        staff_schedule = pd.read_sql("SELECT * FROM staff_schedule", connection)
        services = pd.read_sql("SELECT * FROM services_weekly", connection)
    except (sqlite3.DatabaseError, pd.io.sql.DatabaseError):
        connection.close()
        build_database_from_csv()
        connection = sqlite3.connect(DB_PATH)
        patients = pd.read_sql("SELECT * FROM patients", connection)
        staff = pd.read_sql("SELECT * FROM staff", connection)
        staff_schedule = pd.read_sql("SELECT * FROM staff_schedule", connection)
        services = pd.read_sql("SELECT * FROM services_weekly", connection)
    return connection, patients, staff, staff_schedule, services


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Hospital Management Dashboard",
    page_icon="🏥",
    layout="wide",
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
# Load data
# -------------------------

try:
    connection, patients, staff, staff_schedule, services = load_database()
except FileNotFoundError as exc:
    st.error(
        f"Unable to deploy because a required CSV file is missing: {exc}."
    )
    st.stop()

# -------------------------
# Hospital KPIs
# -------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", len(patients))
col2.metric("Average Stay", round(patients["length_of_stay"].mean(), 1))
col3.metric("Average Satisfaction", round(patients["satisfaction"].mean(), 1))
col4.metric("Total Staff", len(staff))

st.subheader("Patients by Service")
service_counts = patients["service"].value_counts()
st.bar_chart(service_counts)

st.subheader("Average Satisfaction by Service")
satisfaction = patients.groupby("service")["satisfaction"].mean()
st.bar_chart(satisfaction)

st.subheader("Average Length of Stay")
stay = patients.groupby("service")["length_of_stay"].mean()
st.bar_chart(stay)

st.subheader("Patient Refusals")
refused = services.groupby("service")["patients_refused"].sum()
st.bar_chart(refused)
