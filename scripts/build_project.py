from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.analysis import key_metrics
from src.eurex_parser import parse_daily_statistics_csv

monthly = pd.read_csv(ROOT / 'data/processed/monthly_volume_2026_jan_aug.csv')
sep = parse_daily_statistics_csv(ROOT / 'data/raw/dailystat_20260904_selected.csv')

metrics = key_metrics(monthly)
metrics.to_csv(ROOT / 'data/processed/key_metrics.csv', index=False)
sep.to_csv(ROOT / 'data/processed/sep04_snapshot.csv', index=False)

print('Built project outputs successfully')
