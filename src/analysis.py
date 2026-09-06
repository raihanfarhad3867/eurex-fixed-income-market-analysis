from __future__ import annotations
import pandas as pd

GERMAN = ["FGBS", "FGBM", "FGBL"]
TENOR_10Y = ["FGBL", "FBTP", "FOAT"]


def key_metrics(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    german = df[df.product_code.isin(GERMAN)].copy()
    total = german.monthly_volume.sum()
    trading_days = int(df.groupby('month')['trading_days'].first().sum())
    rows.append({"metric":"German curve Jan-Aug total volume","value":float(total),"unit":"contracts"})
    rows.append({"metric":"German curve Jan-Aug ADV","value":float(total/trading_days),"unit":"contracts/day"})

    for code in GERMAN:
        x = german[german.product_code.eq(code)]
        roll = x[x.roll_month].monthly_volume.mean()
        non = x[~x.roll_month].monthly_volume.mean()
        rows.append({"metric":f"{code} roll-month uplift vs non-roll average","value":float((roll/non-1)*100),"unit":"%"})
        rows.append({"metric":f"{code} share of German Jan-Aug volume","value":float(x.monthly_volume.sum()/total*100),"unit":"%"})

    sovereign = df[df.product_code.isin(TENOR_10Y)].groupby('product_code').monthly_volume.sum()
    for code in TENOR_10Y:
        rows.append({"metric":f"{code} share of selected 10Y sovereign volume","value":float(sovereign[code]/sovereign.sum()*100),"unit":"%"})
    return pd.DataFrame(rows)
