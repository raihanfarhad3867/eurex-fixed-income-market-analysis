from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
required = ['README.md','reports/management_memo.md','docs/methodology.md','data/processed/monthly_volume_2026_jan_aug.csv','data/processed/key_metrics.csv']
missing = [p for p in required if not (ROOT/p).exists()]
if missing:
    raise SystemExit(f'Missing: {missing}')

x = pd.read_csv(ROOT/'data/processed/monthly_volume_2026_jan_aug.csv')
assert x.product_code.nunique() == 7
assert set(x.month.unique()) == {'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug'}
assert len(x) == 56
assert x.monthly_volume.gt(0).all()
print('PASS: project structure and dataset validated')
