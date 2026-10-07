# Benchmarks for the active-trader, affluent/wealth and institutional segments: IBKR, Schwab (incl. Advisor Services), Swissquote, Saxo, Julius Baer, UBS GWM, EFG. Data as of 7 Oct 2026

Conventions used in all sections:
- **REPORTED** means the company figure as quoted in the source.
- **COMPUTED** means my arithmetic from reported inputs. The formula is shown.
- bps = basis points. All "per assets" ratios are annualized.
- "Avg" means a simple 2-point average of opening and closing balances unless stated otherwise. The companies' own averages (daily or monthly) were not retrievable.
- **Read the method note in Section 1 › Gaps first.** All figures come from search-engine extracts of primary releases. WebFetch and direct downloads were blocked by the egress proxy, and the session's web-search budget ran out before custody, ECM/DCM and UBS/EFG detail could be searched.

---

## 1. Interactive Brokers: accounts and growth, client equity, DARTs, DARTs per account, commission per order, margin loans and credits ÷ client equity, revenue mix, net revenue ÷ client equity, pretax margin, client-type split

### Takeaway
IBKR is the high-growth, high-margin benchmark for active traders and institutions. At the latest data it had 5.58m accounts (+35% y/y, Sep-26) and $965bn client equity. It earns about 85–92 bps of average client equity: about 55–58% net interest income, about 35% commissions and about 5% other fees. Pretax margin is about 77%. Margin loans run at about 11–12% of client equity and client credits at about 19–21%, and average commission is about $2.6 per cleared order. About 54% of client equity belongs to institutional client types (hedge funds, advisors, prop traders, introducing brokers), down from 64% in 2020.

### Cited Findings

**1.1 Accounts, balances and activity (REPORTED)**

