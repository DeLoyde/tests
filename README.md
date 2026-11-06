# TTC Bus Delays Dashboard (2014–2024)

An interactive Streamlit dashboard of TTC bus delay incidents: monthly trends, incident types,
day-by-hour patterns, top routes and locations, and a heatmap of where delays happen.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a new GitHub repository and push this whole folder to it (including `data/` and `.streamlit/`).
   ```bash
   git init && git add . && git commit -m "TTC bus delay dashboard"
   git branch -M main
   git remote add origin https://github.com/<your-username>/ttc-bus-delays.git
   git push -u origin main
   ```
2. Go to https://share.streamlit.io, sign in with GitHub, and click **Create app**.
3. Pick the repository, branch `main`, and main file `app.py`, then click **Deploy**.

## Data

`data/` holds slimmed, gzipped copies of the cleaned CSVs (only the columns the app uses), so each file
stays well under GitHub's 100 MB limit. To rebuild them from the original CSVs:

```bash
python prepare_data.py /path/to/folder/with/original/csvs
```

## Files

| File | Purpose |
|---|---|
| `app.py` | The dashboard |
| `prepare_data.py` | Rebuilds `data/` from the original CSVs |
| `data/delays.csv.gz` | All incidents (used for stats and charts) |
| `data/delays_geo.csv.gz` | Incidents with coordinates (used for the map) |
| `requirements.txt` | Python packages for Streamlit Cloud |
| `.streamlit/config.toml` | Theme |
