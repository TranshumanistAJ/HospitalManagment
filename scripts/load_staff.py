"""Load staff data into the hospital database."""

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

    # Read the CSV
    staff = pd.read_csv(DATA_DIR / "staff.csv")

    # Connect to SQLite
    connection = sqlite3.connect(DB_DIR / "hospital.db")

    # Save the table
    staff.to_sql(
        "staff",
        connection,
        if_exists="replace",
        index=False
    )

    # Close the database
    connection.close()

    print("Staff table loaded successfully!")

# -------------------------
# Run the program
# -------------------------

if __name__ == "__main__":
    main()
