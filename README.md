# Hospital Management Dashboard

## 🌟 Overview

A polished hospital analytics dashboard built with Streamlit and SQLite. This project combines hospital operations data, patient outcomes, staffing, and capacity tracking into a single local dashboard experience.

The repository is designed for portfolio presentation and local use with sample CSV data and a local SQLite database.

## 📊 Key Capabilities

- Reads hospital data from `database/hospital.db`
- Shows high-level KPIs for admissions, average length of stay, satisfaction, and staffing capacity
- Delivers visual analysis of patient distribution by service, satisfaction trends, length of stay, and service refusals
- Imports CSV data with dedicated loader scripts for staff, schedules, services, and patients

## 🧠 Data Sources

The following CSV files in `data/` provide the data model:

- `patients.csv` — patient admission records with arrival/discharge dates, service category, and satisfaction scores
- `staff.csv` — staff details, roles, and service assignments
- `staff_schedule.csv` — weekly staff attendance and service coverage data
- `services_weekly.csv` — weekly service metrics including capacity, requests, admissions, refusals, morale, and satisfaction

## 🏗️ Project Structure

- `app.py` — Streamlit dashboard entrypoint
- `database/hospital.db` — local SQLite database
- `data/` — source CSV datasets
- `scripts/` — database loader scripts
- `run_streamlit.bat` — Windows launcher for the app
- `.vscode/tasks.json` — VS Code task configuration for project workflows
- `notebooks/capacity.ipynb` — exploratory analysis notebook

## ⚙️ Requirements

- Python 3.10 or newer
- `streamlit`
- `pandas`

## 📦 Installation

Install the required Python packages:

```bash
python -m pip install --upgrade pip
python -m pip install streamlit pandas
```

## 🔄 Data Loading

Populate the SQLite database from the CSV files using the loader scripts:

```bash
python scripts/load_staff.py
python scripts/load_schedule.py
python scripts/load_services.py
python scripts/load_patients.py
```

The loader scripts write data into `database/hospital.db`.

## ▶️ Run the Dashboard

Launch the Streamlit app:

```bash
python -m streamlit run app.py
```

On Windows, the included shortcut can also launch the dashboard:

```bash
run_streamlit.bat
```

## 📌 Deployment Notes

This repository is hosted publicly at:

https://github.com/TranshumanistAJ/HospitalManagment

A standard GitHub workflow for this project is:

1. Initialize the repository:

```bash
git init
```

2. Stage files:

```bash
git add .
```

3. Commit changes:

```bash
git commit -m "Initial hospital management dashboard"
```

4. Add the GitHub remote and push:

```bash
git push -u origin main
```

Streamlit deployment can be enabled by linking this public repository to Streamlit Cloud and selecting the `main` branch.

## 📝 Notes

- The dashboard expects `database/hospital.db` to exist locally.
- Re-run the appropriate loader script after any CSV data update.
- The app uses the tables `patients`, `staff`, `staff_schedule`, and `services_weekly`.

## 🚀 Future Enhancements

- Add interactive filters for service, date range, and department
- Add visualizations for staff scheduling and absence patterns
- Add capacity forecasting and risk indicators
- Add patient-level drill-down views and export capability
- Build a hosted Streamlit deployment for broader access
