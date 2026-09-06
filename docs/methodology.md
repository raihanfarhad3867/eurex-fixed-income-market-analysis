# Methodology

## Question
Where is trading activity concentrated across Eurex European government-bond futures, how does activity change around quarterly roll months, and what can this tell a fixed-income product team about growth opportunities?

## Data construction
1. Jan–Jul 2026 monthly traded-contract figures were transcribed from official Eurex Monthly Statistics reports.
2. The official Eurex Daily Statistics CSV for 4 Sep 2026 was parsed programmatically. The repository stores a compact selected extract containing report metadata plus only the futures used in this analysis.
3. August 2026 monthly volume was reconstructed using: `August = YTD at 4 Sep - Jan..Jul official monthly volume - Sep MTD at 4 Sep`.

The clean Jan–Aug dataset stored in `data/processed/` preserves the monthly volume, trading-day count, ADV, roll-month flag and month-on-month change used in the analysis.

## Products
German curve: FGBS (Schatz), FGBM (Bobl), FGBL (Bund), plus FGBX (Buxl).
Adjacent sovereign benchmarks: FBTP (10Y Italy), FOAT (10Y France), FBTS (short Italy).
New-product case: FBEU (Euro-EU Bond Futures).

## Measures
- Monthly traded contracts
- Average daily volume (ADV)
- Month-on-month activity change
- Share of German-curve volume
- Roll-month uplift: average March/June volume versus non-roll months in Jan–Aug
- 4 Sep daily volume and previous-day open interest snapshot

## Interpretation limits
Volume and open interest are activity indicators, not a complete liquidity measure. A full study would require bid/ask spreads, order-book depth, trade size, intraday data, client segmentation and execution-cost data. March/June activity spikes cannot be attributed to roll alone; macro volatility and hedging demand also matter.
