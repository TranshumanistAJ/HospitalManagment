from pathlib import Path
import pandas as pd
import sqlite3

# -------------------------
# Project folders
# -------------------------
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_DIR = ROOT / "database"

# -------------------------
# Main program
# -------------------------

def main():
    patients = pd.read_csv(DATA_DIR / "patients.csv")

    # --------------------
    # Transform the data
    # --------------------
    patients["arrival_date"] = pd.to_datetime(patients["arrival_date"])
    patients["departure_date"] = pd.to_datetime(patients["departure_date"])

    patients["length_of_stay"] = (
        patients["departure_date"] -
        patients["arrival_date"]
    ).dt.days

    # --------------------
    # Load into SQLite
    # --------------------
    connection = sqlite3.connect(DB_DIR / "hospital.db")

    patients.to_sql(
        "patients",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print("Patients loaded successfully!")


# -------------------------
# Run the program
# -------------------------

if __name__ == "__main__":
    main()
