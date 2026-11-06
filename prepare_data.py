"""Shrink the raw TTC CSVs into small gzipped files the Streamlit app loads.

Run once from this folder:  python prepare_data.py path/to/raw_csv_folder
The raw files are ~107 MB each (over GitHub's 100 MB limit); the outputs are a few MB.
"""
import sys
from pathlib import Path
import pandas as pd

RAW = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

def slim(path, extra=()):
    cols = ["Datetime", "Route", "Station", "Incident", "Min Delay", *extra]
    d = pd.read_csv(path, usecols=cols, dtype={"Route": str}, low_memory=False)
    d["Datetime"] = pd.to_datetime(d["Datetime"], errors="coerce")
    d = d.dropna(subset=["Datetime", "Incident"])
    d["Route"] = d["Route"].str.replace(r"\.0$", "", regex=True)
    d["Station"] = d["Station"].str.strip().str.title()
    d["Datetime"] = d["Datetime"].dt.strftime("%Y-%m-%d %H:%M")
    for c in extra:
        d[c] = d[c].round(5)
    return d

slim(RAW / "pre_2025_ttc_bus_delays_cleaned.csv").to_csv(OUT / "delays.csv.gz", index=False)
m = slim(RAW / "pre_2025_ttc_bus_delays_with_coords.csv", extra=("Latitude", "Longitude"))
m.dropna(subset=["Latitude", "Longitude"]).to_csv(OUT / "delays_geo.csv.gz", index=False)
for f in OUT.glob("*.csv.gz"):
    print(f.name, f"{f.stat().st_size / 1e6:.1f} MB")