| Metric | Value | Unit | Period | Definition / basis (company wording where retrieved) | Source |
|---|---|---|---|---|---|
| Client accounts | 5.576 | m | end-Sep 2026 | +35% y/y, +2% m/m | [FX News Group (IBKR Sep-26 metrics)](https://fxnewsgroup.com/forex-news/retail-forex/interactive-brokers-registers-6-y-y-increase-in-darts-in-sep-2026/); [StockTitan](https://www.stocktitan.net/news/IBKR/interactive-brokers-group-reports-brokerage-metrics-and-other-d0ipkhun44w5.html) |
| Client accounts | 5.185 | m | end-Jun 2026 | +34% y/y, +4% m/m (Q2 release: "+34% to 5.19 million") | [Barchart (IBKR Jun-26 metrics)](https://www.barchart.com/story/news/3081220/interactive-brokers-group-reports-brokerage-metrics-and-other-financial-information-for-june-2026-includes-reg-nms-execution-statistics); [Nasdaq 2Q26 release](https://www.nasdaq.com/press-release/interactive-brokers-group-announces-2q2026-results-2026-07-21) |
| Client accounts | 4.75 | m | end-Mar 2026 | +31% y/y | [Business Wire 1Q26 release](https://www.businesswire.com/news/home/20260421110584/en/Interactive-Brokers-Group-Announces-1Q2026-Results) |
| Client accounts | 4.399 | m | end-Dec 2025 | +32% y/y, +2% m/m | [Business Wire Dec-25 metrics](https://www.businesswire.com/news/home/20260102619678/en/Interactive-Brokers-Group-Reports-Brokerage-Metrics-and-Other-Financial-Information-for-December-2025-includes-Reg.-NMS-Execution-Statistics); [Investing.com](https://www.investing.com/news/company-news/interactive-brokers-reports-37-rise-in-client-equity-for-december-93CH-4428025) |
| Net new accounts | >1 | m | FY2025 | "more than 1 million net new accounts" | [4Q25 call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/01/20/interactive-brokers-ibkr-earnings-transcript/) |
| Client equity | 964.7 | USD bn | end-Sep 2026 | +27% y/y, ≈flat m/m | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/interactive-brokers-registers-6-y-y-increase-in-darts-in-sep-2026/); [StockTitan](https://www.stocktitan.net/news/IBKR/interactive-brokers-group-reports-brokerage-metrics-and-other-d0ipkhun44w5.html) |
| Client equity | 906.7 | USD bn | end-Jul 2026 | — | [BrokerChooser](https://brokerchooser.com/news/interactive-brokers-posts-strong-july-growth-client-equity-tops-9067-billion--81e5d7da) |
| Client equity | 930.3 | USD bn | end-Jun 2026 | +40% y/y, −1% m/m | [Barchart](https://www.barchart.com/story/news/3081220/interactive-brokers-group-reports-brokerage-metrics-and-other-financial-information-for-june-2026-includes-reg-nms-execution-statistics) |
| Client equity | 789.4 | USD bn | end-Mar 2026 | +38% y/y | [Business Wire 1Q26](https://www.businesswire.com/news/home/20260421110584/en/Interactive-Brokers-Group-Announces-1Q2026-Results) |
| Client equity | 779.9 | USD bn | end-Dec 2025 | +37% y/y, +1% m/m | [Business Wire Dec-25](https://www.businesswire.com/news/home/20260102619678/en/Interactive-Brokers-Group-Reports-Brokerage-Metrics-and-Other-Financial-Information-for-December-2025-includes-Reg.-NMS-Execution-Statistics) |
| Client margin loans | 105.2 | USD bn | end-Sep 2026 | +36% y/y, +4% m/m | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/interactive-brokers-registers-6-y-y-increase-in-darts-in-sep-2026/) |
| Client margin loans | 108.5 | USD bn | end-Jun 2026 | +67% y/y, +8% m/m | [Barchart](https://www.barchart.com/story/news/3081220/interactive-brokers-group-reports-brokerage-metrics-and-other-financial-information-for-june-2026-includes-reg-nms-execution-statistics); [Morningstar/BW 2Q26](https://www.morningstar.com/news/business-wire/20260721157186/interactive-brokers-group-announces-2q2026-results) |
| Client margin loans | 86.0 | USD bn | end-Mar 2026 | +35% y/y | [StockTitan 1Q26](https://www.stocktitan.net/news/IBKR/interactive-brokers-group-announces-1q2026-pj6jgla1ic37.html) |
| Client margin loans | 90.2 | USD bn | end-Dec 2025 | +40% y/y, +8% m/m | [Business Wire Dec-25](https://www.businesswire.com/news/home/20260102619678/en/Interactive-Brokers-Group-Reports-Brokerage-Metrics-and-Other-Financial-Information-for-December-2025-includes-Reg.-NMS-Execution-Statistics) |
| Client credit balances | 186.2 | USD bn | end-Sep 2026 | "including $6.4 billion in insured bank deposit sweeps"; +20% y/y | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/interactive-brokers-registers-6-y-y-increase-in-darts-in-sep-2026/) |
| Client credit balances | 182.4 | USD bn | end-Jun 2026 | incl. $6.4bn insured bank deposit sweeps; +27% y/y | [Barchart](https://www.barchart.com/story/news/3081220/interactive-brokers-group-reports-brokerage-metrics-and-other-financial-information-for-june-2026-includes-reg-nms-execution-statistics) |
| Client credit balances | 168.8 | USD bn | end-Mar 2026 | +35% y/y | [StockTitan 1Q26](https://www.stocktitan.net/news/IBKR/interactive-brokers-group-announces-1q2026-pj6jgla1ic37.html) |
| Client credit balances | 160.1 | USD bn | end-Dec 2025 | incl. $6.4bn insured bank deposit sweeps; +34% y/y | [Business Wire Dec-25](https://www.businesswire.com/news/home/20260102619678/en/Interactive-Brokers-Group-Reports-Brokerage-Metrics-and-Other-Financial-Information-for-December-2025-includes-Reg.-NMS-Execution-Statistics) |
| DARTs (total) | 4.111 | m/day | Sep 2026 | Daily Average Revenue Trades; +6% y/y, −4% m/m | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/interactive-brokers-registers-6-y-y-increase-in-darts-in-sep-2026/) |
| DARTs (total) | 5.269 | m/day | Jun 2026 | +53% y/y, +6% m/m | [Investing.com](https://www.investing.com/news/company-news/interactive-brokers-reports-june-metrics-with-53-trade-growth-93CH-4771040) |
| DARTs (total) | 4.82 | m/day | Q2 2026 | +36% y/y | [Nasdaq 2Q26](https://www.nasdaq.com/press-release/interactive-brokers-group-announces-2q2026-results-2026-07-21) |
| DARTs (total) | 4.37 | m/day | Q1 2026 | +24% y/y | [StockTitan 1Q26](https://www.stocktitan.net/news/IBKR/interactive-brokers-group-announces-1q2026-pj6jgla1ic37.html) |
| DARTs (total) | 3.384 | m/day | Dec 2025 | +4% y/y, −21% m/m | [Business Wire Dec-25](https://www.businesswire.com/news/home/20260102619678/en/Interactive-Brokers-Group-Reports-Brokerage-Metrics-and-Other-Financial-Information-for-December-2025-includes-Reg.-NMS-Execution-Statistics) |
| DARTs per account | 159 | cleared DARTs/account/yr | Sep 2026 | "annualized average cleared DARTs per client account" (cleared basis only) | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/interactive-brokers-registers-6-y-y-increase-in-darts-in-sep-2026/) |
| DARTs per account | 166 | cleared DARTs/account/yr | Dec 2025 | same definition | [Business Wire Dec-25](https://www.businesswire.com/news/home/20260102619678/en/Interactive-Brokers-Group-Reports-Brokerage-Metrics-and-Other-Financial-Information-for-December-2025-includes-Reg.-NMS-Execution-Statistics) |
| Avg commission per cleared Commissionable Order | 2.57 | USD/order | Sep 2026 | "including exchange, clearing and regulatory fees" | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/interactive-brokers-registers-6-y-y-increase-in-darts-in-sep-2026/) |
| Avg commission per cleared Commissionable Order | 2.64 | USD/order | Q2 2026 | same definition | [Morningstar/BW 2Q26](https://www.morningstar.com/news/business-wire/20260721157186/interactive-brokers-group-announces-2q2026-results) |

**1.2 P&L (REPORTED)**

| Metric | Value | Unit | Period | Definition / basis | Source |
|---|---|---|---|---|---|
| Net revenues | 1,900 (adjusted 1,880) | USD m | Q2 2026 | Q2-25: 1,480 reported and adjusted | [Yahoo/BW 2Q26](https://finance.yahoo.com/markets/stocks/articles/interactive-brokers-group-announces-2q2026-200100596.html); [Nasdaq](https://www.nasdaq.com/press-release/interactive-brokers-group-announces-2q2026-results-2026-07-21) |
| Commissions | 673 | USD m | Q2 2026 | +30% y/y; client volumes: options +17%, stocks +14%, futures +2% | [Nasdaq 2Q26](https://www.nasdaq.com/press-release/interactive-brokers-group-announces-2q2026-results-2026-07-21) |
| Net interest income | 1,060 | USD m | Q2 2026 | +23%, "primarily on higher average customer margin loans and customer credit balances" | [Nasdaq 2Q26](https://www.nasdaq.com/press-release/interactive-brokers-group-announces-2q2026-results-2026-07-21) |
| Other fees and services | 87 | USD m | Q2 2026 | +40%. Increases: +$9m payments for order flow from exchange-mandated programs, +$8m risk exposure fees, +$3m market data fees | [Morningstar/BW 2Q26](https://www.morningstar.com/news/business-wire/20260721157186/interactive-brokers-group-announces-2q2026-results) |
| Execution, clearing & distribution fees (expense) | 142 | USD m | Q2 2026 | +22%. Driven by +$19m regulatory fees after the SEC Section 31 fee rate rise on 4 Apr 2026, partly offset by more exchange liquidity rebates | [Morningstar/BW 2Q26](https://www.morningstar.com/news/business-wire/20260721157186/interactive-brokers-group-announces-2q2026-results) |
| Compensation & benefits | 182 | USD m | Q2 2026 | = 10% of adjusted net revenues (11% a year earlier) | [BigGo (2Q26 call)](https://finance.biggo.com/news/US_IBKR_2026-07-21) |
| Income before taxes | 1,460 (adjusted 1,440) | USD m | Q2 2026 | Q2-25: 1,100 | [Yahoo/BW 2Q26](https://finance.yahoo.com/markets/stocks/articles/interactive-brokers-group-announces-2q2026-200100596.html) |
| Pretax margin | 77 | % | Q2 2026 | 7th consecutive quarter above 70% | [BigGo](https://finance.biggo.com/news/US_IBKR_2026-07-21) |
| Net revenues | 1,669 | USD m | Q1 2026 | Q1-25: 1,427 | [StockTitan 1Q26](https://www.stocktitan.net/news/IBKR/interactive-brokers-group-announces-1q2026-pj6jgla1ic37.html) |
| Commissions | 613 | USD m | Q1 2026 | +19%; volumes: stocks +25%, futures +20%, options +16% | [Business Wire 1Q26](https://www.businesswire.com/news/home/20260421110584/en/Interactive-Brokers-Group-Announces-1Q2026-Results) |
| Net interest income | 904 | USD m | Q1 2026 | +17% | [Business Wire 1Q26](https://www.businesswire.com/news/home/20260421110584/en/Interactive-Brokers-Group-Announces-1Q2026-Results) |
| Net revenues | 1,640 (adjusted 1,670) | USD m | Q4 2025 | — | [Nasdaq 4Q25](https://www.nasdaq.com/press-release/interactive-brokers-group-announces-4q2025-results-2026-01-20) |
| Commissions / NII | 582 / 966 | USD m | Q4 2025 | +22% / +20%. NII rose "on higher average customer margin loans and customer credit balances and stronger securities lending activity" | [Nasdaq 4Q25](https://www.nasdaq.com/press-release/interactive-brokers-group-announces-4q2025-results-2026-01-20) |
| Income before taxes | 1,300 (adjusted 1,330) | USD m | Q4 2025 | — | [Nasdaq 4Q25](https://www.nasdaq.com/press-release/interactive-brokers-group-announces-4q2025-results-2026-01-20) |
| Net revenues | 6,205 | USD m | FY2025 | FY2024: 5,185 | [IBKR 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1381197/000138119726000062/ibkr-20251231.htm) |
| Commissions | 2,149 | USD m | FY2025 | — | [TradingView (4Q25 release)](https://www.tradingview.com/news/tradingview:5bef34f7fb723:0-interactive-brokers-group-announces-4q2025-results/) |
| Net interest income | ≈3,600 | USD m | FY2025 | rounded ("$3.6 billion"); exact figure not retrieved | [TradingView (4Q25 release)](https://www.tradingview.com/news/tradingview:5bef34f7fb723:0-interactive-brokers-group-announces-4q2025-results/) |
| Other fees and services | 291 | USD m | FY2025 | +4%: higher insured bank deposit sweep ("FDIC sweep") fees, market data fees and PFOF from exchange-mandated programs, partly offset by lower risk exposure fees | [IBKR 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1381197/000138119726000062/ibkr-20251231.htm) |
| Income before income taxes | 4,771 | USD m | FY2025 | FY2024: 3,695 | [IBKR 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1381197/000138119726000062/ibkr-20251231.htm) |

**1.3 Client-type split (REPORTED; partly secondary sources)**

| Metric | Value | Period | Definition / basis | Source |
|---|---|---|---|---|
| Institutional share of customers' equity | ≈54% | FY2025 | "institutional accounts such as hedge funds, financial advisors, proprietary trading firms and introducing brokers" | [IBKR Annual Report FY2025 (ARS)](https://www.sec.gov/Archives/edgar/data/1381197/000114036126009035/ny20056593x4_ars.pdf); [10-Q 1Q25](https://www.sec.gov/Archives/edgar/data/1381197/000138119725000052/ibkr-20250331x10q.htm) |
| Same metric, history | 55% FY24; 57% FY23; 59% FY22; 62% FY21; 64% FY20 | FY2020–24 | same wording | [10-K FY24](https://www.sec.gov/Archives/edgar/data/1381197/000138119725000036/ibkr-20241231x10k.htm), [FY23](https://www.sec.gov/Archives/edgar/data/1381197/000138119724000083/ibkr-20231231x10k.htm), [FY22](https://www.sec.gov/Archives/edgar/data/1381197/000138119723000014/ibkr-20221231x10k.htm), [FY21](https://www.sec.gov/Archives/edgar/data/1381197/000138119722000010/ibkr-20211231x10k.htm), [FY20](https://www.sec.gov/Archives/edgar/data/1381197/000138119721000008/ibkr-20201231x10k.htm) |
| % of accounts by type | Individuals 61, Financial advisors 10, Prop trading groups 2, Hedge & mutual funds 1, Introducing brokers 26 | 31 Mar 2021 | latest full company split retrieved | [IBKR 1Q21 investor presentation](https://investors.interactivebrokers.com/download/investors/1Q21_IBKR_Presentation.pdf) |
| % of client equity by type | Individuals 36, FAs 16, Prop 9, HF/MF 7, IBs 32 | 1Q 2021 | — | [IBKR 1Q21 presentation](https://investors.interactivebrokers.com/download/investors/1Q21_IBKR_Presentation.pdf) |
| % of commissions by type | Individuals 54, FAs 11, Prop 13, HF/MF 6, IBs 16 | 1Q 2021 | — | [IBKR 1Q21 presentation](https://investors.interactivebrokers.com/download/investors/1Q21_IBKR_Presentation.pdf) |
| Hedge funds | 1% of accounts, 6% of client equity, 7% of commissions | ~H1 2024 (secondary) | analyst reading of IBKR presentations | [Bristlemoon Research](https://www.bristlemoonresearch.com/p/interactive-brokers-ibkr-hoovering) |
| Prop trading groups | 2% of accounts, 18% of commissions | H1 2024 (secondary) | same | [Bristlemoon Research](https://www.bristlemoonresearch.com/p/interactive-brokers-ibkr-hoovering) |
| Individuals | 68% of customers, 43% of client equity; introducing brokers 2nd-largest by accounts and equity | ~2023–24 (secondary; period not stated) | — | [Mindful Compounding](https://mindfulcompounding.substack.com/p/a-deep-dive-into-interactive-brokers); [Bristlemoon](https://www.bristlemoonresearch.com/p/interactive-brokers-ibkr-hoovering) |
| Commission concentration | no single customer >2% of commissions | 2025 | — | [IBKR ARS FY2025](https://www.sec.gov/Archives/edgar/data/1381197/000114036126009035/ny20056593x4_ars.pdf) |
| Introducing-broker (white-label) model | IBs are typically banks, wealth managers or brokers that white-label IBKR's platform and execution; revenue is shared; one IB can bring tens of thousands of accounts | — (secondary) | — | [Bristlemoon](https://www.bristlemoonresearch.com/p/interactive-brokers-ibkr-hoovering) |

### Inferences
**Computed ratios (COMPUTED, inputs from 1.1–1.2):**

| Ratio | Value | Arithmetic |
|---|---|---|
| Margin loans ÷ client equity | Dec-25 11.6%; Mar-26 10.9%; Jun-26 11.7%; Sep-26 10.9% | 90.2/779.9; 86.0/789.4; 108.5/930.3; 105.2/964.7 |
| Client credit balances ÷ client equity | Dec-25 20.5%; Mar-26 21.4%; Jun-26 19.6%; Sep-26 19.3% | 160.1/779.9; 168.8/789.4; 182.4/930.3; 186.2/964.7 |
| Margin loans ÷ credit balances | 56%; 51%; 59%; 57% | 90.2/160.1; 86.0/168.8; 108.5/182.4; 105.2/186.2 |
| Client equity per account | Dec-25 $177k; Mar-26 $166k; Jun-26 $179k; Sep-26 $173k | 779.9bn/4.399m etc. |
| Account growth | FY2025 net adds ≈1.07m. Dec-25→Sep-26: +1.18m (+26.8% in 9 months, ≈36% annualized) | Dec-24 accounts implied as 4.399/1.32 = 3.333m; 5.576 − 4.399 = 1.177 |
| Net revenue ÷ avg client equity | FY2025 **92 bps**; Q1-26 **85 bps**; Q2-26 **88 bps** | Dec-24 equity implied as 779.9/1.37 = 569.3bn. FY25: 6,205 / ((569.3+779.9)/2 = 674.6bn). Q1: 1,669×4 / 784.7bn. Q2: 1,900×4 / ((789.4+930.3)/2 = 859.8bn) |
| Components ÷ avg client equity | FY2025: commissions 31.9 bps, NII ≈53 bps, pretax 70.7 bps. Q2-26: commissions 31.3 bps, NII 49.3 bps | 2,149, 3,600 and 4,771 over 674.6bn; 673×4 and 1,060×4 over 859.8bn |
| Revenue mix | FY2025: commissions 34.6%, NII ≈58.0%, other fees 4.7%, other income (residual) ≈2.7%. Q2-26: 35.4% / 55.8% / 4.6% / 4.2% | FY: 2,149, 3,600, 291 over 6,205; residual = 6,205−2,149−3,600−291 = 165. Q2: 673, 1,060, 87 over 1,900; residual 80 |
| Pretax margin | FY2025 76.9%; FY2024 71.3%; Q2-26 76.8% reported, 76.6% adjusted | 4,771/6,205; 3,695/5,185; 1,460/1,900; 1,440/1,880 |
| Net revenue per average account | FY2025 ≈$1,605; Q2-26 annualized ≈$1,529 | 6,205m / ((3.333+4.399)/2); 7,600m / ((4.75+5.19)/2) |
| Commission per total DART | Q2-26 ≈$2.25 | 673m / (4.82m × 62 US trading days). Below the reported $2.64 per cleared commissionable order because total DARTs include non-cleared and non-commissionable trades |
| Total DARTs per average account | Q2-26 ≈244/yr | 4.82m × 252 / 4.97m. **Not comparable** with the reported cleared-basis 159–166 |
| Execution, clearing & distribution cost ÷ commissions | Q2-26 21.1% (net commission retention ≈79%) | 142/673 |
| Client-type yield skew (1Q21) | Hedge funds + prop traders: 3% of accounts, 16% of equity, 19% of commissions. IBs: 26% of accounts, 32% of equity, 16% of commissions. Individuals: 54% of commissions on 36% of equity | sums from 1.3 |

- **Driver-tree implication:**
  - Commissions = DARTs × trading days × commission per DART. Benchmarks: about 160–166 cleared DARTs per account per year and $2.5–2.7 per cleared order.
  - NII ≈ margin loans (about 11–12% of client equity) × lending spread, plus credit balances (about 19–21%) × deposit spread, plus securities lending.
  - Costs are tiny: comp is about 10% of revenue and execution about 21% of commissions, which explains the 77% margin.
- **Definitional flag.** IBKR's "client equity" is net account equity, not gross assets. bps-on-client-equity is therefore not directly comparable with Schwab's "client assets" or the private banks' "AuM/invested assets" (see the Section 4 cross-check). That 92 bps IBKR figure is inflated relative to a gross-asset base by roughly the margin-loan share (about 11–12%).
- **Client mix.** Introducing brokers (white-label/B2B) hold disproportionately large equity but pay below-average commissions. Prop traders and hedge funds are small by count but commission-rich. A universal model should give the institutional/corporate segment a separate yield curve per client type.

### Gaps
- **Method note (applies to all sections).** WebFetch and curl to IBKR, SEC, Schwab, Business Wire, Julius Baer and other sites were blocked by the egress proxy. Every figure was therefore taken from search-engine extracts of the primary documents (listed as sources) or from press re-publications, not read in the original filings. Cross-checks passed in these cases: Schwab segment revenues sum to the reported total; IBKR quarterly vs monthly balances agree; Swissquote line items sum within CHF 1m. The per-turn web-search budget (200, shared by all agents) ran out before UBS/EFG detail, custody and ECM/DCM fees could be searched. Remaining items should be re-verified against the PDFs before external use.
- Current (FY2025) client-type split of accounts and commissions not retrieved. The 4Q25 investor presentation has a "client base by client type" page, but its numbers were not in the extract: [4Q25 presentation](https://www.interactivebrokers.com/download/investors/4Q25_Investor_Presentation.pdf). The 1Q21 split and secondary 2024 snippets are the best available.
- Exact FY2025 NII (only "≈$3.6bn"), FY2025 DARTs, and the cleared-vs-total DART split for Q2-26 were not retrieved.
- IBKR's own average client equity was not available; 2-point averages are used. Dec-2024 equity and accounts are implied from the reported y/y growth.
- Verbatim definitions (DART, cleared DART, client equity, adjusted items) were not retrieved; confirm in the 10-K "key metrics" footnotes.
- IBKR Q3 2026 results (due about mid-October 2026) were not yet published at the cut-off.

---

## 2. Charles Schwab: client assets, core NNA growth, new accounts, revenue mix, revenue and expenses on client assets (bps), daily average trades, margin and cash as % of assets, Advisor Services share

### Takeaway
Schwab is the scale benchmark for the affluent/RIA segment. It had $13.1–13.4T of client assets in mid-2026, growing organically at about 4.4–5.8% a year. It earns only about 22 bps on client assets against about 11–12 bps of expenses (FY25 adjusted pretax margin 50%, Q2-26 54.3%), and revenue is NII-heavy: about 49% NII, 27% asset-management fees, 16% trading, 4% bank-deposit fees. Advisor Services (RIA custody) holds about 44% of client assets but earns only about 21% of revenue, a yield of about 10 bps versus about 28–30 bps in Investor Services. In 2026, margin loans jumped to about 1.3% of client assets, driven by long/short strategies run by RIAs.

### Cited Findings

**2.1 FY2025 (REPORTED)**

| Metric | Value | Unit | Period | Definition / basis | Source |
|---|---|---|---|---|---|
| Total net revenues | 23.9 (segment sum 23,921) | USD bn (m) | FY2025 | +22% y/y | [Schwab 4Q25/FY25 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q4_2025_earnings_release.pdf); [Pressroom](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Reports-Record-4Q-and-Full-Year-2025-Results/default.aspx) |
| Net interest revenue | 11.8 | USD bn | FY2025 | +28% | same |
| Total expenses excluding interest | 12,462 | USD m | FY2025 | — | same |
| Pretax profit margin | 47.9 GAAP / 50.0 adjusted | % | FY2025 | adjusted (non-GAAP) is up nearly 800 bps vs 2024. GAAP check: (23,921 − 12,462)/23,921 = 47.9% ✓. Adjustment items (acquisition/integration costs, intangibles amortization) not re-verified | same |
| Core net new assets | 519 | USD bn | FY2025 | "core" = excluding significant one-off flows (definition wording not retrieved; see Gaps) | [Schwab 4Q25 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q4_2025_earnings_release.pdf); [InvestmentNews](https://www.investmentnews.com/ria-news/schwab-posts-record-2025-results-but-still-just-shy-of-wall-street-estimates/264916) |
| New brokerage accounts | 4.7 | m | FY2025 | +13% | [Schwab 4Q25 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q4_2025_earnings_release.pdf) |
| Daily average trades | 7.7 | m/day | FY2025 | +31% | same |
| Total client assets | 11,903.0 | USD bn | 31 Dec 2025 | — | [Schwab 8-K 21 Jan 2026](https://content.schwab.com/web/retail/public/about-schwab/schw_8k_01212026.pdf) |
| Client cash as % of client assets | 9.7 | % | Dec 2025 | company metric (monthly report) | [Schwab 8-K 21 Jan 2026](https://content.schwab.com/web/retail/public/about-schwab/schw_8k_01212026.pdf); [4Q25 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q4_2025_earnings_release.pdf) |
| Margin loan balances | 112.3 | USD bn | 31 Dec 2025 | +34% vs YE2024; includes $9.6bn of client margin loans for long/short strategies run by RIA clients | [Schwab 4Q25 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/316709/000031670926000004/a4q25exhibit991.htm) |
| Transactional sweep cash | 453.7 | USD bn | 31 Dec 2025 | +$28.1bn q/q (organic growth, client net buying, year-end seasonality) | [4Q25 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q4_2025_earnings_release.pdf) |
| Net interest margin | 2.90 | % | Q4 2025 | +57 bps vs 4Q24 | same |
| Expenses excl. interest ÷ avg client assets | 0.12 / 0.12 / 0.11 | % (annualized) | Q1-25 / Q3-25 / Q4-25 | company metric; the extract put FY2025 at "≈0.12%" (unconfirmed) | [Q4 2025 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q4_2025_earnings_release.pdf); [Q3 2025 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q3_2025_earnings_release.pdf); [Q1 2025 release](https://content.schwab.com/web/retail/public/about-schwab/schw_q1_2025_earnings_release.pdf) |

**2.2 FY2025 segments (REPORTED; USD m unless stated)**

| Segment | Client assets YE25 | NIR | AM&A fees | Trading | Bank deposit account fees | Other | Total | Source |
|---|---|---|---|---|---|---|---|---|
| Advisor Services | $5,195.5bn | 2,422 (+33%) | 1,750 (+11%) | 396 (+7%) | 211 (+31%) | 143 (+18%) | 4,922 (COMPUTED sum) | [Schwab 10-K FY2025](https://www.sec.gov/Archives/edgar/data/316709/000031670926000009/schw-20251231.htm); [Annual Report 2025](https://content.schwab.com/web/retail/public/about-schwab/schwab_annual_report_2025.pdf) |
| Investor Services | $6,707.5bn | 9,328 (+27%) | 4,756 (+15%) | 3,525 (+22%) | 766 (+35%) | 624 (−1%) | 18,999 (COMPUTED sum) | same |
| Total | $11,903bn | 11,750 | 6,506 | 3,921 | 977 | 767 | 23,921 (= reported $23.9bn ✓) | COMPUTED |

The extract also said each segment's client assets were "+10% vs 2024". That is inconsistent with the total's growth (about +18% from about $10.1T), so the growth figure was not used.

**2.3 2026 year-to-date (REPORTED)**

| Metric | Value | Unit | Period | Definition / basis | Source |
|---|---|---|---|---|---|
| Total net revenues | 7.1 | USD bn | Q2 2026 | +21% y/y, record | [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/charles-schwab-q2-2026-earnings-115701690.html); [Schwab Q2-26 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q2_2026_earnings_release.pdf) |
| Net interest revenue / NIM | 3.4 / 3.00% | USD bn / % | Q2 2026 | +19% y/y | same |
| Asset management & administration fees | 1.8 | USD bn | Q2 2026 | +16% | same |
| Trading revenue | 1.2 | USD bn | Q2 2026 | +28%; daily average trades a record 11.9m | same |
| Bank deposit account fees | n/a (+35% y/y) | — | Q2 2026 | growth from improving net yield; amount not in extract | same |
| Adjusted pretax margin | 54.3 | % | Q2 2026 | adjusted (non-GAAP) | same |
| Core net new assets | 119.8 (H1: 259.8) | USD bn | Q2 2026 (H1 2026) | +49% y/y (H1 +19%) | [Schwab pressroom Q2-26](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Reports-Record-Quarterly-Revenue-and-Earnings/default.aspx) |
| June core NNA / organic growth | 62.7 / 5.8% | USD bn / % annualized | Jun 2026 | "annualized organic growth rate" | same; [01net copy](https://www.01net.it/schwab-reports-record-quarterly-revenue-and-earnings/) |
| Total client assets | 13.08 | USD tn | 30 Jun 2026 | +22% y/y, +10% vs YE2025 | same |
| New brokerage accounts | 1.4 | m | Q2 2026 | — | [Schwab Q2-26 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q2_2026_earnings_release.pdf) |
| Active brokerage accounts / total client accounts | 39.8 / 48.0 | m | 30 Jun 2026 | — | same |
| Margin balances | 165.1 | USD bn | 30 Jun 2026 | long/short component: margin debits $42.1bn, short cash credits $43.7bn | [Schwab Q2-26 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q2_2026_earnings_release.pdf); [Webull transcript](https://www.webull.com/news/15268143499453440) |
| Transactional sweep cash | 485.7 | USD bn | 30 Jun 2026 | +$24.2bn q/q | [Schwab Q2-26 release](https://content.schwab.com/web/retail/public/about-schwab/schwab_q2_2026_earnings_release.pdf) |
| Advisor Services net revenues | 1,544 | USD m | Q2 2026 | +27%; segment NIR +35%, AM&A +12%, trading +28% | [Investing.com Q2-26 slides](https://www.investing.com/news/company-news/schwab-q2-2026-slides-record-results-significant-growth-runway-ahead-93CH-4803623); [Schwab 10-Q Q2-26](https://www.sec.gov/Archives/edgar/data/0000316709/000031670926000031/schw-20260630.htm) |
| Advisor Services net new assets | 80.2 | USD bn | Q2 2026 | +89% vs $42.4bn in Q2-25 | same |
| Advisor Services client assets | 5,741.9 | USD bn | 30 Jun 2026 | +22% y/y | same |
| Margin balances | 154.6 | USD bn | end-May 2026 | +38% YTD; incl. $37.4bn long/short strategies | [Business Wire (May-26 activity)](https://www.businesswire.com/news/home/20260612897792/en/Schwab-Reports-Monthly-Activity-Highlights) |
| New brokerage accounts / daily average trades | 461k / 11.8m | — | May 2026 | +37% y/y / record | same |
| Client assets / core NNA / margin | 13.04tn / 58.1bn / 169.9bn | USD | Jul 2026 | record July NNA | [Pulse 2.0](https://pulse2.com/schwab-client-assets-reach-13-04-trillion-as-july-core-net-new-assets-hit-record-58-1-billion/) |
| Total client assets | 13.41 | USD tn | end-Aug 2026 | +19% y/y, +3% m/m | [Schwab Aug-26 activity report](https://content.schwab.com/web/retail/public/about-schwab/schw_aug2026_press_release.pdf); [StockTitan](https://www.stocktitan.net/news/SCHW/schwab-reports-monthly-activity-504uwj5m7w59.html) |
| Core net new assets | 64.8 | USD bn | Aug 2026 | +46% y/y, August record | same |
| Daily average trades | 9.8 | m/day | Aug 2026 | — | same |
| Margin balances | 177.6 | USD bn | end-Aug 2026 | +58% vs YE2025; long/short strategies: margin loans $53.7bn and short credits $55.8bn | same |
| Transactional sweep cash | 483.3 | USD bn | end-Aug 2026 | +$6.5bn m/m | same |
| Client cash as % of client assets | 8.8 | % | Aug 2026 | −20 bps m/m | same |

### Inferences
**Computed ratios (COMPUTED):**

| Ratio | Value | Arithmetic / caveat |
|---|---|---|
| Revenue mix FY2025 | NIR 49.1%, AM&A 27.2%, trading 16.4%, BDA fees 4.1%, other 3.2% | lines from 2.2 ÷ 23,921 |
| Advisor Services revenue mix FY2025 | NIR 49.2%, AM&A 35.6%, trading 8.0%, BDA 4.3%, other 2.9% | ÷ 4,922 |
| Revenue on client assets FY2025 | **≈21.7 bps** (range 20–23) | 23,921 / avg client assets. Avg = (10,100 + 11,903)/2 = 11,002bn. YE2024 $10.10T is from memory of the 4Q24 release and was not re-verified. Cross-check: the implied expense ratio (11.3 bps) matches Schwab's reported 0.11–0.12%. Ending-asset basis gives 20.1 bps. Backing avg assets out of Schwab's 0.11–0.12% expense ratio gives 21.1–23.0 bps |
| Expenses on client assets FY2025 | **≈11.3 bps** | 12,462 / 11,002bn; consistent with Schwab-reported 0.11–0.12% |
| Pretax on client assets FY2025 | ≈10.4 bps | 21.7 − 11.3 |
| Revenue bps by line FY2025 | NIR 10.7, AM&A 5.9, trading 3.6, BDA fees 0.9, other 0.7 | line ÷ 11,002bn |
| Revenue on client assets Q2-26 | ≈21.7 bps (ending assets) / ≈22.7 bps (avg of YE25 and Q2-end) | 7.1bn×4 / 13.08T; 7.1bn×4 / 12.49T |
| Advisor Services revenue yield | FY25 ≈9.5 bps; Q2-26 ≈10.8 bps (ending-asset basis, a lower bound) | 4,922 / 5,195.5bn; 1,544×4 / 5,741.9bn |
| Investor Services revenue yield | FY25 ≈28.3 bps (ending-asset basis) | 18,999 / 6,707.5bn |
| Advisor Services share | 43.6% of client assets (YE25), 43.9% (Q2-26); 20.6% of revenue (FY25), 21.7% (Q2-26); 66.9% of core NNA (Q2-26) | 5,195.5/11,903; 5,741.9/13,080; 4,922/23,921; 1,544/7,100; 80.2/119.8. AS figure is NNA, which may include non-core flows |
| Organic growth (core NNA ÷ opening client assets, annualized) | FY25 ≈5.1%; Q1-26 ≈4.7%; H1-26 ≈4.4%; Jun-26 5.8% (reported) | 519/10,100; (259.8−119.8)×4/11,903; 259.8×2/11,903 |
| Margin loans ÷ client assets | YE25 0.94%; Jun-26 1.26%; Aug-26 1.32% | 112.3/11,903; 165.1/13,080; 177.6/13,410 |
| Long/short share of margin balances | YE25 8.5% → May-26 24.2% → Jun-26 25.5% → Aug-26 30.2% | 9.6/112.3; 37.4/154.6; 42.1/165.1; 53.7/177.6 |
| Sweep cash ÷ client assets | YE25 3.8%; Jun-26 3.7%; Aug-26 3.6% | 453.7/11,903; 485.7/13,080; 483.3/13,410 |
| Client cash (absolute) | YE25 ≈$1.15T; Aug-26 ≈$1.18T | 9.7% × 11,903; 8.8% × 13,410 |
| Trading revenue per trade | FY25 ≈$2.04; Q2-26 ≈$1.63 | 3,921m / (7.7m × 250 days); 1,200m / (11.9m × 62 days). Trading revenue includes PFOF, principal markups and commissions |
| Trades per active brokerage account | Q2-26 ≈75 per year | 11.9m × 252 / 39.8m (vs IBKR about 160 cleared DARTs per account) |
| Revenue per active brokerage account | Q2-26 ≈$714/yr | 7.1bn × 4 / 39.8m (vs IBKR ≈$1,530) |
| Client assets per active brokerage account | ≈$329k | 13,080bn / 39.8m. Total client assets include some assets outside active brokerage accounts |

- **Segment benchmarks.** For an "affluent self-directed + advice" segment, Investor Services (≈28–30 bps) is the better benchmark. For "B2B custody for independent advisors", Advisor Services (≈10 bps, about 49% of it NII) is the better one. Blending them gives the ≈22 bps headline.
- **Margin growth source.** The 2026 margin surge (+58% YTD to August) is largely structured long/short strategy financing for RIAs. About 30% of margin is matched by short credits. It is not ordinary retail margin, so margin ÷ assets benchmarks should strip it out where possible.

### Gaps
- Schwab's verbatim definitions of "core net new assets", "client cash as a percentage of client assets" and "daily average trades" were not retrieved (sources blocked). From memory of Schwab glossaries (unverified): core NNA excludes significant one-time flows such as acquisitions/divestitures or extraordinary single-client flows, generally >$10bn; client cash includes sweep, bank deposits, third-party bank deposit balances and money-market funds.
- The YE2024 client asset base ($10.10T) is used from memory and was not re-verified; it affects the FY25 bps and growth figures by about ±1 bp and ±0.1 pp.
- Q2-26 bank deposit account fee and "other" amounts were not retrieved; together they are a residual of ≈$0.7bn (7.1 − 3.4 − 1.8 − 1.2).
- Segment pretax income and Q1-26 segment client assets were not retrieved. Schwab's own "revenue/expense on client assets" chart from business updates was not retrieved: [Winter Business Update Jan-2026](https://content.schwab.com/web/retail/public/about-schwab/schwab_winter_business_update_012126.pdf).
- Q3-2026 results (due mid-October) were not yet published.

---

## 3. Swissquote (with Saxo as the European multi-asset broker peer): clients, client assets, net new money, revenue mix, revenue ÷ assets, white-label/B2B

### Takeaway
Swissquote is the European online-bank benchmark. It holds CHF 96.3bn of client assets (H1-26) and grows net new money at about 11–12% a year. It earns about 79–88 bps on average client assets with a 50–58% pretax margin. FY25 revenue was balanced: about 30% NII, 29% fees, 17% trading ex-FX, 13% eForex and 12% crypto. Crypto is the swing factor: it fell 66% in H1-26, and the company cut its FY26 guidance to CHF 730m revenue and CHF 365m pretax. Saxo is the comparable multi-asset broker with EUR 133bn client assets and >1.5m clients, but it earns only about 58 bps (H1-25, computed) and was barely profitable in H2-25.

### Cited Findings

**3.1 Swissquote (REPORTED)**

| Metric | Value | Unit | Period | Definition / basis | Source |
|---|---|---|---|---|---|
| Net revenues | 723.3 | CHF m | FY2025 | +9.4% y/y. One article cites FY2024 as CHF 655m, which conflicts with +9.4% (that implies ≈661m) | [Swissquote FY2025 ad hoc release](https://www.swissquote.com/en/api/internal/media/get-media?filename=press-releases/ad+hoc+MI+Swissquote+FY+2025_EN.pdf); [FinanceMagnates](https://www.financemagnates.com/forex/swissquotes-2025-revenue-and-pre-tax-profits-beat-guidance/) |
| Pretax profit | 420.2 | CHF m | FY2025 | includes ≈CHF 50m positive one-offs, chiefly the revaluation of the Yuh stake after full acquisition | [FinanceMagnates](https://www.financemagnates.com/forex/swissquotes-2025-revenue-and-pre-tax-profits-beat-guidance/); [finews](https://www.finews.com/news/english-news/70862-swissquote-ergebnis-vorlaeufig-2025-yuh-2) |
| Net fee & commission income (excl. crypto) | 209.4 | CHF m | FY2025 | +17.5%; higher trading activity | [Swissquote FY2025 release](https://www.swissquote.com/en/api/internal/media/get-media?filename=press-releases/ad+hoc+MI+Swissquote+FY+2025_EN.pdf) |
| Net interest income | 217.6 | CHF m | FY2025 | −3.0% (CHF rate cuts) | same |
| Net crypto assets income | 85.7 | CHF m | FY2025 | +0.2% | same |
| eForex income, net | 91.1 | CHF m | FY2025 | −3.8% | same |
| Net trading income (excl. FX and crypto) | 120.4 | CHF m | FY2025 | +47.4% | same |
| Client assets | 88.7 | CHF bn | 31 Dec 2025 | "approached CHF 89bn". The exact 88.7 came from a search extract whose page was not pinned | [Swissquote FY2025 release](https://www.swissquote.com/en/api/internal/media/get-media?filename=press-releases/ad+hoc+MI+Swissquote+FY+2025_EN.pdf); [TipRanks](https://www.tipranks.com/news/company-announcements/swissquote-posts-strong-2025-with-pre-tax-profit-near-chf-420-million) |
| Client assets | 76 | CHF bn | 31 Dec 2024 | — | [Vontobel report](https://www.vontobel.com/contentassets/fbf8dcc42b1f47dc9d8155fb4ee1d94f/company-report_swissquote_2025-09-25_en.pdf) |
| Net new money | 8.5 | CHF bn | FY2025 | — | [TipRanks](https://www.tipranks.com/news/company-announcements/swissquote-posts-strong-2025-with-pre-tax-profit-near-chf-420-million) |
| Net new accounts | 506,718 | accounts | FY2025 | likely includes the Yuh accounts consolidated after the full acquisition (not confirmed) | [TipRanks](https://www.tipranks.com/news/company-announcements/swissquote-posts-strong-2025-with-pre-tax-profit-near-chf-420-million); [FinanceMagnates](https://www.financemagnates.com/forex/swissquotes-2025-revenue-and-pre-tax-profits-beat-guidance/) |
| Net revenues | 364.2 | CHF m | H1 2026 | +1.7% y/y | [Swissquote H1-26 release](https://www.swissquote.com/en/api/internal/media/get-media?filename=press-releases%2Fad+hoc_EN_Media_Release_H1_2026.pdf); [Hubbis](https://hubbis.com/news/swissquote-cuts-2026-guidance-as-crypto-income-slumps-in-first-half) |
| Pretax profit / margin | 182.9 / 50.2% | CHF m / % | H1 2026 | −1.2% y/y | [SwissWealthHub](https://swisswealthhub.substack.com/p/swissquote-h1-2026-results); [Financefeeds](https://financefeeds.com/swissquote-cuts-2026-guidance-as-crypto-revenue-falls-66-despite-record-chf-96-3-billion-in-client-assets/) |
| Net profit | 153.6 | CHF m | H1 2026 | −2.9% (H1-25: 158.2) | same; [MarketScreener](https://www.marketscreener.com/news/swissquote-group-holding-sa-reports-earnings-results-for-the-half-year-ended-june-30-2026-ce7859d9da8af522) |
| Net fee & commission income | 123.7 | CHF m | H1 2026 | +13% | [Hubbis](https://hubbis.com/news/swissquote-cuts-2026-guidance-as-crypto-income-slumps-in-first-half) |
| Net interest income | 115.9 | CHF m | H1 2026 | +7.2% | same |
| Net crypto assets income | 14.6 | CHF m | H1 2026 | −66.2% (low volatility, lower prices, risk aversion) | same; [Bitcoin.com](https://news.bitcoin.com/crypto-news/swissquote-cuts-revenue-target-as-crypto-income-plunges-66-2/) |
| eForex / trading income | eForex +9.1%; trading +15.8% (Hubbis) vs "CHF 107.5m, +5%" (another extract) | CHF m / % | H1 2026 | **conflicting extracts**; residual eForex + trading = 110.0 (COMPUTED) | [Hubbis](https://hubbis.com/news/swissquote-cuts-2026-guidance-as-crypto-income-slumps-in-first-half); [Yahoo call highlights](https://finance.yahoo.com/markets/stocks/articles/swissquote-group-holding-sa-wbo-010618528.html) |
| Client assets | 96.3 | CHF bn | 30 Jun 2026 | +19.8% y/y, record | [Swissquote H1-26 release](https://www.swissquote.com/en/api/internal/media/get-media?filename=press-releases%2Fad+hoc_EN_Media_Release_H1_2026.pdf) |
| Net new money | 5.1 | CHF bn | H1 2026 | 2nd-best half-year ever | same |
| New accounts / total | +64k Swissquote, +24k Yuh; total >1.2m | accounts | H1 2026 | >60k new clients YTD | [Yahoo call highlights](https://finance.yahoo.com/markets/stocks/articles/swissquote-group-holding-sa-wbo-010618528.html); [Hubbis](https://hubbis.com/news/swissquote-cuts-2026-guidance-as-crypto-income-slumps-in-first-half) |
| FY2026 guidance | revenue ≈730 (was 760); pretax ≈365 (was 385) | CHF m | FY2026E | company guidance | [Hubbis](https://hubbis.com/news/swissquote-cuts-2026-guidance-as-crypto-income-slumps-in-first-half) |
| B2B / white-label | >600 B2B partners. White-labelled platform for PostFinance (clients log in via PostFinance e-banking). B2B clients: full-service and private banks, independent asset managers, brokers, insurers, family offices | — | 2024–25 | no B2B revenue or asset split disclosed in extracts | [Hubbis (partnership model)](https://hubbis.com/article/swissquote-spreading-the-word-of-its-state-of-the-art-global-trading-and-custody-solutions-platform-via-its-partnership-model); [Swissquote Institutional](https://www.swissquote.com/en/institutional) |

**3.2 Saxo Bank (REPORTED)**

| Metric | Value | Unit | Period | Definition / basis | Source |
|---|---|---|---|---|---|
| Net profit | 539 (≈$85m) | DKK m | FY2025 | FY2024: DKK 1,005m | [FX News Group (H2-25)](https://fxnewsgroup.com/forex-news/retail-forex/saxo-bank-sees-2-revenue-decline-posts-loss-in-h2-2025/) |
| Adjusted net profit | 120 | EUR m | FY2025 | company "adjusted" | [WealthBriefing](https://www.wealthbriefing.com/html/printarticle.php?id=205444) |
| Clients | >1.5 | m | YE2025 | YE2024: 1.29m | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/saxo-bank-sees-2-revenue-decline-posts-loss-in-h2-2025/) |
| Client assets | 995 (≈$157bn; EUR 133bn) | DKK bn | YE2025 | YE2024: DKK 853bn | same; [WealthBriefing](https://www.wealthbriefing.com/html/printarticle.php?id=205444) |
| H2 2025 | revenue −2%, net loss | — | H2 2025 | — | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/saxo-bank-sees-2-revenue-decline-posts-loss-in-h2-2025/) |
| Total income | 335 (H1-24: 311) | EUR m | H1 2025 | — | [Mondo Visione](https://mondovisione.com/media-and-resources/news/saxo-bank-announces-h1-2025-results-with-steady-growth-in-net-profits-and-a-reco-2025828/) |
| Net profit | 73 | EUR m | H1 2025 | +18% | [FinanceMagnates](https://www.financemagnates.com/forex/saxo-bank-grows-client-base-to-14-million-profits-climb-18-in-h1-2025) |
| Clients / client assets | 1.4m / EUR 118bn | — | 30 Jun 2025 | record | same |
| Q1-2026 update | "record-breaking number of clients and client assets" (figures not in extract) | — | 14 Apr 2026 | — | [Saxo press release](https://www.home.saxo/en-sg/content/commentaries/pr/press-release/saxo-bank-reports-record-breaking-number-of-clients-and-client-assets-14042026) |

### Inferences
**Computed ratios (COMPUTED):**

| Ratio | Value | Arithmetic |
|---|---|---|
| Swissquote revenue ÷ avg client assets | FY25 **87.8 bps**; H1-26 **78.7 bps** (annualized) | 723.3 / ((76.0+88.7)/2 = 82.35bn); 364.2×2 / ((88.7+96.3)/2 = 92.5bn) |
| Swissquote pretax ÷ avg client assets | FY25 51.0 bps (incl. ≈50m one-offs); H1-26 39.5 bps | 420.2/82.35bn; 182.9×2/92.5bn |
| Swissquote pretax margin | FY25 58.1% reported (≈51% if the ≈CHF 50m one-off is stripped from profit only); H1-26 50.2%; FY26 guidance 50.0% | 420.2/723.3; (420.2−50)/723.3; 365/730 |
| Swissquote NNM growth | FY25 11.2%; H1-26 11.5% annualized | 8.5/76.0; 5.1×2/88.7 |
| Swissquote revenue mix FY25 | NII 30.1%, fees 29.0%, trading ex-FX 16.6%, eForex 12.6%, crypto 11.8% | lines ÷ 723.3 (lines sum to 724.2, a CHF 0.9m difference) |
| Swissquote revenue mix H1-26 | fees 34.0%, NII 31.8%, eForex + trading 30.2% (residual), crypto 4.0% | 123.7, 115.9, 110.0, 14.6 over 364.2 |
| Swissquote client assets per account | ≈CHF 80k (upper bound) | 96.3bn / ">1.2m" accounts (incl. low-balance Yuh accounts) |
| Saxo revenue ÷ avg client assets | H1-25 ≈**57.7 bps** | 335×2 / ((114.3+118)/2). YE24 = DKK 853bn / 7.46 = EUR 114.3bn |
| Saxo client assets per client | ≈EUR 89k | 133bn / 1.5m |
| Saxo H2-25 net profit (implied) | ≈ −DKK 6m (≈ break-even) | 539 − 73 × 7.46. Consistent with the reported "loss in H2-25" |

- **Revenue-mix volatility.** Swissquote's crypto line went from 11.8% of revenue (FY25) to 4.0% (H1-26), so a model needs a volatility- or price-linked driver for crypto, separate from equities brokerage.
- **Yield-gap explanation.** The two platforms share a multi-asset, FX/CFD-heavy model, but Saxo's yield gap (≈58 vs ≈80–88 bps) and its weak H2-25 suggest pricing pressure and a cost base not yet scaled. This is an inference, and revenue definitions differ: total income vs net revenues.

### Gaps
- See the method note in Section 1 › Gaps.
- No disclosed B2B or white-label revenue or asset split for Swissquote; the share of client assets from B2B partners was not found. Saxo's white-label (B2B2C) partner economics were not retrieved.
- The H1-26 eForex amount and the "net trading income" figure conflict between extracts; resolve from the [H1-26 press-conference deck](https://www.swissquote.com/en/api/internal/media/get-media?filename=2026-08%2FPress+conference+Results+H1-2026+vFinal.pdf).
- Swissquote's own definition of "client assets" (deposits + custody securities + crypto, incl. Yuh?) and of "net new monies" was not retrieved verbatim.
- Saxo H1-2026 results and its revenue split (commission vs spread vs NII) were not retrieved. Saxo ownership changes were not researched.

---

## 4. Wealth/affluent benchmarks (Julius Baer, UBS GWM, EFG): gross margin on AuM, NNM growth, cost/income, AuM and clients per RM, mandate share and fees, structured products

### Takeaway
On their own AuM definitions, the pure-play private banks earn **82–97 bps** gross margin: Julius Baer 82–87 bp, EFG 91–97 bp. UBS GWM earns about 58–59 bps (computed) on a broader invested-asset base with a large US advisor business. NNM growth is 2–3% a year at JB and UBS and about 6% at EFG. Cost/income is 62.6% (JB H1-26 adjusted) to 75.6% (UBS GWM FY25). JB's AuM per relationship manager is CHF 413–438m. At UBS GWM, fee-generating (mandate and fund) assets are about 44% of invested assets (computed); mandate penetration was 38% in Q3-24. Clients per RM, mandate fee levels and structured-product contribution were not found.

### Cited Findings

**4.1 Julius Baer (REPORTED)**

| Metric | Value | Unit | Period | Definition / basis | Source |
|---|---|---|---|---|---|
| AuM | 547 | CHF bn | 30 Jun 2026 | all-time high | [Julius Baer HY2026 release](https://www.juliusbaer.com/en/media/news-portal/presentation-of-the-2026-half-year-results-of-the-julius-baer-group/); [EQS](https://www.eqs-news.com/news/ad-hoc/presentation-of-the-2026-half-year-results-for-the-julius-baer-group/f76695d3-f05c-4484-9c41-cee51535fc62_en) |
| Net new money | 5.7 (2.2% annualized) | CHF bn | H1 2026 | after a slow start | same |
| Gross margin | 87 (H1-25 underlying 83) | bp | H1 2026 | exceptionally high Q1 client activity | same; [WealthBriefing](https://www.wealthbriefing.com/html/article.php/julius-baer-net-profit-doubles-to-new-record-in-h1-2026-) |
| Adjusted cost/income ratio | 62.6 (H1-25 underlying 68.2) | % | H1 2026 | adjusted | same |
| Net profit (IFRS = adjusted) | 673 | CHF m | H1 2026 | +32% vs underlying CHF 511m | same |
| Net commission & fee income | 1,279 | CHF m | H1 2026 | +12%: higher recurring income on AuM plus brokerage from client activity | [Investing.com HY26 slides](https://www.investing.com/news/company-news/julius-bar-h1-2026-slides-record-profit-amid-strategic-transformation-93CH-4802021); [JB HY2026 deck](https://www.juliusbaer.com/index.php?eID=dumpFile&t=f&f=109334&token=81c7eee862d5f29f1c1e49275dd97e898da64629fc12f6be508c851b59a29f49) |
| Net interest income | 130 | CHF m | H1 2026 | +80%: interest expense −21% (lower client deposit rates), interest income −13% | same |
| Relationship managers | 1,247 | FTE | 30 Jun 2026 | −14 YTD (50 hired, 64 left) | same |
| AuM per RM | 438 | CHF m | 30 Jun 2026 | +6% YTD | same |
| AuM | 521 | CHF bn | 31 Dec 2025 | +5% | [JB FY2025 presentation](https://www.juliusbaer.com/index.php?eID=dumpFile&t=f&f=106605&token=7f6c6a311ae7162895f016c72d03b3dd8e109673); [EQS FY25](https://www.eqs-news.com/news/ad-hoc/presentation-of-the-2025-full-year-results-for-the-julius-baer-group/802d4961-fef8-4dc1-b0de-f0b99b109618_en) |
| Net new money | 14.4 (2.9%) | CHF bn | FY2025 | mainly Asia (HK, India, Singapore, Thailand), W. Europe (UK & Ireland, Germany, Iberia), Middle East (UAE) | same |
| Gross margin | 82 underlying (−1 bp) / 77.4 "adjusted" | bp | FY2025 | **two bases in the extract**; the gap likely reflects 2025 one-off and credit items | same |
| Adjusted cost/income ratio | 71.3 | % | FY2025 | adjusted | same |
| Relationship managers | 1,262 | FTE | 31 Dec 2025 | 1,261 implied by H1-26 (1,247 + 14) | [JB AR 2025 extract](https://www.juliusbaer.com/index.php?eID=dumpFile&t=f&f=106603&token=57cb59f63407ff15c5951216d075e9626e594707) |

**4.2 UBS Global Wealth Management (REPORTED)**

| Metric | Value | Unit | Period | Definition / basis | Source |
|---|---|---|---|---|---|
| Invested assets | 4,942 | USD bn | 30 Jun 2026 | +$274bn q/q (+6%) | [WealthBriefing](https://www.wealthbriefing.com/html/article.php/ubss-wealth-results-in-q2-2026-show-revenue,-aum-increase;-group-profits-beat-forecasts); [Funds Society](https://www.fundssociety.com/en/news/business/ubs-delivers-another-record-quarter-driven-by-wealth-management-business/) |
| Net new assets | 36 (3% annualized) | USD bn | Q2 2026 | — | same |
| Total revenues | 7,112 | USD m | Q2 2026 | +13% y/y | [WealthBriefing](https://www.wealthbriefing.com/html/article.php/ubss-wealth-results-in-q2-2026-show-revenue,-aum-increase;-group-profits-beat-forecasts) |
| Underlying revenues | 6,997 | USD m | Q2 2026 | +14% y/y, double-digit growth in all lines; underlying transaction-based income +23% y/y | [Business Wire UBS 2Q26](https://www.businesswire.com/news/home/20260728010217/en/UBS-reports-2Q26-net-profit-of-USD-2.8bn-and-USD-5.8bn-for-1H26-with-robust-momentum-across-businesses-Group-invested-assets-at-USD-7.3trn-Ad-hoc-announcement-pursuant-to-Article-53-of-the-SIX-Exchange-Regulation-Listing-Rules); [UBS 2Q26 media page](https://www.ubs.com/global/en/media/display-page-ndp/en-20260729-2q26-quarterly-result.html) |
| Underlying profit before tax | 3,971 | USD m | H1 2026 | underlying | [UBS 6-K 2Q26](https://www.sec.gov/Archives/edgar/data/0001610520/000161052026000082/ubs-20260630.htm) |
| Group cost/income ratio (not GWM) | ≈70 | % | Q2 2026 | Group-wide | [MarketBeat call highlights](https://www.marketbeat.com/instant-alerts/ubs-group-q2-earnings-call-highlights-2026-07-29/) |
| GWM PBT excl. litigation | 6.1 (+23%) | USD bn | FY2025 | each of 4 regions ≈$1.5bn | [UBS 4Q25 investor presentation text (6-K)](https://www.sec.gov/Archives/edgar/data/1610520/000161052026000014/investorpresotext4q25.htm) |
| GWM cost/income ratio | 75.6 (>3 pp better) | % | FY2025 | basis as presented (likely excl. litigation) | same |
| Invested assets / fee-generating assets | ≈4.8T / ≈2.1T | USD | YE2025 | fee-generating assets "include discretionary or advisory mandates and investment funds" | [UBS Annual Report 2025](https://www.ubs.com/content/dam/assets/cc/investor-relations/annual-report/2025/annual-report-ubs-group-2025.pdf); [20-F FY2025](https://www.sec.gov/Archives/edgar/data/0001610520/000161052026000023/ubs-20251231.htm) |
| Net new assets | 8.5 | USD bn | Q4 2025 | — | [UBS 4Q25 investor presentation text (6-K)](https://www.sec.gov/Archives/edgar/data/1610520/000161052026000014/investorpresotext4q25.htm); [UBS 4Q25 report](https://www.ubs.com/content/dam/assets/cc/investor-relations/quarterlies/2025/4q25/full-report-ubs-group-consolidated-4q25.pdf) |
| GWM mandate penetration | 38 (+2 pp y/y) | % | Q3 2024 | rose for the 4th consecutive quarter in 2025; 2025 level not in extract | [UBS call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/02/05/ubs-ubs-q3-2024-earnings-call-transcript/) |
| MyWay (discretionary) invested assets | >30 (≈doubled y/y) | CHF bn (currency as quoted) | 2025 | — | [UBS Annual Report 2025](https://www.ubs.com/content/dam/assets/cc/investor-relations/annual-report/2025/annual-report-ubs-group-2025.pdf) |

**4.3 EFG International (REPORTED)**

| Metric | Value | Unit | Period | Definition / basis | Source |
|---|---|---|---|---|---|
| Operating income | 856.5 | CHF m | H1 2026 | +7% y/y excl. 2025 insurance recovery; net commission income +20% | [WealthBriefing](https://www.wealthbriefing.com/html/article.php/efg-international-profit-rises-5-per-cent%3B-assets-over-sfr200-billion) |
| Revenue margin | 91 (H2-25: 93; H1-25: 97 excl. insurance recovery) | bp | H1 2026 | lower rates weighed on interest income | same |
| AuM | 196.3 (+21% y/y); >200 after Quilvest Switzerland closed 21 Jul 2026 | CHF bn | 30 Jun 2026 | — | same; [Private Banker International](https://www.privatebankerinternational.com/news/efg-aum-h1-2026/) |
| Net new assets | 5.7 (6.2% annualized; target 4–6%) | CHF bn | H1 2026 | — | same |
| Net profit | 184.6 (+5%) | CHF m | H1 2026 | — | same |

### Inferences
**Computed ratios (COMPUTED):**

| Ratio | Value | Arithmetic |
|---|---|---|
| JB AuM per RM | FY25 CHF 413m; H1-26 CHF 439m (reported 438) | 521bn/1,262; 547bn/1,247 |
| JB operating income H1-26 (approx.) | ≈CHF 2.32bn | 87 bp × avg AuM ((521+547)/2 = 534bn) ÷ 2. JB uses monthly-average AuM |
| JB revenue mix H1-26 (approx.) | fees & commissions ≈55%, NII ≈6%, FVTPL/trading + other ≈39% | 1,279, 130 and residual 914 over ≈2,323. JB's FVTPL line includes treasury FX-swap income that is economically interest-like |
| JB pretax margin on AuM H1-26 (approx.) | ≈33 bp | 87 × (1 − 0.626); ignores credit-loss provisions |
| UBS GWM revenue ÷ avg invested assets | Q2-26 ≈**59.2 bps** reported / ≈58.2 bps underlying | 7.112bn×4 / ((4,668 + 4,942)/2 = 4,805bn), where Q1-end = 4,942 − 274 = 4,668; 6.997bn×4 / 4,805bn |
| UBS GWM NNA growth | Q2-26 ≈3.1% annualized (reported "3%") | 36×4 / 4,668 |
| UBS GWM fee-generating share of invested assets | ≈44% | 2.1/4.8 |
| EFG implied average AuM | ≈CHF 188bn | 856.5×2 / 0.0091 (consistent with 196.3 closing) |

**Cross-segment comparison (REPORTED or COMPUTED as noted; see the section sources):**

| Firm (segment proxy) | Asset base definition | Revenue ÷ assets (bps) | Cost/income or margin | Organic growth | Assets per client / RM |
|---|---|---|---|---|---|
| IBKR (active traders + institutions) | client equity (net of margin) | 85–92 (C) | pretax margin ≈77% → C/I ≈23% (C) | accounts +35% y/y; equity +27–40% incl. markets | ≈$173k per account (C) |
| Schwab total | total client assets | ≈22 (C) | adj. pretax 50% FY25, 54% Q2-26 | core NNA 4.4–5.8% | ≈$329k per active brokerage account (C) |
| Schwab Advisor Services (B2B RIA custody) | AS client assets | ≈10 (C) | n/a | AS NNA ≈5.6% annualized on ending assets (C) | n/a |
| Schwab Investor Services (retail/affluent) | IS client assets | ≈28 (C) | n/a | n/a | n/a |
| Swissquote | client assets (deposits + custody + crypto) | 79–88 (C) | pretax 50–58% | NNM 11–12% (C) | ≈CHF 80k per account (C) |
| Saxo | client assets | ≈58 (C, H1-25) | thin (H2-25 loss) | n/a | ≈EUR 89k per client (C) |
| Julius Baer | AuM | 82–87 (R) | adj. C/I 62.6–71.3% (R) | NNM 2.2–2.9% (R) | CHF 413–438m per RM |
| EFG | AuM | 91–97 (R) | n/a | NNA 6.2% (R) | n/a |
| UBS GWM | invested assets | ≈58–59 (C) | C/I 75.6% FY25 (R) | NNA ≈3% (R) | n/a |

- **Comparability flag.** Private-bank margins are on AuM/invested assets, which exclude custody-only assets. Broker yields are on broader "client assets" (Swissquote, Saxo, Schwab) or net "client equity" (IBKR). On a like-for-like gross basis, private-bank yields would be lower than shown.
- **Wealth benchmark band.**
  - Gross margin: about 80–95 bp for advisory-led private banking; about 60 bp for a scaled, US-heavy wealth manager.
  - Cost/income: 62–76%.
  - NNM: 2–6% a year.
  - These contrast with digital brokers: about 80–90 bps yield at a 50–77% pretax margin, with NNM 11–12% (Swissquote) or account growth of 30%+ (IBKR).
- **Recurring vs. activity.** JB's jump from 83 to 87 bp came from Q1-26 client activity (brokerage/transactional). UBS GWM underlying transaction-based income rose 23% y/y. For a 2026 base year, part of the margin is cyclical: activity-driven, not recurring.

### Gaps
- See the method note in Section 1 › Gaps.
- UBS GWM's reported "gross margin on invested assets" (bps), FY2025 revenues and NNA, current mandate penetration, and number of client advisors / clients per advisor were not retrieved. The search budget was exhausted; see the [UBS 2Q26 report (6-K)](https://www.sec.gov/Archives/edgar/data/0001610520/000161052026000082/ubs-20260630.htm).
- EFG's cost/income ratio, number of client relationship officers (CROs), AuM per CRO and FY2025 figures were not retrieved.
- JB mandate penetration (advisory + discretionary share of AuM), client counts per RM and the verbatim gross-margin definition (adjusted vs underlying) were not retrieved. The FY2025 77.4 bp vs 82 bp discrepancy is unresolved.
- No mandate fee levels (e.g., the typical all-in discretionary fee as % of AuM) and no structured-products contribution to revenue were found for any of the three banks. Industry studies (BCG Global Wealth, McKinsey private banking survey) were not reached before the search budget ran out.

---

## 5. Institutional brokerage pricing: commission levels for institutional/DMA flow, custody fees (bps), ECM/DCM underwriting fees, market-making and liquidity-provision fee practices

### Takeaway
Within the retrieved sources, only IBKR gives granular institutional/DMA price points:
- top-tier US stock commission $0.0035/share;
- introducing-broker markups capped at 15× that rate (≈$0.0525/share);
- US options markups capped at 10% of trade value;
- about $2.6 average per cleared order including exchange, clearing and regulatory fees;
- execution and clearing costs about 21% of commissions.

Prop trading groups and hedge funds are about 3% of IBKR accounts but 19–25% of commissions. Custody bps, ECM/DCM fee ranges and market-making fee benchmarks **could not be sourced in this session**. They are listed under Gaps as unverified orientation values only.

### Cited Findings

| Metric | Value | Unit | Period | Definition / basis | Source |
|---|---|---|---|---|---|
| IBKR highest-tier rate, US stocks (tiered pricing) | 0.0035 | USD/share | current | the reference rate for introducing-broker markup caps | [IBKR "Broker" (introducing broker) page](https://www.interactivebrokers.com/en/accounts/broker.php) |
| Introducing-broker markup cap, stocks | ≤15× IBKR's highest tiered rate + external fees | — | current | B2B/white-label pricing guard-rail | same |
| Introducing-broker markup cap, US options | ≤10% of trade value | — | current | — | same |
| Avg commission per cleared Commissionable Order | 2.57 (Sep-26); 2.64 (Q2-26) | USD/order | 2026 | incl. exchange, clearing and regulatory fees | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/interactive-brokers-registers-6-y-y-increase-in-darts-in-sep-2026/); [Morningstar/BW](https://www.morningstar.com/news/business-wire/20260721157186/interactive-brokers-group-announces-2q2026-results) |
| Execution, clearing & distribution fees | 142 | USD m | Q2 2026 | +$19m regulatory fees from the SEC Section 31 fee-rate increase on 4 Apr 2026; offset by more liquidity rebates captured from exchanges on higher stock/option volumes | [Morningstar/BW 2Q26](https://www.morningstar.com/news/business-wire/20260721157186/interactive-brokers-group-announces-2q2026-results) |
| Market-structure fee items inside IBKR "other fees" | PFOF from exchange-mandated programs (+$9m y/y), risk exposure fees (+$8m), market data fees (+$3m) | USD m (increments) | Q2 2026 | options-exchange PFOF programs pass marketing fees to brokers | same |
| Prop trading groups' share of commissions | 13% (1Q21); 18% (H1-24, secondary) | % | — | prop firms: 2% of accounts | [IBKR 1Q21 presentation](https://investors.interactivebrokers.com/download/investors/1Q21_IBKR_Presentation.pdf); [Bristlemoon](https://www.bristlemoonresearch.com/p/interactive-brokers-ibkr-hoovering) |
| Hedge funds' share of commissions | 6% (1Q21); 7% (H1-24, secondary) | % | — | 1% of accounts, 6–7% of equity | same |
| Introducing brokers' share | 26% of accounts, 32% of equity, 16% of commissions | % | 1Q21 | white-label/omnibus-type flow | [IBKR 1Q21 presentation](https://investors.interactivebrokers.com/download/investors/1Q21_IBKR_Presentation.pdf) |
| Schwab trading revenue | 3,921 (FY25); 1.2bn (Q2-26) | USD m | — | composition (commissions, order-flow revenue, principal markups) is my description, not re-verified | [Schwab 10-K FY2025](https://www.sec.gov/Archives/edgar/data/316709/000031670926000009/schw-20251231.htm); [Yahoo Q2-26](https://finance.yahoo.com/markets/stocks/articles/charles-schwab-q2-2026-earnings-115701690.html) |
| UBS GWM transaction-based income (underlying) | +23% y/y | % | Q2 2026 | UBS line item; composition not retrieved (typically brokerage, structured products, FX) | [Business Wire UBS 2Q26](https://www.businesswire.com/news/home/20260728010217/en/UBS-reports-2Q26-net-profit-of-USD-2.8bn-and-USD-5.8bn-for-1H26-with-robust-momentum-across-businesses-Group-invested-assets-at-USD-7.3trn-Ad-hoc-announcement-pursuant-to-Article-53-of-the-SIX-Exchange-Regulation-Listing-Rules) |

### Inferences
- **(COMPUTED) Implied B2B markup ceiling at IBKR: ≈$0.0525/share** (15 × 0.0035), on top of external fees. The IB economics: IBKR's base rate is the wholesale price and the markup is the partner's retail margin. That fits an "institutional/corporate → introducing broker" sub-segment.
- **(COMPUTED) Net execution economics.** At IBKR, about 21% of commission revenue (142/673) is passed to exchanges, clearing houses and regulators, so net retention is about 79%. Regulatory fee shocks such as the Section 31 rate rise move this ratio directly.
- **(COMPUTED) Revenue per trade, retail/affluent vs active-trader.** Schwab earns about $1.6–2.0 of trading revenue per trade (largely zero-commission equities monetized via order flow and principal markups); IBKR earns about $2.6 per cleared commissionable order. Use these as the price-per-transaction bounds for retail vs. active/professional flow.
- **Institutional yield concentration.** Prop and hedge-fund flow is 3% of IBKR accounts but 19–25% of commissions. Institutional active-trading revenue is therefore heavily concentrated, and a model should drive it by "active institutional accounts × turnover × per-share/per-contract price" rather than by assets.

### Gaps
- See the method note in Section 1 › Gaps. No source was retrieved this session for any of the items below. The orientation values are **UNVERIFIED background knowledge**: not cited, not to be used as facts, and to be confirmed in the suggested sources before entering the model.
  - **Institutional cash-equity commissions** (Coalition Greenwich; buy-side cost studies). Orientation only:
    - US high-touch ≈2–4 cents/share; low-touch, algo or DMA ≈0.5–1.5 cents/share.
    - Europe high-touch ≈8–12 bps; low-touch ≈2–5 bps of value traded.
    - Unbundling under MiFID II pushed rates down.
    - Low confidence.
  - **Custody fees.** Orientation only:
    - Large global custodians earn about 1 bp or less of assets under custody/administration on core servicing. Derivable as servicing-fee revenue ÷ AUC/A from State Street or BNY 10-Ks.
    - Private-bank and retail custody fees in Switzerland are often ~0.1–0.4% p.a. of custody assets.
    - Medium/low confidence.
  - **ECM fees.** Orientation only:
    - US IPO gross spreads cluster at 7% for mid-sized deals (Chen & Ritter, "The Seven Percent Solution", Journal of Finance 2000) and fall for very large IPOs.
    - European IPO fees are roughly half that, ≈2–4% (Abrahamson, Jenkinson & Jones, Journal of Finance 2011).
    - Follow-ons ≈3–5%; accelerated bookbuilds/blocks ≈1–3% (fee or discount).
    - Medium confidence for the US 7% figure; lower for the rest.
  - **DCM fees.** Orientation only: investment-grade corporate bond gross spreads ≈0.3–0.9% of issue size depending on tenor; high-yield ≈1.5–2.5%. Low-medium confidence.
  - **Market-making / liquidity provision.** Orientation only:
    - US exchange maker-taker access fees are capped by SEC Rule 610 (historically $0.0030/share; 2024 amendments lowered the cap for most stocks priced ≥$1 — check the compliance status).
    - Retail PFOF runs roughly 0.1–0.2 cents/share for equities and a few tens of cents per options contract.
    - In European and Nordic small caps, issuers pay liquidity providers a fixed annual retainer under liquidity-provider agreements.
    - Low confidence; no amounts sourced.
- No company-reported institutional custody or underwriting figures were retrieved for the peer set. Schwab, IBKR and Swissquote do not run material ECM/DCM franchises. UBS's Investment Bank and Julius Baer/EFG structured-product revenues were not reached.
- Suggested primary sources for follow-up:
  - SEC Rule 606 reports for PFOF rates.
  - LSEG or Dealogic fee data, or Jay Ritter's IPO statistics, for gross spreads.
  - State Street and BNY 10-K servicing fees and AUC/A for custody bps.
  - Coalition Greenwich equity trading studies for commission rates.
  - Nasdaq Nordic and Euronext liquidity-provider programme documents for market-making practice.
