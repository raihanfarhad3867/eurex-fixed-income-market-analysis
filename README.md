# Eurex Fixed-Income Futures Activity & Product Opportunity Monitor

Independent portfolio project by Raihan Farhad Sakil.

## Project question
How can public Eurex trading statistics be used to understand where activity is concentrated across European government-bond futures, how quarterly futures rolls affect the numbers, and where a product-growth opportunity or adoption challenge may exist?

## What I analysed
- Euro-Schatz Futures (FGBS) — short German government-bond exposure
- Euro-Bobl Futures (FGBM) — medium German exposure
- Euro-Bund Futures (FGBL) — long German benchmark exposure
- Euro-Buxl (FGBX), Euro-BTP (FBTP), Euro-OAT (FOAT) and Short-Term BTP (FBTS) as adjacent benchmarks
- Euro-EU Bond Futures (FBEU) as a newer-product adoption/liquidity-formation case

## Evidence policy
- Jan–Jul 2026 monthly volumes come from official Eurex Monthly Statistics.
- August is derived deterministically from the official 4 Sep 2026 daily report: **Sep-4 YTD − Jan–Jul totals − Sep month-to-date**.
- The repository keeps a compact selected extract of the official 4 Sep daily statistics for the products used here.
- Volume and open interest are activity indicators, not a complete measure of liquidity.

## Main findings
| Finding | Result |
|---|---:|
| FGBS + FGBM + FGBL Jan–Aug volume | ~553.7m contracts |
| Combined German-curve ADV | ~3.28m contracts/day |
| FGBL share of German three-product volume | 39.3% |
| FGBM share | 31.3% |
| FGBS share | 29.4% |
| FGBL share of selected FGBL/FBTP/FOAT comparison | ~65.0% |

March and June were much more active than the non-roll months in this sample. The uplift was about 118% for FGBS, 61% for FGBM and 59% for FGBL. This should **not** be attributed to the roll alone because market volatility and hedging demand also matter.

The more interesting product-management case is FBEU. The 4 Sep 2026 daily statistics show 13,291 contracts YTD and 107 contracts of previous-day open interest. The question therefore becomes less "can we design another contract?" and more **"what would make a newer contract develop sustainable two-sided liquidity?"**

## Technical workflow
```text
Official Eurex monthly statistics
          +
Selected official Sep-4 daily-statistics extract
          ↓
Python parsing + validation
          ↓
Jan-Aug clean dataset
          ↓
ADV / MoM / roll-month / market-share metrics
          ↓
Management memo + product recommendation
```

## Run locally
```bash
pip install -r requirements.txt
python scripts/build_project.py
pytest -q
```

## Why this project matters
The project follows a practical exchange/product-analysis workflow: collect market data, validate it, understand futures-specific effects, compare products, identify a product-growth question, and turn the analysis into a management recommendation.

## Important limitation
This is a public-data portfolio project, not an internal Eurex liquidity study. A production study should add bid/ask spreads, order-book depth, trade-size distribution, client/account segmentation, market-maker quote quality, TES/block activity, execution costs and Bloomberg/internal data where permitted.

See `reports/management_memo.md`, `docs/methodology.md`, `docs/concepts.md` and `docs/sources.md`.