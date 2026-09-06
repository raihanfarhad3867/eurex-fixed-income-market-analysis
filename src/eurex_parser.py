from __future__ import annotations
from pathlib import Path
import pandas as pd

PRODUCT_CODES = ["FGBS", "FGBM", "FGBL", "FGBX", "FBTP", "FOAT", "FBTS", "FBEU"]
NUMERIC_COLS = {5:"daily_volume",7:"month_to_date_volume",9:"year_to_date_volume",11:"avg_daily_volume_month",12:"avg_daily_volume_year",14:"open_interest_prev_day"}


def _to_num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s.astype(str).str.replace(",", "", regex=False).replace("nan", pd.NA), errors="coerce")


def parse_daily_statistics_csv(path: str | Path, codes=PRODUCT_CODES) -> pd.DataFrame:
    """Parse the compact selected extract from the official Eurex Daily Statistics CSV."""
    raw = pd.read_csv(path, header=None)
    rows = raw[raw[4].astype(str).isin(codes)].copy()
    out = pd.DataFrame({"product_name":rows[3].astype(str).values,"product_code":rows[4].astype(str).values})
    for idx, name in NUMERIC_COLS.items():
        out[name] = _to_num(rows[idx]).values
    date = None
    for value in raw.iloc[:12,0].dropna().astype(str):
        try:
            date = pd.to_datetime(value, format="%m/%d/%Y", errors="raise").date().isoformat()
            break
        except Exception:
            continue
    out.insert(0,"date",date)
    return out.reset_index(drop=True)
