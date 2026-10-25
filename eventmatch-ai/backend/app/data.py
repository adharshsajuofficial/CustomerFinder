from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "demo_users.csv"
REQUIRED = {"user_id","display_name","city","interests","skills","preferred_event_types"}

def load_profiles(path=DATA_PATH):
    if not path.exists(): raise FileNotFoundError(f"Dataset not found: {path}")
    df = pd.read_csv(path, keep_default_na=False)
    missing = REQUIRED - set(df.columns)
    if missing: raise ValueError("Missing required columns: " + ", ".join(sorted(missing)))
    return df.to_dict(orient="records")
