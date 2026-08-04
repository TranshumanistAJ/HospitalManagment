"""Load staff schedule data into the hospital database."""

from pathlib import Path
import pandas as pd
import sqlite3

# -------------------------
# Find the project folders
# -------------------------
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_DIR = ROOT / "database"

# -------------------------
# Main recipe
# -------------------------

def main():

    # Read the CSV file
    schedule = pd.read_csv(DATA_DIR / "staff_schedule.csv")

    # Open the database
    connection = sqlite3.connect(DB_DIR / "hospital.db")

    # Save the dataframe as a SQL table
    schedule.to_sql(
        "staff_schedule",
        connection,
        if_exists="replace",
        index=False,
    )

    # Close the database
    connection.close()

    print("Staff schedule loaded successfully!")

# -------------------------
# Start here
# -------------------------

if __name__ == "__main__":
    main()
