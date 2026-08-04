# Hospital Management Dashboard

## Overview

This project is a personal Hospital Management Dashboard built with Streamlit and SQLite. It provides a lightweight analytics interface for monitoring patient demand, satisfaction, length of stay, and hospital capacity across services.

The dashboard is designed for local use with CSV sample data and a local SQLite database. It is a solo project for your hospital data management and performance monitoring.

## What it does

- Loads hospital data from the local SQLite database at `database/hospital.db`
- Displays key performance indicators (KPIs) for patient volume, average stay, satisfaction, and staffing
- Visualizes patient counts by service, average satisfaction by service, length of stay by service, and patient refusals by service
- Loads data tables from CSV source files using the included Python loader scripts

## Data sources

The project uses the following CSV files in `data/`:

- `patients.csv` — patient admission records with arrival/discharge dates, service category, and satisfaction scores
- `staff.csv` — staff members, roles, and service assignments
- `staff_schedule.csv` — weekly staff attendance records, including presence and service assignment
- `services_weekly.csv` — weekly service-level metrics such as available beds, requests, admissions, refusals, satisfaction, and staff morale

These files are imported into the local SQLite database using the loader scripts in `scripts/`.

## How the project is structured

- `app.py` — Streamlit dashboard for visualizing hospital metrics
- `database/hospital.db` — local SQLite database used by the dashboard
- `data/` — source CSV files containing sample hospital data
- `scripts/` — data loader scripts to populate the database from CSV files
- `run_streamlit.bat` — shortcut to launch the dashboard on Windows
- `.vscode/tasks.json` — VS Code task configuration for starting the Streamlit app
- `notebooks/capacity.ipynb` — exploratory notebook for capacity analysis

## Requirements

- Python 3.10+ (or a supported Python version)
- `streamlit`
- `pandas`

## Installation

1. Install Python if it is not already installed.
2. Open a terminal in the project root.
3. Install the required Python packages:

```bash
python -m pip install --upgrade pip
python -m pip install streamlit pandas
```

## Load the data into the database

Before running the dashboard, populate the SQLite database with the CSV data.

Run each loader script from the project root:

```bash
python scripts/load_staff.py
python scripts/load_schedule.py
python scripts/load_services.py
python scripts/load_patients.py
```

The loader scripts will write the data into `database/hospital.db`.

## Run the dashboard

Start the Streamlit app with either command:

```bash
python -m streamlit run app.py
```

or on Windows:

```bash
run_streamlit.bat
```

Then open the local URL shown in the terminal, usually `http://localhost:8501`.

## Notes

- The dashboard expects the local database file to exist at `database/hospital.db`.
- If you update any CSV file, rerun the corresponding loader script to refresh the database.
- The app is configured to use `database/hospital.db` and the tables `patients`, `staff`, `staff_schedule`, and `services_weekly`.

## Recommended workflow

1. Confirm the `data/` files contain the latest hospital data.
2. Run the loader scripts to refresh the local database.
3. Launch `app.py` with Streamlit.
4. Review the KPI summary and charts for patient demand, outcomes, and resource status.

## Future enhancements

Potential next steps for the project:

- Add interactive filters by service, date range, and department
- Add staff schedule visualizations and absence analysis
- Display capacity forecasts and admission risk indicators
- Add patient-level drill-down views and export options
- Deploy to a hosted Streamlit service or package as a web app

## GitHub deployment guidance

To deploy this project to GitHub:

1. Initialize a repository in the project root:

```bash
git init
```

2. Add your files:

```bash
git add .
```

3. Commit changes:

```bash
git commit -m "Initial hospital management dashboard"
```

4. Create a GitHub repository and add it as a remote.
5. Push the repository:

```bash
git push -u origin main
```

Once the repository is on GitHub, you can continue adding documentation, issues, or future improvements there.
