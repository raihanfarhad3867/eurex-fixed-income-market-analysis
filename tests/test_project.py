from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.eurex_parser import parse_daily_statistics_csv
from src.analysis import key_metrics


def test_sep04_parser():
    x = parse_daily_statistics_csv(ROOT/'data/raw/dailystat_20260904_selected.csv')
    bund = x[x.product_code.eq('FGBL')].iloc[0]
    assert int(bund.daily_volume) == 2026366
    assert int(bund.open_interest_prev_day) == 2106126


def test_fbeu_snapshot():
    x = parse_daily_statistics_csv(ROOT/'data/raw/dailystat_20260904_selected.csv')
    eu = x[x.product_code.eq('FBEU')].iloc[0]
    assert int(eu.year_to_date_volume) == 13291
    assert int(eu.open_interest_prev_day) == 107


def test_master_dataset_and_metrics():
    x = pd.read_csv(ROOT/'data/processed/monthly_volume_2026_jan_aug.csv')
    assert len(x) == 56
    metrics = key_metrics(x)
    total = metrics.loc[metrics.metric.eq('German curve Jan-Aug total volume'),'value'].iloc[0]
    assert int(total) == 553736896
