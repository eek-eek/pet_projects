# Mass-retail, self-directed (mobile-first) public brokers: benchmark dataset (Robinhood, eToro, flatexDEGIRO, Avanza, Nordnet; plus Webull, Trading 212, Trade Republic)

_Method and source-access note (read first). Data cut-off is 7 Oct 2026. The latest data available at research time: Robinhood Q2-2026 results and Aug-2026 monthly operating data; eToro Q2-2026; flatexDEGIRO Q2/H1-2026; Avanza and Nordnet Q2-2026 interim reports plus Aug-2026 monthly statistics. September-2026 monthly data had not been published for Robinhood, Avanza or Nordnet. In this session the egress proxy blocked direct fetching of every source host tried (sec.gov, investors.robinhood.com, etoro.com, q4cdn.com, mb.cision.com, inderes.se, mondovisione, finviz, placera). The shared web-search budget then ran out before every gap was closed. As a result, **every figure below was taken from search-engine summaries of the cited pages**. Most of those pages are the companies' own releases or reports, or verbatim wire copies of them. Each figure is attributed to the URL the search tool cited for it. Before hard-coding a figure into the model, spot-check it against the linked PDF or HTML. **[C]** marks a value I computed from cited inputs, with the arithmetic shown. Rounding in the source figures carries into computed ratios, typically by ±1–3%. Currency is native unless stated otherwise._

## 1. Client base: funded customers and accounts, "active" definitions, active share, growth, dormancy

### Takeaway
Robinhood is 6–7x larger than any European peer, with 28.6 M funded customers in Aug-2026. Its relative growth (+7% YoY) is slower than eToro's (+18%), Nordnet's (+12–13%), flatexDEGIRO's (+11%) and Avanza's (≈+8–9%). None of the companies currently publishes an "active share" KPI, such as MAU ÷ funded customers or the share of customers who traded in the period. Robinhood dropped MAU from its SEC key metrics in 2024. "Activity" therefore has to be read from each company's customer definition:
- **Robinhood:** strictest. Counts unique persons with a balance or a transaction in the last 45 days.
- **eToro:** one trade ever plus a positive balance.
- **flatexDEGIRO, Avanza, Nordnet:** count accounts or customers. I captured no activity criterion for them.

### Cited Findings

**Robinhood**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Funded Customers | 28.6 M | end Aug-2026 | +~120k MoM; +~1.90 M YoY | [HOOD Aug-2026 operating data](https://investors.robinhood.com/news-releases/news-release-details/robinhood-markets-inc-reports-august-2026-operating-data); [InvestingNews copy](https://investingnews.com/robinhood-markets-inc-reports-august-2026-operating-data/) |
| Funded Customers | 28.4 M | end Q2-2026 | +1.9 M / +7% YoY | [HOOD Q2-2026 release](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results); [8-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/0001783879/000178387926000113/q22026robinhoodexhibit991.htm) |
| Funded Customers | 27.0 M | end FY2025 | +1.8 M / +7% YoY | [HOOD Q4/FY2025 release](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-fourth-quarter-and-full-year-2025-results) |
| Funded Customers, end-FY2024 [C] | 25.2 M | end FY2024 | 27.0 − 1.8 | as above |
| YoY growth [C] | 7.1% | Aug-2026 | 1.90 ÷ (28.6 − 1.90) | [Aug-2026 data](https://investors.robinhood.com/news-releases/news-release-details/robinhood-markets-inc-reports-august-2026-operating-data) |
| Net-add run-rate [C] | ≈1.44 M/yr ≈ 5.1% of base | Aug-2026 | 0.12 M × 12 ÷ 28.5 M | as above |
| Implied average Funded Customers [C] | ≈28.0 M (implies ≈27.6 M at end-Q1-2026) | Q2-2026 | annualized Q2 revenue ÷ ARPU = (1,308 × 4) ÷ 187; end-Q1 = 2 × 27.98 − 28.4 (sensitive to rounding) | [HOOD Q2-2026 release](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results) |
| **Definition: Funded Customer** | A unique person with at least one account who, within the past 45 calendar days, had an account balance above zero or completed a transaction. Each holder of a joint account counts separately. End-clients of RIAs on the TradePMR platform are included from Q1-2025, and Bitstamp customers from June-2025. | FY2025 | Acquisitions widened the scope, so 2025 growth is not purely organic. | [SEC CORRESP 2024](https://www.sec.gov/Archives/edgar/data/1783879/000178387924000187/filename1.htm); [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000023/hood-20251231.htm) |
| **MAU status** | MAU is "no longer an input used by management or the board". It was removed from SEC filings from the Q1-2024 10-Q but kept in earnings materials "for informational purposes" at that time. | 2024 onward | No current active-share KPI. | [SEC CORRESP 2024](https://www.sec.gov/Archives/edgar/data/1783879/000178387924000187/filename1.htm) |

**eToro**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Funded Accounts | 4.28 M | end Q2-2026 | +18% YoY | [eToro Q2-2026 release (IR)](https://investors.etoro.com/news-releases/news-release-details/etoro-reports-second-quarter-2026-results); [etoro.com copy](https://www.etoro.com/news-and-analysis/press-releases/etoro-reports-second-quarter-2026-results/) |
| Funded Accounts | 4.02 M | end Q1-2026 | +12% vs 3.58 M in Q1-2025 | [eToro Q1-2026 release (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/05/12/3292651/0/en/eToro-Reports-First-Quarter-2026-Results.html) |
| Funded Accounts | 3.81 M | end Q4-2025 | +9% vs 3.48 M in Q4-2024 | [eToro Q4/FY2025 release](https://www.etoro.com/en-us/news-and-analysis/latest-news/press-release/etoro-reports-fourth-quarter-and-full-year-2025-results); [FinTech Futures copy](https://www.fintechfutures.com/press-releases/etoro-reports-fourth-quarter-and-full-year-2025-results) |
| Funded Accounts | 3.73 M | end Q3-2025 | +16% vs 3.21 M in Q3-2024 | [eToro FY2025 20-F](https://www.sec.gov/Archives/edgar/data/0001493318/000121390026022034/ea0278371-20f_etoro.htm) (via search summary) |
| Q2-2026 net adds [C] | +0.26 M (+6.5% QoQ) | Q2-2026 | 4.28 − 4.02 | as above |
| **Definition: Funded Account** | A user who has completed KYC/AML and onboarding, activated the account, deposited funds, executed at least one trade at any time, and holds a positive balance (invested or uninvested). | IPO prospectus | No recency test, so dormant accounts with a balance are included. | [eToro IPO prospectus](https://www.stifel.com/prospectusfiles/PD_7111.pdf) |
| **Data conflict** | A pre-IPO Finance Magnates article cites 3.13 M funded accounts "at end of 2024". eToro's own FY2025 release uses 3.48 M as the Q4-2024 comparator. | 2024 | Treat 3.48 M (company figure) as authoritative. 3.13 M probably refers to an earlier date. | [Finance Magnates](https://www.financemagnates.com/fintech/etoro-bets-on-growth-ahead-of-ipo-q1-income-slips-but-reach-expands/) vs [eToro FY2025](https://www.fintechfutures.com/press-releases/etoro-reports-fourth-quarter-and-full-year-2025-results) |

**flatexDEGIRO**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Customer Accounts | 3.66 M | end Q2-2026 | +5% vs YE-2025; +11% YoY | [FTK Q2-2026 press release (PDF)](https://s206.q4cdn.com/770226284/files/doc_news/2026/07/260722-flatexDEGIRO_Press-Release_Q2-2026-Results.pdf); [webdisclosure copy](https://www.webdisclosure.com/press-release/online-broker-flatexdegiro-further-expands-record-results-and-increases-net-income-by-55-percent-pIHtqXjeilQ) |
| Customer Accounts | 3.58 M | end Q1-2026 | +3% vs YE-2025 | [FTK Q1-2026 (EQS via finanzen.net)](https://www.finanzen.net/nachricht/aktien/eqs-news-flatexdegiro-starts-2026-with-a-record-quarter-15627664) |
| Customer Accounts | 3.5 M (2024: 3.1 M) | end FY2025 | +13% YoY; 446k new customer accounts in 2025 | [FTK FY2025 (EQS via boersengefluester)](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| Gross new-account rate [C] | 14.4% of opening accounts | FY2025 | 446k ÷ 3.1 M | as above |
| Definition | Counts **accounts**, not unique persons. The exact definition was not captured. | — | — | — |

**Avanza**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Customers | 2,371,900 | end Aug-2026 | +19,200 net in August | [Avanza Aug-2026 monthly statistics (PDF)](https://investors.avanza.se/files/mfn/9acfa038-d7f2-4bfd-b63b-13515552f639/august-monthly-statistics.pdf); [Inderes copy](https://www.inderes.se/en/releases/august-monthly-statistics-7) |
| Customers | 2,338,300 | end Q2-2026 | +40,300 net in Q2-2026 | [Avanza Jan–Jun 2026 interim report (PDF)](https://storage.mfn.se/bec572f7-2a0c-4659-a0e0-c6b1214b997f/avanza-bank-holding-ab-publ-interim-report-january-june-2026.pdf); [Inderes copy](https://www.inderes.se/en/releases/avanza-bank-holding-ab-publ-interim-report-january-june-2026) |
| Customers | 2,242,700 | end FY2025 | +171,000 in 2025 | [Avanza FY2025 preliminary statement (PDF)](https://storage.mfn.se/0fe566e9-ab2b-4934-9b74-a0c97530ebe3/avanza-bank-holding-ab-publ-preliminary-financial-statement-2025.pdf); [Inderes copy](https://www.inderes.fi/en/releases/avanza-bank-holding-ab-publ-preliminary-financial-statement-2025) |
| H1-2026 net adds [C] | 95,600 | H1-2026 | 2,338,300 − 2,242,700. Company slides say "~100k new customers in H1". | [Investing.com Q2-2026 slides](https://ng.investing.com/news/company-news/avanza-q2-2026-slides-record-profit-100k-new-customers-in-h1-93CH-2598106) |
| Customer growth [C] | 8.3% | FY2025 | 171,000 ÷ (2,242,700 − 171,000 = 2,071,700) | as above |
| Customer growth [C] | 5.8% YTD (≈8.6% annualized) | Jan–Aug 2026 | 129,200 ÷ 2,242,700; × 12/8 | as above |

**Nordnet**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Customers | 2,544,000 | end Aug-2026 | +12.3% YoY; 23,700 new customers in August | [Nordnet Aug-2026 monthly statistics (MFN)](https://mfn.se/all/a/nordnet/nordnet-monthly-statistics-august-f963d7ba); [Inderes copy](https://www.inderes.dk/en/releases/nordnet-monthly-statistics-august-5) |
| Customers | >2.5 M | end Q2-2026 | +13% YoY; 73,600 new customers in Q2-2026 (Q2-2025: 56,800) | [Nordnet Q2-2026 interim report (PDF)](https://nordnetab.com/wp-content/uploads/2026/07/2Q26-report.pdf); [Investing.com](https://www.investing.com/news/earnings/nordnet-q2-profit-hits-record-as-trading-boom-customer-inflows-lift-earnings-4797398); [call highlights](https://ca.investing.com/news/company-news/nordnet-ab-publ-fra9jl-q2-2026-earnings-call-highlights-record-revenue-and-customer--4745172) |
| Customers | 2.35 M | end FY2025 | ≈250k new savers; +12% | [Nordnet Annual Report 2025 release (Cision)](https://news.cision.com/nordnet/r/nordnet-publishes-annual-and-sustainability-report-for-2025,c4320623) |
| Customers | >2 M | end FY2024 | 256,300 new customers in 2024. Growth of 14.3% after adjusting for the sale of the unsecured-loan portfolio to Ikano Bank on 1 Oct 2024. | [Nordnet AR2024 release (Inderes)](https://inderes.se/releases/nordnet-publishes-annual-and-sustainability-report-for-2024); [Nordnet Jan-2025 monthly](https://inderes.dk/releases/nordnet-monthly-statistics-january-4) |
| Definition | Management says "new active customers". The formal definition was not captured. | — | — | [call highlights](https://ca.investing.com/news/company-news/nordnet-ab-publ-fra9jl-q2-2026-earnings-call-highlights-record-revenue-and-customer--4745172) |

**Webull, Trade Republic, Trading 212**

| Company | Metric | Value | Period | Note | Source |
|---|---|---|---|---|---|
| Webull | Funded accounts | 5.13 M | Q2-2026 | +8% YoY | [Webull Q2-2026 6-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/0001866364/000121390026091702/ea030257601ex99-1.htm); [Barchart copy](https://www.barchart.com/story/news/3937147/webull-reports-second-quarter-2026-financial-results) |
| Webull | Registered users | 28.2 M | Q2-2026 | +13% YoY | as above |
| Webull | Funded ÷ registered [C] | 18.2% | Q2-2026 | 5.13 ÷ 28.2 | as above |
| Trade Republic | Customers | ~10 M | Dec-2025 | Doubled within a year. >5 M in Germany; >2 M across FR, IT and ES. Not defined. | [Trade Republic press release, Dec-2025 (PDF)](https://assets.traderepublic.com/assets/files/251217_Secondary_PressRelease_DE_DE2.pdf); [Börsen-Zeitung](https://www.boersen-zeitung.de/banken-finanzen/trade-republic-ueberschreitet-marke-von-10-millionen-kunden) |
| Trading 212 UK Ltd | Funded-account growth | +69% | FY2025 | Absolute count not captured. Secondary reporting of a Companies House filing. | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/trading-212-uk-revenues-soar-72-in-2025-to-277m-profit-tops-92m/); [Finance Magnates](https://www.financemagnates.com/forex/trading-212-continues-to-grow-in-the-uk-2025-revenue-jumps-72-profit-doubles/) |

### Inferences
- Ranking by how strict the customer unit is: Robinhood (unique person, 45-day balance-or-transaction test) > eToro (positive balance and at least one trade ever) > Webull "funded accounts" > flatexDEGIRO accounts and Avanza/Nordnet customers (no activity test captured) > Trade Republic "customers" (undefined).
  - For the driver tree: define the base unit as "unique person with balance > 0", and attach an adjustment flag to each peer.
- Webull's 18% funded-to-registered conversion is the only funnel ratio captured. It suggests the registered-but-unfunded pool of a US mobile app is about 4–5x the funded base.
- Robinhood's 2025 growth includes inorganic additions (TradePMR end-clients, Bitstamp). Its organic growth is therefore somewhat below the +7% headline. eToro accelerated in Q2-2026, adding +0.26 M accounts in one quarter.

### Gaps
- None of the companies had a current MAU, "% of customers that traded" or dormant-share figure in the sources found. Robinhood's MAU (still in its 2024 earnings materials) was not captured for 2025–26.
- Formal customer definitions for flatexDEGIRO, Avanza and Nordnet (in each report's APM or glossary section) were not captured.
- Robinhood "Investment Accounts", eToro registered users and Trading 212 absolute funded accounts were not captured.
- Source access: all PDFs and IR pages were blocked for direct fetch in this session, and the search budget was exhausted (see note under the title).

## 2. Client assets: platform assets and AuC, assets per customer, net inflows as % of opening assets, flows vs. market

### Takeaway
Robinhood's annualized net deposits run at 27–35% of opening assets, about 3x the European mass-retail peers (flatexDEGIRO ≈11%, Nordnet ≈9%, Avanza ≈5–7%). Assets per customer differ by an order of magnitude:

| Company | Assets per customer |
|---|---|
| Nordnet / Avanza | SEK 0.53–0.56 M |
| flatexDEGIRO | €29.6k |
| Robinhood | $13.4k |
| Webull | $5.6k |
| eToro | $4.4k |

In Jan–Aug 2026 about 70% of Nordic asset growth came from market performance and about 30% from net flows. For Robinhood in FY2025, net deposits explain about 52% of TPA growth; the rest is markets plus acquired assets.

### Cited Findings

**Robinhood**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Total Platform Assets (TPA) | $384 B | end Aug-2026 | +8% MoM; +26% YoY | [HOOD Aug-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-markets-inc-reports-august-2026-operating-data) |
| TPA | $369 B | end Q2-2026 | +32% YoY | [HOOD Q2-2026](https://www.barchart.com/story/news/3534009/robinhood-reports-second-quarter-2026-results) |
| TPA | $324 B | end FY2025 | +68% YoY. The company attributes the growth to net deposits, acquired assets and higher equity valuations. | [HOOD Q4/FY2025](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-fourth-quarter-and-full-year-2025-results) |
| TPA, end-FY2024 [C] | ≈$193 B | end FY2024 | 324 ÷ 1.68 | as above |
| TPA, end-Q1-2026, implied [C] | ≈$310 B (±$5 B from rounding) | end Q1-2026 | 21.7 × 4 ÷ 0.28 | [HOOD Q2-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results) |
| Net Deposits | $4.0 B (14% annualized growth rate vs July TPA) | Aug-2026 | — | [HOOD Aug-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-markets-inc-reports-august-2026-operating-data) |
| Net Deposits | $21.7 B, a record (28% annualized vs TPA at end-Q1-2026) | Q2-2026 | — | [HOOD Q2-2026](https://www.barchart.com/story/news/3534009/robinhood-reports-second-quarter-2026-results) |
| Net Deposits | $75.7 B (27% of TPA at end-Q2-2025) | TTM to Q2-2026 | — | as above |
| Net Deposits | $68.1 B (35% of TPA at end-Q4-2024) | FY2025 | — | [HOOD Q4/FY2025](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-fourth-quarter-and-full-year-2025-results); [10-K](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000023/hood-20251231.htm) |
| **Definition: TPA** | Sum of the fair value of all equities, options, cryptocurrency, futures (including options on futures and swaps, and event contracts) and cash held by users in their accounts, net of receivables from users (formerly "Assets Under Custody"). Also includes assets managed by RIAs on TradePMR's platform that Robinhood does not custody. Trade-date basis. | FY2025 | Net of margin debt; includes non-custodied RIA assets. | [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000023/hood-20251231.htm) |
| **Definition: net-deposit growth rate** | Net deposits for the period (annualized for months and quarters) ÷ TPA at the end of the prior period | — | — | [HOOD Q2-2026](https://www.barchart.com/story/news/3534009/robinhood-reports-second-quarter-2026-results) |
| TPA per Funded Customer [C] | $12.0k / $13.0k / $13.4k | end FY2025 / Q2-2026 / Aug-2026 | 324 ÷ 27.0; 369 ÷ 28.4; 384 ÷ 28.6 | as above |
| Net deposits per average Funded Customer [C] | ≈$2,610 | FY2025 | 68.1 B ÷ avg(25.2, 27.0) M = 68.1 ÷ 26.1 | as above |
| Flows vs. market [C] | ΔTPA ≈ $131 B = net deposits $68.1 B (52%) + markets, acquisitions and other ≈ $63 B (48%) | FY2025 | 324 − 193 | as above |
| Flows vs. market [C] | ΔTPA ≈ $59 B = net deposits $21.7 B (37%) + markets and other ≈ $37 B (63%) | Q2-2026 | 369 − 310 | as above |

**eToro**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Assets Under Administration (AUA) | $19 B (record) | end Q2-2026 | +10% YoY | [Yahoo Finance Q2-2026 call highlights](https://finance.yahoo.com/markets/stocks/articles/etoro-group-ltd-etor-q2-210139045.html); [Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/08/18/etoro-etor-q2-2026-earnings-call-transcript/) |
| AUA | $17 B | end Q1-2026 | +15% YoY | [Finance Magnates Q1-2026](https://www.financemagnates.com/fintech/etoro-q1-net-income-climbs-37-to-82-million-on-commodities-surge/) |
| AUA | $18.5 B | end FY2025 | +11% vs $16.6 B at end-2024 | [eToro Q4/FY2025](https://www.fintechfutures.com/press-releases/etoro-reports-fourth-quarter-and-full-year-2025-results) |
| AUA per Funded Account [C] | $4,856 / $4,229 / $4,439 | FY2025 / Q1-2026 / Q2-2026 | 18.5 ÷ 3.81; 17 ÷ 4.02; 19 ÷ 4.28 | as above |

**flatexDEGIRO**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Assets under Custody (AuC) | €108.3 B = securities €101.8 B + customer deposits €6.5 B | end Q2-2026 | June-2025: €83.5 B (securities €78.4 B; cash €5.1 B). Securities exceeded €100 B for the first time. | [FTK Q2-2026 (PDF)](https://s206.q4cdn.com/770226284/files/doc_news/2026/07/260722-flatexDEGIRO_Press-Release_Q2-2026-Results.pdf); [€100 bn SuC release (PDF)](https://s206.q4cdn.com/770226284/files/doc_news/2026/07/01/260701-flatexDEGIRO_press-release_100bn-SuC.pdf) |
| AuC | €94.5 B = securities €88.1 B + cash €6.4 B | end Q1-2026 | — | [FTK Q1-2026](https://www.finanzen.net/nachricht/aktien/eqs-news-flatexdegiro-starts-2026-with-a-record-quarter-15627664) |
| AuC | €95.5 B | end FY2025 | +34% YoY | [FTK FY2025](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| AuC, end-FY2024 [C] | ≈€71.3 B | end FY2024 | 95.5 ÷ 1.34 | as above |
| Net Cash Inflows | €5.2 B | H1-2026 | H1-2025: €5.6 B | [FTK Q2-2026](https://www.webdisclosure.com/press-release/online-broker-flatexdegiro-further-expands-record-results-and-increases-net-income-by-55-percent-pIHtqXjeilQ) |
| Net Cash Inflows | €8.1 B | FY2025 | FY2024: €6.6 B | [FTK FY2025](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| Net-inflow rate [C] | 11.4% / 10.9% annualized | FY2025 / H1-2026 | 8.1 ÷ 71.3; (5.2 × 2) ÷ 95.5 | as above |
| Flows vs. market [C] | ΔAuC €24.2 B = flows €8.1 B (33%) + market and other €16.1 B (67%) | FY2025 | — | as above |
| Flows vs. market [C] | ΔAuC €12.8 B = flows €5.2 B (41%) + market and other €7.6 B (59%) | H1-2026 | — | as above |
| AuC per account [C] | €27.3k / €29.6k | end FY2025 / end Q2-2026 | 95.5 ÷ 3.5; 108.3 ÷ 3.66 | as above |

**Avanza**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Savings capital | SEK 1,263.5 B | end Aug-2026 | July: SEK 1,216.3 B; +22% YoY | [Avanza Aug-2026 monthly (PDF)](https://investors.avanza.se/files/mfn/9acfa038-d7f2-4bfd-b63b-13515552f639/august-monthly-statistics.pdf) |
| Savings capital | SEK 1,208.3 B (record) | end Q2-2026 | — | [Avanza Q2-2026 report (PDF)](https://storage.mfn.se/bec572f7-2a0c-4659-a0e0-c6b1214b997f/avanza-bank-holding-ab-publ-interim-report-january-june-2026.pdf) |
| Savings capital | SEK 1,079.2 B | end FY2025 | 8.3% share of the Swedish savings market | [Avanza FY2025 (Inderes)](https://www.inderes.fi/en/releases/avanza-bank-holding-ab-publ-preliminary-financial-statement-2025) |
| Net inflow | SEK 7.35 B in August; SEK 51.3 B YTD | Aug-2026 / Jan–Aug 2026 | Share of Swedish savings market 8.7%; share of net inflow 9.0% | [Avanza Aug-2026 monthly (Inderes)](https://www.inderes.se/en/releases/august-monthly-statistics-7) |
| Net inflow | ≈SEK 19 B, of which ≈SEK 17 B into mutual funds (a record) | Q2-2026 | — | [Investing.com Q2-2026 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-avanza-bank-posts-record-q2-2026-profit-shares-rise-93CH-4789991) |
| Net inflow | SEK 54 B | FY2025 | — | [Avanza FY2025 (Inderes)](https://www.inderes.fi/en/releases/avanza-bank-holding-ab-publ-preliminary-financial-statement-2025) |
| Net-inflow rate [C] | 5.2% of average savings capital | FY2025 | 54 ÷ 1,045. The average of SEK 1,045 B is implied by the 0.43% income ratio: 4,495 ÷ 0.0043. | as above |
| Net-inflow rate [C] | 7.1% of opening savings capital, annualized | Jan–Aug 2026 | 51.3 × 12/8 ÷ 1,079.2 | as above |
| Flows vs. market [C] | Δ savings capital SEK 184.3 B = net inflow 51.3 B (28%) + market ≈133 B (72%) | Jan–Aug 2026 | — | as above |
| Savings capital per customer [C] | SEK 481k / 517k / 533k | end FY2025 / Q2-2026 / Aug-2026 | 1,079,200 ÷ 2,242,700; 1,208,300 ÷ 2,338,300; 1,263,500 ÷ 2,371,900 (SEK M ÷ customers) | as above |

**Nordnet**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Savings capital | SEK 1,436 B (lending SEK 32.0 B) | end Aug-2026 | — | [Nordnet Aug-2026 monthly (MFN)](https://mfn.se/all/a/nordnet/nordnet-monthly-statistics-august-f963d7ba) |
| Savings capital | SEK 1,374 B (vs 1,064 B; +29%) | end Q2-2026 | — | [Nordnet Q2-2026 report (PDF)](https://nordnetab.com/wp-content/uploads/2026/07/2Q26-report.pdf) |
| Savings capital | SEK 1,183 B (+15%) | end FY2025 | — | [Nordnet AR2025 release](https://news.cision.com/nordnet/r/nordnet-publishes-annual-and-sustainability-report-for-2025,c4320623) |
| Net savings | SEK 8.8 B in August; SEK 73.2 B YTD | Aug-2026 | — | [Nordnet Aug-2026 monthly (Inderes)](https://www.inderes.dk/en/releases/nordnet-monthly-statistics-august-5) |
| Net savings | SEK 26 B (+78% YoY) | Q2-2026 | — | [Investing.com](https://www.investing.com/news/earnings/nordnet-q2-profit-hits-record-as-trading-boom-customer-inflows-lift-earnings-4797398) |
| Net-savings rate [C] | 9.3% of opening savings capital, annualized | Jan–Aug 2026 | 73.2 × 12/8 ÷ 1,183 | as above |
| Flows vs. market [C] | Δ savings capital SEK 253 B = net savings 73.2 B (29%) + market ≈180 B (71%) | Jan–Aug 2026 | — | as above |
| Savings capital per customer [C] | SEK 503k / ≈550k / 564k | FY2025 / Q2-2026 / Aug-2026 | 1,183 ÷ 2.35; 1,374 ÷ ~2.5; 1,436 ÷ 2.544 (SEK B ÷ M) | as above |

**Webull and Trade Republic**

| Company | Metric | Value | Period | Note | Source |
|---|---|---|---|---|---|
| Webull | Customer assets | $28.5 B | Q2-2026 | +79% YoY | [Webull Q2-2026 (Barchart)](https://www.barchart.com/story/news/3937147/webull-reports-second-quarter-2026-financial-results) |
| Webull | Assets per funded account [C] | $5,556 | Q2-2026 | 28.5 ÷ 5.13 | as above |
| Trade Republic | Assets under administration | ≈€150 B | Dec-2025 | Company-announced milestone; no audited definition | [Trade Republic release (PDF)](https://assets.traderepublic.com/assets/files/251217_Secondary_PressRelease_DE_DE2.pdf) |
| Trade Republic | AUA per customer [C] | ≈€15k | Dec-2025 | 150 B ÷ 10 M | as above |

### Inferences
- Net-deposit intensity is the largest structural difference. Plausible flow assumptions for the model:
  - US mobile-first platform in a strong cycle (Robinhood 2025–26): 25–35% of opening assets per year.
  - Mature European neobroker: 7–11% per year.
- Nordic and flatexDEGIRO customers hold 2–4x more assets than Robinhood's. Their revenue per unit of assets (bps) is structurally lower, but ARPU ends up in a similar range (see §3).
- 59–72% of 2026 asset growth at the Nordics and flatexDEGIRO came from market performance. Model the asset node as opening assets × (1 + flow rate + market return) rather than a single growth rate.
- eToro has the lowest assets per account (≈$4.4k), consistent with a lower-balance user base oriented to trading, CFDs and crypto.

### Gaps
- Not captured: eToro net inflows; Webull net deposits (the search summary's "+7%" was ambiguous); Robinhood TPA split by asset class; company-reported flow-vs-market bridges for the Nordics.
- Definitional comparability of flows was not verified. flatexDEGIRO's "Net Cash Inflows" may exclude securities transfers. Robinhood's Net Deposits include asset transfers and promotions. Whether Avanza and Nordnet include security transfers was not confirmed.

## 3. Revenue: totals, mix, ARPU, revenue ÷ average client assets (bps)

### Takeaway
The peers fall into two monetization archetypes:

| Archetype | Company | Revenue ÷ assets | Mix note |
|---|---|---|---|
| Activity-monetizers | Robinhood | 154–173 bps | ~59% transaction revenue (options, crypto and, from 2026, event contracts) |
| | Webull | ≥279 bps | 74% trading |
| | eToro | ≈495–580 bps (net contribution basis) | ≈67% trading contribution |
| Asset-gatherers | flatexDEGIRO | ≈66–67 bps | — |
| | Avanza | 43–47 bps | — |
| | Nordnet | ≈48–55 bps | — |

ARPU converges far more than bps does: Robinhood $171–187, eToro $221–264 (net contribution), flatexDEGIRO €170–184, Avanza SEK 2.1–2.3k, Nordnet ≈SEK 2.65k.

### Cited Findings

**Robinhood**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Total net revenues | $1.31 B (+32% YoY), a record | Q2-2026 | — | [HOOD Q2-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results); [Barchart copy](https://www.barchart.com/story/news/3534009/robinhood-reports-second-quarter-2026-results) |
| Transaction-based revenues | $776 M (+44%) | Q2-2026 | Options $342 M (+29%); event contracts $156 M (>10x, from ≈$10 M in Q2-2025); equities $129 M (+95%); crypto $100 M (−38%) | [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/robinhood-q2-2026-earnings-beat-132303262.html); [The Block](https://www.theblock.co/news/business/2026-07-29-robinhoods-prediction-markets-top-crypto-and-equities-revenue-in-q2-410102) |
| Other transaction-based [C] | $49 M | Q2-2026 | 776 − 342 − 156 − 129 − 100 | as above |
| Net interest revenues | $389 M (+9%) | Q2-2026 | Driven by growth in interest-earning assets | [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/robinhood-q2-2026-earnings-beat-132303262.html) |
| Other revenues | $143 M (+54%) | Q2-2026 | Gold subscriptions plus Trump Accounts service revenue | as above |
| Mix [C] | Transaction 59.3% (options 26.1%, event contracts 11.9%, equities 9.9%, crypto 7.6%, other 3.7%); NII 29.7%; other 10.9% | Q2-2026 | Each line ÷ $1,308 M (sum of components) | as above |
| ARPU | $187 (+24% YoY), annualized | Q2-2026 | — | [HOOD Q2-2026](https://www.barchart.com/story/news/3534009/robinhood-reports-second-quarter-2026-results) |
| Total net revenues | $4,473 M (+51.6%); Q4-2025: $1.28 B (+27%) | FY2025 | — | [HOOD FY2025 (Barchart)](https://www.barchart.com/story/news/140750/robinhood-reports-fourth-quarter-and-full-year-2025-results); [10-K](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000023/hood-20251231.htm) |
| Transaction-based revenues | $2,628 M (+59.6%) | FY2025 | Options $1,123 M (+48%); crypto $901 M (+44%); equities $302 M (+71%); other $302 M (+260%) | as above |
| Net interest revenues | $1,514 M (+36.5%) | FY2025 | — | as above |
| Other revenues | $331 M (+69.7%) | FY2025 | — | as above |
| Mix [C] | Transaction 58.8% (options 25.1%, crypto 20.1%, equities 6.8%, other 6.8%); NII 33.8%; other 7.4% | FY2025 | — | as above |
| FY2024 back-solved [C] | Revenue ≈$2,951 M; transaction ≈$1,647 M; NII ≈$1,109 M; other ≈$195 M | FY2024 | FY2025 value ÷ (1 + reported growth) | as above |
| ARPU | $171 (FY2025) vs $122 (FY2024), +40% | FY2025 | — | [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000023/hood-20251231.htm) (via search summary) |
| ARPU definition check [C] | 4,473 ÷ avg(25.2, 27.0) = $171.4, which matches the reported $171 | FY2025 | So ARPU = net revenue ÷ average of opening and closing Funded Customers, annualized for quarters. The verbatim definition was not captured. | as above |
| Revenue ÷ average TPA [C] | ≈173 bps | FY2025 | 4,473 ÷ avg(193, 324) = 4,473 ÷ 258.5 B | as above |
| Revenue ÷ average TPA [C] | ≈154 bps annualized (±2 bps) | Q2-2026 | (1,308 × 4) ÷ avg(310, 369) | as above |

**eToro** (reported net contribution, "NC")

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Net Contribution | $229 M (+9% YoY) | Q2-2026 | Capital-markets net trading contribution $142 M (+25%); crypto net trading contribution $11 M (down YoY); NII $49 M (+7%) | [Yahoo Finance call highlights](https://finance.yahoo.com/markets/stocks/articles/etoro-group-ltd-etor-q2-210139045.html); [Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/08/18/etoro-etor-q2-2026-earnings-call-transcript/); [eToro Q2-2026](https://investors.etoro.com/news-releases/news-release-details/etoro-reports-second-quarter-2026-results) |
| Other NC [C] | $27 M | Q2-2026 | 229 − 142 − 11 − 49 | as above |
| Mix [C] | Capital markets 62.0%; crypto 4.8%; NII 21.4%; other 11.8% | Q2-2026 | — | as above |
| Net Contribution | $258 M (+19% YoY), driven by commodities trading | Q1-2026 | — | [Finance Magnates](https://www.financemagnates.com/fintech/etoro-q1-net-income-climbs-37-to-82-million-on-commodities-surge/); [GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/12/3292651/0/en/eToro-Reports-First-Quarter-2026-Results.html) |
| Net Contribution | $868 M (+10% vs $788 M in 2024); Q4-2025: $227 M | FY2025 | — | [eToro Q4/FY2025](https://www.etoro.com/en-us/news-and-analysis/latest-news/press-release/etoro-reports-fourth-quarter-and-full-year-2025-results) |
| **Definition: Net Contribution** | Total revenue and income, less cost of revenue from cryptoassets and margin interest expense | — | eToro's GAAP revenue books crypto sales gross, so NC is the comparable "net revenue". | [eToro prospectus](https://www.stifel.com/prospectusfiles/PD_7111.pdf) |
| NC per average Funded Account [C] | $238 / $264 / $221 | FY2025 / Q1-2026 annualized / Q2-2026 annualized | 868 ÷ avg(3.48, 3.81); 1,032 ÷ avg(3.81, 4.02); 916 ÷ avg(4.02, 4.28) | as above |
| NC ÷ average AUA [C] | ≈495 / ≈581 / ≈509 bps | FY2025 / Q1-2026 / Q2-2026 | 868 ÷ 17.55; 1,032 ÷ 17.75; 916 ÷ 18.0 (USD B) | as above |

**flatexDEGIRO**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Revenues | €166.5 M (+26% YoY) | Q2-2026 | — | [Investing.com Q2-2026 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-flatexdegiro-lifts-outlook-after-strong-q2-2026-93CH-4807923); [Quartr](https://quartr.com/events/flatexdegiro-ftk-q2-2026_3sEyeTNy) |
| Interest income | €53 M (+23%) | Q2-2026 | — | as above |
| Commission income [C] | ≈€101.6 M (61.0% of revenues) | Q2-2026 | 21.9 M transactions × €4.64 | as above |
| Other revenues [C] | ≈€11.9 M (7.1%); interest income = 31.8% | Q2-2026 | 166.5 − 101.6 − 53 | as above |
| Revenues | €560 M (+17%), at the top end of upgraded guidance | FY2025 | — | [FTK FY2025](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| Commission income | €369 M (+31%) = 65.9% of revenues [C] | FY2025 | — | as above |
| FY2024 back-solved [C] | Revenues ≈€479 M; commission income ≈€282 M | FY2024 | 560 ÷ 1.17; 369 ÷ 1.31 | as above |
| **Conflict** | techleap.nl reports "€633 M revenue" for FY2025 | FY2025 | Contradicts the company's €560 M; disregard. | [techleap.nl](https://finder.techleap.nl/news/feed/flatexdegiro-hits-633m-revenue-with-44-profit-surge-and-3-5m-customers) |
| Revenue per average account [C] | €170 / €184 | FY2025 / Q2-2026 annualized | 560 ÷ avg(3.1, 3.5); 666 ÷ avg(3.58, 3.66) | as above |
| Revenue ÷ average AuC [C] | ≈67 / ≈66 bps | FY2025 / Q2-2026 annualized | 560 ÷ avg(71.3, 95.5); 666 ÷ avg(94.5, 108.3) | as above |

**Avanza**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Operating income | SEK 1,334 M (+26% YoY; +6% QoQ) | Q2-2026 | Growth came from currency-related income, NII, brokerage and fund commissions. | [Avanza Q2-2026 (Inderes)](https://www.inderes.se/en/releases/avanza-bank-holding-ab-publ-interim-report-january-june-2026); [Avanza Q2-2026 press page](https://investors.avanza.se/en/media/press/2026/avanza-bank-holding-ab-publ-interim-report-januaryjune-2026/) |
| Income to savings capital | 0.47% | Q2-2026 | — | [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-avanza-bank-posts-record-q2-2026-profit-shares-rise-93CH-4789991) |
| Operating income | SEK 4,495 M (+15% vs 3,900 M); Q4-2025: 1,139 M (+7%) | FY2025 | — | [Avanza FY2025 (Inderes)](https://www.inderes.fi/en/releases/avanza-bank-holding-ab-publ-preliminary-financial-statement-2025) |
| Income to savings capital | 0.43% | FY2025 | — | [Avanza FY2025 (Inderes)](https://www.inderes.dk/releases/avanza-bank-holding-ab-publ-preliminary-financial-statement-2025) |
| Income mix | Net brokerage income SEK 1,201 M (27%); NII SEK 1,577 M (35%) | FY2025 (inferred: the shares tie to the FY2025 total of 4,495) | — | [Avanza company presentation, Mar-2026 (PDF)](https://investors.avanza.se/files/Presentationer/2026-03_04_bolagspresentation_eng.pdf) |
| Fund commissions, currency-related and other [C] | SEK 1,717 M (38%) | FY2025 | 4,495 − 1,201 − 1,577 | as above |
| Ratio-basis check [C] | 0.47% implies average savings capital of ≈SEK 1,135 B. Costs of 406 × 4 ÷ 1,135 B = 14.3 bps, matching the reported 14 bps. | Q2-2026 | So the ratios are quarterly figures, annualized, on average savings capital. | as above |
| Revenue per average customer [C] | SEK 2,084 / SEK 2,302 | FY2025 / Q2-2026 annualized | 4,495 M ÷ avg(2,071,700, 2,242,700); 5,336 M ÷ avg(2,298,000, 2,338,300) | as above |

**Nordnet**

| Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|
| Operating income | SEK 1,634 M (vs 1,293 M; +26% [C]) | Q2-2026 | — | [Nordnet Q2-2026 report (PDF)](https://nordnetab.com/wp-content/uploads/2026/07/2Q26-report.pdf); [Cision PDF](https://mb.cision.com/Main/116/4375517/4195075.pdf) |
| Net transaction-related income | SEK 740 M (+37%) | Q2-2026 | Record cross-border trading | [Investing.com](https://www.investing.com/news/earnings/nordnet-q2-profit-hits-record-as-trading-boom-customer-inflows-lift-earnings-4797398) |
| Fund-related income | SEK 198 M | Q2-2026 | In-house funds passed SEK 100 B of savings capital | as above |
| Net interest income | SEK 675 M (+12.3%) | Q2-2026 | — | as above |
| Other [C] | SEK 21 M | Q2-2026 | 1,634 − 740 − 198 − 675 | as above |
| Mix [C] | Transaction 45.3%; fund 12.1%; NII 41.3%; other 1.3% | Q2-2026 | — | as above |
| Revenue ÷ savings capital [C] | 47.6–55.2 bps (bounds) | Q2-2026 annualized | 6,536 ÷ 1,374 B (end-Q2, lower bound); ÷ 1,183 B (end-2025, upper bound). End-Q1-2026 capital was not captured. | as above |
| Revenue per customer [C] | ≈SEK 2,650 | Q2-2026 annualized | 6,536 M ÷ ~2.46 M average customers (approximate) | as above |
| FY2025 context | Adjusted operating profit SEK 3,748 M (record); NII fell on lower rates. Q4-2025: adjusted operating income SEK 1,391 M; adjusted operating profit SEK 966 M (period label inferred as Q4). | FY2025 / Q4-2025 | — | [Nordnet AR2025 release](https://news.cision.com/nordnet/r/nordnet-publishes-annual-and-sustainability-report-for-2025,c4320623); [Q4-2025 release](https://news.cision.com/nordnet/r/nordnet-ab-publishes-its-fourth-quarter-2025-interim-report,c4298500); [4Q25 presentation](https://nordnetab.com/wp-content/uploads/2026/01/Presentation-4Q25.pdf) |

**Webull, Trading 212, Trade Republic**

| Company | Metric | Value | Period | Note | Source |
|---|---|---|---|---|---|
| Webull | Total revenues | $198.8 M (+51%) | Q2-2026 | — | [Webull 6-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/0001866364/000121390026091702/ea030257601ex99-1.htm); [Barchart](https://www.barchart.com/story/news/3937147/webull-reports-second-quarter-2026-financial-results) |
| Webull | Trading-related revenue | $147.7 M (+66%) = 74.3% [C] | Q2-2026 | Non-trading revenue (interest and other) [C] = $51.1 M (25.7%) | as above; [Finance Magnates datalab](https://datalab.financemagnates.com/market-insights/webull-s-51-revenue-jump-came-from-more-activity-not-many-more-accounts) |
| Webull | Revenue per funded account [C] | ≈$155 annualized | Q2-2026 | 198.8 × 4 ÷ 5.13 (end-period base) | as above |
| Webull | Revenue ÷ customer assets [C] | ≥279 bps | Q2-2026 | 795 ÷ 28.5 B. End-period assets, so this is a lower bound. | as above |
| Trading 212 UK Ltd | Revenue | £277.6 M (+72%) | FY2025 | Trading ≈£257 M (92.6% [C]); client interest income £20.6 M (7.4% [C]); debit cards £1.68 M. Secondary reporting of a Companies House filing. | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/trading-212-uk-revenues-soar-72-in-2025-to-277m-profit-tops-92m/); [Finance Magnates](https://www.financemagnates.com/forex/trading-212-continues-to-grow-in-the-uk-2025-revenue-jumps-72-profit-doubles/) |
| Trading 212 Group | Revenue | >£194 M; UK entity £161.7 M, of which £150 M from investment brokerage | FY2024 | Secondary source | [Finance Magnates (2024 accounts)](https://www.financemagnates.com/forex/trading-212-uk-doubles-2024-ad-spending-but-profit-keeps-rising); [Wikipedia](https://en.wikipedia.org/wiki/Trading_212) |
| Trade Republic | Revenue | "Umsatz" >€500 M; "Gesamterträge" ≈€340 M including ≈€316 M commission income; net income ≈€35 M | Probably FY2024 | Internally inconsistent secondary report. Do not benchmark without the HGB filing. | [broker-test.at](https://www.broker-test.at/news/trade-republic-knackt-500-millionen-umsatz-marke-so-stark-waechst-europas-shootingstar-der-fintechs/) |

### Inferences
- Within one year, prediction markets (event contracts) became Robinhood's #2 transaction line: 11.9% of Q2-2026 revenue, while crypto fell to 7.6%. The driver tree needs an "event contracts" node: contracts × fee per contract (≈$0.0115, see §4).
- Bps on assets falls as balances build up. Robinhood went from 173 to 154 bps while ARPU rose from $171 to $187. For activity-monetizers, model revenue through ARPU drivers (activity × take rate, plus balances × spread). For Nordic asset-gatherers, bps on assets is a stable driver.
- eToro earns ≈5% of AUA a year, which reflects CFD, crypto and FX-conversion monetization. Per account, however, its NC ($220–264) is close to Robinhood's ARPU. Annual net revenue of $170–260 per customer looks like a mass-retail band, regardless of model.
- Interest-rate cyclicality: NII is 21–41% of revenue across the set.
  - Robinhood's NII grew 36.5% in 2025 but only 9% YoY in Q2-2026, and its NII share fell from 33.8% to 29.7%.
  - Nordnet's NII fell in 2025 on policy-rate cuts, then rose 12.3% YoY in Q2-2026 on volume.
  - flatexDEGIRO's interest income is still +23% YoY.

### Gaps
- Not captured:
  - Avanza Q2-2026 income components (brokerage, fund commissions, currency-related, NII).
  - Nordnet FY2025 full income-statement components and reported income ÷ savings capital.
  - flatexDEGIRO FY2025 interest income.
  - eToro FY2025 NC by asset class.
  - Webull revenue split (options, equities, crypto, interest).
- Robinhood's PFOF/rebate share of transaction revenue is not quantified here.
- Trade Republic audited financials not captured.

## 4. Trading activity: trades per customer, volumes, revenue per trade and take rate, turnover

### Takeaway
Only flatexDEGIRO (trades per account, € per trade), Nordnet (trades per day, SEK per trade) and Robinhood (notional and contract volumes) yielded activity drivers here. European mass-retail customers trade about 23–30 times a year. The take is ≈€4.6 per trade at flatexDEGIRO and ≈SEK 42 at Nordnet. Robinhood's equity notional volume equals about 0.9x TPA every month.

### Cited Findings

| Company | Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|---|
| Robinhood | Equity notional trading volume | $335 B (+1% MoM; +68% YoY) | Aug-2026 | — | [HOOD Aug-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-markets-inc-reports-august-2026-operating-data) |
| Robinhood | Event contracts traded | >13.6 B contracts (>10x YoY) | Q2-2026 | — | [The Block](https://www.theblock.co/post/410102/robinhoods-prediction-markets-top-crypto-and-equities-revenue-in-q2); [Brokerchooser](https://brokerchooser.com/news/prediction-markets-become-robinhoods-second-largest-revenue-driver--0c37bdeb) |
| Robinhood | Revenue per event contract [C] | ≈$0.0115 | Q2-2026 | $156 M ÷ 13.6 B | as above |
| Robinhood | Equity notional ÷ TPA [C] | 0.87x a month (≈10.5x annualized) | Aug-2026 | 335 ÷ 384. Notional counts both buys and sells, and TPA also includes crypto and cash. | as above |
| flatexDEGIRO | Settled transactions | 21.9 M (+22% YoY) | Q2-2026 | — | [Investing.com Q2-2026 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-flatexdegiro-lifts-outlook-after-strong-q2-2026-93CH-4807923) |
| flatexDEGIRO | Settled transactions | 22.7 M (≈+17% YoY) | Q1-2026 | — | [FTK Q1-2026](https://www.finanzen.net/nachricht/aktien/eqs-news-flatexdegiro-starts-2026-with-a-record-quarter-15627664) |
| flatexDEGIRO | Settled transactions | 75 M (2024: 63 M; +19%) | FY2025 | — | [FTK FY2025](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| flatexDEGIRO | Transactions per customer | 23 (2024: 22) | FY2025 | — | as above |
| flatexDEGIRO | Transactions per account [C] | 24.2 / 25.6 annualized | Q2-2026 / Q1-2026 | 21.9 × 4 ÷ 3.62; 22.7 × 4 ÷ 3.54 | as above |
| flatexDEGIRO | Commission per transaction | €4.64 / €4.62 / €4.39 | Q2-2026 / Q1-2026 / Q2-2025 | — | [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-flatexdegiro-lifts-outlook-after-strong-q2-2026-93CH-4807923) |
| flatexDEGIRO | Average commission per transaction | €4.90 (computed check: 369 ÷ 75 = €4.92) | FY2025 | **Basis conflict** with the quarterly series (Q2-2025 = €4.39). 2024 [C] = 282 ÷ 63 = €4.47. Probably a different basis, e.g. the 2026 IFRS 18 re-presentation. Do not mix the series. | [FTK FY2025](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| Nordnet | Trades per day | 298,000 (+15%) | Q2-2026 | — | [Nordnet call highlights](https://ca.investing.com/news/company-news/nordnet-ab-publ-fra9jl-q2-2026-earnings-call-highlights-record-revenue-and-customer--4745172) |
| Nordnet | Income per trade | SEK 41.9 (+37%) | Q2-2026 | Consistent with net transaction-related income ÷ trades [C]: 740 M ÷ (298k × ~59 trading days ≈ 17.6 M) ≈ SEK 42. The trading-day count is my assumption. | as above |
| Nordnet | Trades | 5,325,900 = 253,600 a day | Aug-2026 | — | [Nordnet Aug-2026 monthly](https://www.inderes.dk/en/releases/nordnet-monthly-statistics-august-5) |
| Nordnet | Trades per customer per year [C] | ≈30 / ≈25 | Q2-2026 / Aug-2026 run-rate | 298k × 252 ÷ 2.5 M; 253.6k × 252 ÷ 2.544 M (252 trading days assumed) | as above |

### Inferences
- Benchmarks for European fixed-fee or low-fee mass retail:
  - About 23–30 trades per customer per year.
  - About €4.6 per trade at flatexDEGIRO. Nordnet's SEK 42 is roughly €3.8 at an illustrative ~11 SEK/EUR (my assumption, not sourced).
- flatexDEGIRO's revenue per trade rose ≈6% YoY in Q2-2026 (€4.39 → €4.64), alongside 22% transaction growth. Price/mix and volume both contributed.
- Robinhood's equity turnover of ≈10x TPA per year shows trading intensity relative to balances far above European peers. Treat it as order-of-magnitude only (two-sided notional; mixed asset base).

### Gaps
- Not captured:
  - Robinhood: options contracts traded, crypto notional (app and Bitstamp), and per-unit take rates (options revenue per contract, crypto bps).
  - Webull: DARTs and notional.
  - eToro: trade counts and volumes.
  - Avanza: brokerage-generating notes per day and brokerage per note, which its reports do publish.

## 5. Margin book, uninvested cash, securities lending

### Takeaway
Robinhood's margin book is 5.6% of TPA (Aug-2026), up from ≈4.1% a year earlier, while sweep cash fell from ≈11.3% to 8.1% of TPA. Customer cash is 6.0% of AuC at flatexDEGIRO. Nordnet's total lending is 2.2–2.3% of savings capital, and that includes mortgages. NII makes up 21–41% of revenue at the companies with data.

### Cited Findings

| Company | Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|---|
| Robinhood | Margin balances | $21.5 B (+4% MoM; +72% YoY) | end Aug-2026 | — | [HOOD Aug-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-markets-inc-reports-august-2026-operating-data); [InvestingNews](https://investingnews.com/robinhood-markets-inc-reports-august-2026-operating-data/) |
| Robinhood | Cash sweep balances | $31.2 B (+7% MoM; −9% YoY) | end Aug-2026 | — | as above |
| Robinhood | Cash and deposit balances | $19.6 B (+1% MoM; +37% YoY) | end Aug-2026 | Exact scope not captured | as above |
| Robinhood | Total securities lending revenue | $36 M (−10% MoM; −32% YoY) | Aug-2026 | — | as above |
| Robinhood | Margin ÷ TPA [C] | 5.6% (Aug-2026) vs ≈4.1% (Aug-2025) | — | 21.5 ÷ 384; (21.5 ÷ 1.72) ÷ (384 ÷ 1.26) | as above |
| Robinhood | Sweep ÷ TPA [C] | 8.1% (Aug-2026) vs ≈11.3% (Aug-2025) | — | 31.2 ÷ 384; (31.2 ÷ 0.91) ÷ 304.8 | as above |
| Robinhood | Cash and deposits ÷ TPA [C] | 5.1% | Aug-2026 | 19.6 ÷ 384 | as above |
| Robinhood | Securities-lending run-rate [C] | ≈$108 M a quarter ≈ 28% of Q2-2026 NII, ≈8% of the revenue run-rate | — | 36 × 3 vs 389; 36 × 12 vs 5,232. Mixes periods; indicative only. | as above |
| Robinhood | NII share of revenue [C] | 33.8% (FY2025) → 29.7% (Q2-2026) | — | See §3 | as above |
| eToro | Net interest income | $49 M (+7%) = 21.4% of NC [C] | Q2-2026 | — | [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/etoro-group-ltd-etor-q2-210139045.html) |
| flatexDEGIRO | Customer cash ÷ AuC [C] | 6.0% / 6.8% / 6.1% | Q2-2026 / Q1-2026 / Q2-2025 | 6.5 ÷ 108.3; 6.4 ÷ 94.5; 5.1 ÷ 83.5 | [FTK Q2-2026](https://s206.q4cdn.com/770226284/files/doc_news/2026/07/260722-flatexDEGIRO_Press-Release_Q2-2026-Results.pdf); [FTK Q1-2026](https://www.finanzen.net/nachricht/aktien/eqs-news-flatexdegiro-starts-2026-with-a-record-quarter-15627664) |
| flatexDEGIRO | Interest income ÷ average customer cash [C] | ≈3.3% annualized | Q2-2026 | 53 × 4 ÷ avg(6.4, 6.5). Upper-bound proxy, because interest income also comes from lending and treasury. | as above |
| Avanza | Net interest income | SEK 1,577 M = 35% of operating income | FY2025 | — | [Avanza presentation, Mar-2026](https://investors.avanza.se/files/Presentationer/2026-03_04_bolagspresentation_eng.pdf) |
| Nordnet | Lending | SEK 31.4 B (vs 27.0 B) = 2.3% of savings capital [C] | Q2-2026 | Includes mortgages and margin/securities-backed loans. The unsecured-loan book was sold to Ikano Bank in Oct-2024. | [Investing.com](https://www.investing.com/news/earnings/nordnet-q2-profit-hits-record-as-trading-boom-customer-inflows-lift-earnings-4797398); [Inderes (Ikano)](https://inderes.dk/releases/nordnet-monthly-statistics-january-4) |
| Nordnet | Lending | SEK 32.0 B = 2.2% of savings capital [C] | Aug-2026 | — | [Nordnet Aug-2026 monthly](https://www.inderes.dk/en/releases/nordnet-monthly-statistics-august-5) |
| Nordnet | NII | SEK 675 M (+12.3%) = 41.3% of operating income [C] | Q2-2026 | NII declined in 2025 on lower market rates. | [Investing.com](https://www.investing.com/news/earnings/nordnet-q2-profit-hits-record-as-trading-boom-customer-inflows-lift-earnings-4797398); [Nordnet Q4-2025](https://news.cision.com/nordnet/r/nordnet-ab-publishes-its-fourth-quarter-2025-interim-report,c4298500) |
| Trading 212 UK Ltd | Client interest income | £20.6 M = 7.4% of revenue [C] | FY2025 | — | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/trading-212-uk-revenues-soar-72-in-2025-to-277m-profit-tops-92m/) |

### Inferences
- Robinhood's balance mix is moving from sweep cash to margin: the margin book is up 72% YoY and sweep balances are down 9%. Its NII depends increasingly on margin demand rather than on rates paid on idle cash. This driver is pro-cyclical with markets.
- Ranges for the model's "uninvested cash ÷ client assets" node: 6% (flatexDEGIRO) to 13% (Robinhood sweep plus cash and deposits).
- Ranges for the "margin loans ÷ client assets" node: 2–6%. The low end is Nordnet, whose total lending includes mortgages; the high end is Robinhood.
- Trading 212's low interest share (7%) fits a model that passes most of the interest on uninvested cash to clients. That is an inference; I did not verify Trading 212's interest policy here.

### Gaps
- Share of customers using margin: not found for any company.
- Not captured:
  - Avanza and Nordnet customer deposits and cash share of savings capital; Avanza lending.
  - flatexDEGIRO margin-loan ("flatex flex") book.
  - eToro interest-bearing balances.
  - Robinhood quarter-end margin and sweep balances for Q2-2026.
  - Securities-lending revenue for anyone except Robinhood.

## 6. Subscriptions: paid subscribers, penetration, price, revenue contribution

### Takeaway
Of the peers in this set, I found subscription data only for Robinhood. Robinhood Gold had 4.8 M subscribers in Q2-2026, about 17% penetration, and roughly 40% of new funded customers sign up. Gold subscription revenue was about $50 M a quarter in Q4-2025, about 4% of revenue (≈$48 a year per subscriber [C]). Most of Gold's economic value likely comes through interest and margin on the subscribers' balances, not the fee itself; that is an inference.

### Cited Findings

| Company | Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|---|
| Robinhood | Gold Subscribers | 4.8 M (+1.4 M / +39% YoY; +0.5 M QoQ) | end Q2-2026 | Adoption ≈17%. About 40% of new Funded Customers signed up for Gold in Q2. | [Subscription Insider](https://www.subscriptioninsider.com/blog/robinhood-gold-subscribers-grow-39-to-record-4-8-million-news); [HOOD Q2-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results) |
| Robinhood | Gold Subscribers | 4.2 M (+1.5 M / +58%) | end FY2025 | — | [HOOD Q4/FY2025](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-fourth-quarter-and-full-year-2025-results) |
| Robinhood | Gold subscription revenue | $50 M (+56% YoY) | Q4-2025 | — | as above |
| Robinhood | Penetration [C] | 15.6% → 16.9% | end FY2025 → Q2-2026 | 4.2 ÷ 27.0; 4.8 ÷ 28.4 | as above |
| Robinhood | Gold revenue share and per subscriber [C] | 3.9% of Q4-2025 net revenue; ≈$48 a year per subscriber | Q4-2025 | 50 ÷ 1,280; 50 × 4 ÷ 4.2. The end-period base slightly understates the per-subscriber figure. | as above |
| Robinhood | Other revenues (includes Gold) | $143 M (+54%) | Q2-2026 | Also includes Trump Accounts service revenue; Gold not shown separately in the sources captured. | [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/robinhood-q2-2026-earnings-beat-132303262.html) |

### Inferences
- New customers attach to Gold at about 40% versus about 17% for the existing base, so penetration should keep rising.
- For the model, set two Robinhood-like defaults:
  - Subscription penetration grows about 1.3–1.5 pp per year (15.6% at FY2025 to 16.9% at Q2-2026).
  - Fee ≈$48–50 per subscriber per year.
- Treat Gold mainly as a lever for deposits and NII. The Gold fee is only about 4% of revenue.

### Gaps
- Gold list price (monthly or annual), subscriber churn, Gold revenue for Q2-2026, and the ARPU uplift of Gold versus non-Gold customers were not captured.
- No paid-subscription data was captured for eToro (its "Club" appears to be an equity-tiered status programme, not verified here), flatexDEGIRO, Avanza, Nordnet or Webull.

## 7. Retention and churn: customer churn, closures, cohort retention, asset retention

### Takeaway
I captured no explicitly disclosed churn or cohort-retention figure for any company. The only quantitative proxy is my computed estimate for flatexDEGIRO: implied account attrition of about 1–2% of opening accounts in FY2025, which is sensitive to rounding. Asset retention can only be proxied through net-inflow rates, which are positive everywhere: Robinhood 27–35%, flatexDEGIRO ≈11%, Nordnet ≈9%, Avanza ≈5–7%.

### Cited Findings

| Company | Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|---|
| flatexDEGIRO | Implied account attrition [C] | ≈43k ≈ 1.4% of opening accounts (plausible range ≈1–2%) | FY2025 | 446k new accounts − net growth (13% × 3.1 M ≈ 403k). Highly sensitive to rounding of 3.1 M and 3.5 M. | [FTK FY2025](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| Robinhood | Churn KPI | None captured | — | The 45-day lookback drops zero-balance inactive users from Funded Customers, so reported growth (+1.8–1.9 M a year) is already net of churn. | [SEC CORRESP 2024](https://www.sec.gov/Archives/edgar/data/1783879/000178387924000187/filename1.htm) |
| Avanza | Customer adds | Reported net ("40,300 new customers were added (net)") | Q2-2026 | Gross adds and churn cannot be inferred. | [Avanza Q2-2026 (Inderes)](https://www.inderes.se/en/releases/avanza-bank-holding-ab-publ-interim-report-january-june-2026) |
| Nordnet | Customer adds | "New customers": 73,600 in Q2-2026; 23,700 in Aug-2026; YoY growth 12.3% | 2026 | Whether "new customers" is a gross figure is not confirmed, so churn cannot be inferred. Implied customers at Aug-2025 [C] = 2,544,000 ÷ 1.123 ≈ 2.265 M. | [Nordnet Aug-2026 monthly](https://www.inderes.dk/en/releases/nordnet-monthly-statistics-august-5) |
| All | Asset-retention proxy: net inflow ÷ opening assets, annualized [C] | Robinhood 27–35%; FTK ≈11%; Nordnet ≈9%; Avanza ≈5–7% | 2025–26 | See §2 | See §2 |

### Inferences
- For mass-retail models, structural customer churn at mature European brokers appears low. flatexDEGIRO implies about 1–2% a year in accounts, and the Nordics report double-digit net growth.
- Robinhood's definition embeds churn in the net figure. A driver tree needs separate "gross adds" and "attrition" nodes, which have to be estimated, not benchmarked, for Robinhood and eToro.

### Gaps
- Not captured: eToro F-1 cohort charts (net contribution or retention by cohort); Nordnet and Avanza churn (the brief expected these disclosures, but none was found in the material captured); account closures and escheatment at Robinhood.
- Gold subscriber retention: not found.

## 8. Acquisition: marketing spend, new funded accounts, CAC, payback, referral costs

### Takeaway
Paid-acquisition intensity varies about 2x:

| Company | Marketing intensity |
|---|---|
| Robinhood | ≈9% of net revenue ($399 M in 2025; about +$100 M planned for 2026) |
| eToro | 20% of net contribution in Q4-2025, guided up to 25% in 2026 |
| Trading 212 UK | ≈19% of revenue (FY2025) |

Upper-bound CAC proxies (marketing ÷ net new funded customers): Robinhood ≈$222 (FY2025) and eToro ≈$575 (Q4-2025). Simple revenue paybacks are about 1.3 and 2.4 years.

### Cited Findings

| Company | Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|---|
| Robinhood | Marketing expense | $399 M vs $272 M in 2024 (+47%) | FY2025 | Management plans about +$100 M of marketing in 2026 (≈$500 M [C]). | [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000023/hood-20251231.htm) (via search summary; verify the line item) |
| Robinhood | Marketing ÷ revenue [C] | 8.9% (FY2025); 9.2% (FY2024) | — | 399 ÷ 4,473; 272 ÷ 2,951 | as above |
| Robinhood | Marketing per net new Funded Customer [C] | ≈$222 | FY2025 | 399 ÷ 1.8 M. An upper bound for true CAC, because gross adds are not disclosed. | as above |
| Robinhood | Payback [C] | ≈1.3 years on revenue; ≈2.3 years on adj.-EBITDA margin | FY2025 | 222 ÷ 171; 222 ÷ (171 × 56.3%) | as above |
| Robinhood | Q2-2026 opex driver | Opex +33% YoY to $734 M, driven by "marketing and growth investments", a one-off restructuring charge (June-2026 reduction in force), Trump Accounts and Rothera | Q2-2026 | — | [Pulse2 (release copy)](https://pulse2.com/robinhood-reports-revenues-up-32-to-record-1-31-billion-for-q2-2026) |
| eToro | Marketing expense | $147 M (+27% YoY) | FY2024 | — | [eToro FY2025 20-F](https://www.sec.gov/Archives/edgar/data/0001493318/000121390026022034/ea0278371-20f_etoro.htm) (via search summary) |
| eToro | Adjusted sales and marketing | $46 M = 20% of NC; plan to raise gradually to up to 25% of NC in 2026 | Q4-2025 | — | [AOL / Motley Fool Q4-2025 transcript](https://www.aol.com/finance/etoro-etor-q4-2025-earnings-174942622.html) |
| eToro | Marketing per net new Funded Account [C] | ≈$575 | Q4-2025 | 46 ÷ (3.81 − 3.73 M). Upper bound. | as above |
| eToro | Payback [C] | ≈2.4 years of NC | — | 575 ÷ 238 | as above |
| flatexDEGIRO | New customer accounts | 446k | FY2025 | Marketing spend not captured | [FTK FY2025](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| Avanza | International expansion cost | SEK 3 M expensed in Q2-2026; ≈SEK 50 M expected in the 2026 cost base. Swedish cost growth guided at ≈9%. | 2026 | — | [Avanza Q2-2026 (Inderes)](https://www.inderes.se/en/releases/avanza-bank-holding-ab-publ-interim-report-january-june-2026) |
| Trading 212 UK Ltd | Advertising and marketing | £51.5 M = 18.6% of revenue [C] | FY2025 | Staff grew from 53 to 122 | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/trading-212-uk-revenues-soar-72-in-2025-to-277m-profit-tops-92m/) |
| Trading 212 Group | Advertising and marketing | >£65 M; staff costs £27.7 M; 422 employees | FY2024 | Headline: "UK doubles 2024 ad spending" | [Finance Magnates](https://www.financemagnates.com/forex/trading-212-uk-doubles-2024-ad-spending-but-profit-keeps-rising) |

### Inferences
- Plausible defaults for a mass-retail acquisition engine:
  - Marketing at 9–25% of net revenue.
  - Blended CAC of a few hundred dollars per funded customer, with payback of 1–3 years of revenue.
- Robinhood's lower CAC proxy is consistent with brand, referral effects and Gold-led offers. Those drivers are not broken out in the material captured.
- eToro and Trading 212 sit at the high end (≈19–25%), consistent with competitive European and multi-country acquisition.

### Gaps
- Not captured: gross new funded customers (Robinhood, eToro), referral or free-stock incentive costs, and marketing spend for flatexDEGIRO, Avanza, Nordnet and Webull.
- No company-disclosed CAC or LTV figure was found.

## 9. Efficiency: cost/income, cost per customer, adjusted EBITDA and pretax margins

### Takeaway
The Nordics set the efficiency frontier: cost/income of 27–31% and operating margins of 69–73%. flatexDEGIRO earns about 48–51% margins. Robinhood's GAAP operating margin is about 47% (adjusted EBITDA about 56%). eToro's adjusted EBITDA is about 37% of net contribution, Webull's adjusted operating margin about 31%, and Trading 212 UK's net margin about 33%. Annual cost per customer clusters around €60–110 equivalent, except for eToro, where it was not computed per account.

### Cited Findings

| Company | Metric | Value | Period | Definition / note | Source |
|---|---|---|---|---|---|
| Robinhood | Total operating expenses | $2,379 M (+25.4%) | FY2025 | Cost/income [C] 53.2%; GAAP operating margin [C] 46.8% | [HOOD FY2025 (Barchart)](https://www.barchart.com/story/news/140750/robinhood-reports-fourth-quarter-and-full-year-2025-results) |
| Robinhood | Adjusted EBITDA | $2.52 B (+76%) | FY2025 | Margin [C] 56.3% | as above |
| Robinhood | Total operating expenses | $734 M (+33%) | Q2-2026 | Cost/income [C] 56.1% | [Pulse2](https://pulse2.com/robinhood-reports-revenues-up-32-to-record-1-31-billion-for-q2-2026) |
| Robinhood | Adjusted operating expenses + SBC | $641 M (+23%) | Q2-2026 | ÷ revenue [C] 49.0% | as above |
| Robinhood | Adjusted EBITDA | $741 M (+35%) | Q2-2026 | Margin [C] 56.7% | as above |
| Robinhood | Diluted EPS | $0.62 (+48%) | Q2-2026 | — | [HOOD Q2-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results) |
| Robinhood | Opex per average Funded Customer [C] | $91 / $105 annualized | FY2025 / Q2-2026 | 2,379 ÷ 26.1; 734 × 4 ÷ 27.98 | as above |
| Robinhood | Opex ÷ average TPA [C] | ≈92 bps | FY2025 | 2,379 ÷ 258.5 B | as above |
| Robinhood | Q4-2025 operating expenses | $633 M (+38%), driven by marketing, growth and acquisitions | Q4-2025 | — | [Barchart FY2025](https://www.barchart.com/story/news/140750/robinhood-reports-fourth-quarter-and-full-year-2025-results) |
| eToro | Adjusted EBITDA | $317 M (+4%) = 36.5% of NC [C]; FY2024: $304 M = 38.6% [C] | FY2025 | — | [eToro FY2025](https://www.fintechfutures.com/press-releases/etoro-reports-fourth-quarter-and-full-year-2025-results) |
| eToro | Net income | $216 M (+12% vs $192 M) = 24.9% of NC [C] | FY2025 | — | as above |
| eToro | Net income | $53 M (+77%) = 23.1% of NC [C]; diluted EPS $0.58 (vs $0.31); adjusted diluted EPS $0.68 (vs $0.56) | Q2-2026 | — | [StockTitan](https://www.stocktitan.net/news/ETOR/etoro-reports-second-quarter-2026-p56dsara3gcv.html); [eToro Q2-2026](https://www.etoro.com/news-and-analysis/press-releases/etoro-reports-second-quarter-2026-results/) |
| eToro | Net income | $82 M (+37%) = 31.8% of NC [C] | Q1-2026 | — | [Finance Magnates](https://www.financemagnates.com/fintech/etoro-q1-net-income-climbs-37-to-82-million-on-commodities-surge/) |
| eToro | Adjusted cost base ÷ average AUA [C] | ≈314 bps | FY2025 | (868 − 317) ÷ 17.55 B. "Cost" here means NC less adjusted EBITDA. | as above |
| flatexDEGIRO | EBITDA | €267.7 M, 47.8% margin; net income €160 M (+44%) = 28.6% [C] | FY2025 | — | [FTK FY2025](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| flatexDEGIRO | Operating profit | ≈€85 M (+>50%) under IFRS 18; margin [C] 51.1%. Net income +55% (headline). | Q2-2026 | IFRS 18 adopted in 2026, so comparability with 2025 EBITDA is limited. | [Investing.com news](https://m.investing.com/news/earnings/flatexdegiro-posts-record-secondquarter-profit-raises-2026-outlook-4806645?ampMode=1); [webdisclosure](https://www.webdisclosure.com/press-release/online-broker-flatexdegiro-further-expands-record-results-and-increases-net-income-by-55-percent-pIHtqXjeilQ) |
| flatexDEGIRO | Cost per average account [C] | ≈€89 (EBITDA-basis costs) | FY2025 | (560 − 267.7) ÷ 3.3 M | as above |
| flatexDEGIRO | Costs ÷ average AuC [C] | ≈35 bps | FY2025 | 292.3 ÷ 83.4 B | as above |
| Avanza | Operating expenses | SEK 1,413 M (+10.4%, guidance 11%) vs 1,280 M | FY2025 | Cost/income [C] 31.4% (2024: 32.8%); operating profit SEK 3,078 M, margin [C] 68.5%; profit SEK 2,631 M | [Avanza FY2025 (Inderes)](https://www.inderes.fi/en/releases/avanza-bank-holding-ab-publ-preliminary-financial-statement-2025) |
| Avanza | Costs ÷ savings capital | 14 bps (unchanged) | Q2-2026 | FY2025 [C] ≈13.5 bps (1,413 ÷ 1,045 B) | [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-avanza-bank-posts-record-q2-2026-profit-shares-rise-93CH-4789991) |
| Avanza | Operating expenses | SEK 406 M (+15%) | Q2-2026 | Cost/income [C] 30.4%; operating profit SEK 928 M (+31%), margin [C] 69.6%; profit SEK 795 M (+33%); EPS SEK 4.97 | [Avanza Q2-2026 (Inderes)](https://www.inderes.se/en/releases/avanza-bank-holding-ab-publ-interim-report-january-june-2026) |
| Avanza | Opex per average customer [C] | SEK 655 | FY2025 | 1,413 M ÷ 2,157,200 | as above |
| Nordnet | Operating expenses | SEK 440 M (+11%; core Nordic +7.5% excluding Germany) | Q2-2026 | Cost/income [C] 26.9% (company: "efficiency ratio 27%"); operating profit SEK 1,190 M, margin [C] 72.8%; diluted EPS SEK 3.80 (vs 2.84) | [Nordnet Q2-2026 report](https://nordnetab.com/wp-content/uploads/2026/07/2Q26-report.pdf); [call highlights](https://ca.investing.com/news/company-news/nordnet-ab-publ-fra9jl-q2-2026-earnings-call-highlights-record-revenue-and-customer--4745172) |
| Nordnet | Cost per customer and costs ÷ savings capital [C] | ≈SEK 715 a year; 12.8–14.9 bps | Q2-2026 annualized | 1,760 M ÷ ~2.46 M; 1,760 ÷ 1,374 B (lower bound) or ÷ 1,183 B (upper bound) | as above |
| Nordnet | Adjusted operating profit | SEK 3,748 M (record); adjusted opex +8.1% excluding Germany | FY2025 | Q4-2025 cost/income [C] ≈30.6% = (1,391 − 966) ÷ 1,391 | [Nordnet AR2025](https://news.cision.com/nordnet/r/nordnet-publishes-annual-and-sustainability-report-for-2025,c4320623); [Q4-2025](https://news.cision.com/nordnet/r/nordnet-ab-publishes-its-fourth-quarter-2025-interim-report,c4298500) |
| Webull | Adjusted operating profit | $62.6 M (+169%) = 31.5% margin [C]; total opex +13% | Q2-2026 | — | [Webull Q2-2026 (Barchart)](https://www.barchart.com/story/news/3937147/webull-reports-second-quarter-2026-financial-results) |
| Trading 212 UK Ltd | Net profit | £92.2 M = 33.2% net margin [C] | FY2025 | — | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/trading-212-uk-revenues-soar-72-in-2025-to-277m-profit-tops-92m/) |
| Trading 212 Group | Net profit | £43.8 M on >£194 M revenue | FY2024 | Secondary | [Wikipedia](https://en.wikipedia.org/wiki/Trading_212) |

### Inferences
- Cost per asset unit spans more than 25x across models:
  - Nordics: 13–15 bps.
  - flatexDEGIRO: ≈35 bps.
  - Robinhood: ≈92 bps.
  - eToro: ≈314 bps.
- Cost per customer converges much more: Robinhood $91–105, flatexDEGIRO €89, Avanza SEK 655, Nordnet ≈SEK 715. The SEK figures are ≈€60–65 at an illustrative ~11 SEK/EUR.
- For the driver tree, model costs as cost per customer plus a variable component (marketing, transaction costs), not as bps of assets.
- Nordic margins of about 70% show the ceiling for scaled, asset-heavy mass retail. Robinhood (47–57%) and flatexDEGIRO (48–51%) are mid-band. eToro (≈37% adjusted EBITDA on NC) is lower because of heavy marketing and multi-jurisdiction costs; this is an inference.

### Gaps
- Not captured: eToro total opex and its split; flatexDEGIRO FY2025 opex lines and Q2-2026 opex; Webull opex; Trade Republic profitability (only an unreliable secondary figure).

## 10. Definitional differences: how comparable are these metrics across companies?

### Takeaway
Customer units, asset perimeters, revenue lines and flow measures all differ in ways that move ratios by tens of percent. The biggest traps:
- eToro's net contribution versus its gross GAAP revenue.
- Robinhood's TPA, which nets margin debt and includes non-custodied RIA assets.
- flatexDEGIRO counting accounts rather than persons, plus its 2026 IFRS 18 re-presentation and the conflicting €/transaction series.
- Avanza/Nordnet "savings capital", which covers all products including funds and pensions.
- Robinhood's Funded Customers and eToro's Funded Accounts, which differ on recency.

### Cited Findings

| Company | Customer unit (activity criterion) | Asset metric | Revenue metric | Flow metric | Source |
|---|---|---|---|---|---|
| Robinhood | Funded Customer: unique person; balance > 0 or a transaction within 45 days; joint holders each counted; includes TradePMR RIA end-clients (Q1-2025 on) and Bitstamp (June-2025 on) | TPA: fair value of equities, options, crypto, futures and event contracts, plus cash, **net of margin receivables**, plus non-custodied TradePMR RIA assets; trade-date basis | GAAP total net revenues. ARPU = revenue ÷ average Funded Customers, annualized (verified by arithmetic, §3). | Net Deposits. Growth rate = annualized net deposits ÷ prior-period-end TPA. | [10-K](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000023/hood-20251231.htm); [SEC CORRESP](https://www.sec.gov/Archives/edgar/data/1783879/000178387924000187/filename1.htm) |
| eToro | Funded Account: KYC complete, deposited, at least one trade **ever**, positive balance (no recency test) | AUA (definition not captured) | **Net Contribution** = total revenue and income − cost of crypto revenue − margin interest expense | Net inflows not captured | [Prospectus](https://www.stifel.com/prospectusfiles/PD_7111.pdf) |
| flatexDEGIRO | Customer **Accounts** (not persons) | AuC = securities + customer cash deposits | IFRS revenues (IFRS 18 presentation from 2026). Commission per transaction: quarterly series (€4.39–4.64) conflicts with FY2025 €4.90. | **Net Cash Inflows** (perimeter not captured) | [FTK Q2-2026](https://s206.q4cdn.com/770226284/files/doc_news/2026/07/260722-flatexDEGIRO_Press-Release_Q2-2026-Results.pdf); [FTK FY2025](https://app.boersengefluester.de/en/newswire/DE000FTG1111/flatexdegiro-se/flatexdegiro-extends-its-profitable-growth-trajectory-with-fy-2025-guidance-slightly-exceeded-2281786) |
| Avanza | Customers (net adds reported) | Savings capital | Operating income. Income ÷ savings capital and costs ÷ savings capital are annualized on average savings capital (verified by arithmetic, §3). | Net inflow; market share of the Swedish savings market and of net inflow | [Avanza Q2-2026](https://www.inderes.se/en/releases/avanza-bank-holding-ab-publ-interim-report-january-june-2026); [Aug-2026 monthly](https://www.inderes.se/en/releases/august-monthly-statistics-7) |
| Nordnet | Customers ("active customers" in management language); YoY growth rates sometimes adjusted, e.g. for the Ikano loan-book sale | Savings capital; lending includes mortgages | (Adjusted) operating income. Income per trade = net transaction-related income ÷ trades (≈ verified). | Net savings | [Nordnet Q2-2026](https://nordnetab.com/wp-content/uploads/2026/07/2Q26-report.pdf); [Inderes Jan-2025](https://inderes.dk/releases/nordnet-monthly-statistics-january-4) |
| Webull | Funded accounts vs registered users | Customer assets | Total revenues; trading-related revenue | Not captured | [Webull 6-K](https://www.sec.gov/Archives/edgar/data/0001866364/000121390026091702/ea030257601ex99-1.htm) |
| Trade Republic | "Kunden" (undefined) | "Verwaltetes Vermögen" (undefined) | Unaudited and inconsistent in the secondary press | — | [TR release](https://assets.traderepublic.com/assets/files/251217_Secondary_PressRelease_DE_DE2.pdf) |
| Trading 212 | Entity-level statutory accounts (UK Ltd vs Group) | — | Statutory revenue (UK Ltd FY2025) | — | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/trading-212-uk-revenues-soar-72-in-2025-to-277m-profit-tops-92m/) |

### Inferences
Normalization rules for the model:
- **Customers:** convert accounts to persons where possible. Apply a recency/balance filter so that Robinhood-style counts and eToro-style counts are comparable.
- **Revenue:** use net revenue, which means net contribution for eToro.
- **Client assets:** state whether margin debt is netted (Robinhood nets it) and whether non-custodied assets are included.
- **Flows:** separate cash flows from securities transfers.
- **Ratios:** compute bps on **average** assets, not period-end assets. Several ratios above bracket the two because average data was missing.

### Gaps
- Verbatim definitions were not captured for: eToro AUA; flatexDEGIRO Customer Accounts and Net Cash Inflows; Avanza and Nordnet customers, savings capital and net inflow/net savings; Robinhood Net Deposits (including treatment of promotions and acquisitions).
- These are in each report's glossary or APM section (links above).

## 11. Benchmark summary for the driver tree (latest periods; ratios computed unless stated "reported")

### Takeaway
One-page ranges for the mass-retail segment. Use them as priors, together with the definitional flags in §10. Inputs and arithmetic are in §§1–9.

### Cited Findings

| Driver | Robinhood | eToro | flatexDEGIRO | Avanza | Nordnet | Webull | Trading 212 UK |
|---|---|---|---|---|---|---|---|
| Customers (latest) | 28.6 M persons (Aug-2026) | 4.28 M accounts (Q2-2026) | 3.66 M accounts (Q2-2026) | 2.37 M (Aug-2026) | 2.54 M (Aug-2026) | 5.13 M funded (Q2-2026) | n/a |
| Customer growth YoY | +7% | +18% | +11% | ≈+8–9% | +12.3% | +8% | +69% funded accounts (FY2025) |
| Client assets per customer | $13.4k | $4.4k | €29.6k | SEK 533k | SEK 564k | $5.6k | n/a |
| Net inflow, % of opening assets, annualized | 27% TTM (Q2-2026); 35% (FY2025) | n/a | 10.9% (H1-2026); 11.4% (FY2025) | 7.1% (2026 YTD); 5.2% of average (FY2025) | 9.3% (2026 YTD) | n/a | n/a |
| Share of asset growth from flows | 52% (FY2025); 37% (Q2-2026) | n/a | 33% (FY2025); 41% (H1-2026) | 28% (2026 YTD) | 29% (2026 YTD) | n/a | n/a |
| Revenue ÷ average client assets | 173 bps (FY2025); ≈154 bps (Q2-2026) | ≈495 bps (FY2025, NC); ≈509 bps (Q2-2026) | 67 bps (FY2025); 66 bps (Q2-2026) | 43 bps (FY2025, reported); 47 bps (Q2-2026, reported) | ≈48–55 bps (Q2-2026) | ≥279 bps (Q2-2026) | n/a |
| ARPU, annual | $171 (FY2025, reported); $187 (Q2-2026, reported) | $238 (FY2025); $221 (Q2-2026) | €170 (FY2025); €184 (Q2-2026) | SEK 2,084 (FY2025); SEK 2,302 (Q2-2026) | ≈SEK 2,650 (Q2-2026) | ≈$155 (Q2-2026) | n/a |
| Transaction/trading share of revenue | 58.8% (FY2025); 59.3% (Q2-2026) | 66.8% (Q2-2026, capital markets + crypto) | 65.9% (FY2025); ≈61% (Q2-2026) | 27% (FY2025, brokerage only) | 45.3% (Q2-2026) | 74.3% (Q2-2026) | 92.6% (FY2025) |
| NII share of revenue | 33.8% (FY2025); 29.7% (Q2-2026) | 21.4% (Q2-2026) | 31.8% (Q2-2026) | 35% (FY2025) | 41.3% (Q2-2026) | ≤25.7% | 7.4% |
| Subscription share of revenue | ≈3.9% (Gold, Q4-2025) | n/a | n/a | n/a | n/a | n/a | n/a |
| Subscription penetration | 16.9% (Q2-2026); 40% of new customers | n/a | n/a | n/a | n/a | n/a | n/a |
| Trades per customer per year | n/a | n/a | 23 (FY2025, reported); 24.2 (Q2-2026) | n/a | ≈30 (Q2-2026); ≈25 (Aug-2026) | n/a | n/a |
| Revenue per trade | ≈$0.0115 per event contract | n/a | €4.64 (Q2-2026, reported) | n/a | SEK 41.9 (Q2-2026, reported) | n/a | n/a |
| Margin loans ÷ client assets | 5.6% (Aug-2026) | n/a | n/a | n/a | 2.2–2.3% (all lending) | n/a | n/a |
| Uninvested cash ÷ client assets | 8.1% sweep + 5.1% cash and deposits | n/a | 6.0% | n/a | n/a | n/a | n/a |
| Marketing ÷ revenue | 8.9% (FY2025) | 20% (Q4-2025, reported); up to 25% in 2026 | n/a | n/a | n/a | n/a | 18.6% (FY2025) |
| CAC proxy (marketing ÷ net adds; upper bound) | ≈$222 (FY2025) | ≈$575 (Q4-2025) | n/a | n/a | n/a | n/a | n/a |
| Cost/income | 53.2% (FY2025); 56.1% (Q2-2026) | ≈63.5% (NC − adj. EBITDA, FY2025) | ≈52% (EBITDA basis, FY2025) | 31.4% (FY2025); 30.4% (Q2-2026) | 26.9% (Q2-2026) | ≈68.5% (adjusted basis) | n/a |
| Margin | Adj. EBITDA 56.3% (FY2025); 56.7% (Q2-2026); GAAP operating 46.8% (FY2025) | Adj. EBITDA 36.5% of NC; net 24.9% (FY2025) | EBITDA 47.8% (FY2025); operating 51.1% (Q2-2026, IFRS 18) | Operating 68.5% (FY2025); 69.6% (Q2-2026) | Operating 72.8% (Q2-2026) | Adj. operating 31.5% | Net 33.2% (FY2025) |
| Cost per customer, annual | $91 (FY2025); $105 (Q2-2026) | n/a | €89 (FY2025) | SEK 655 (FY2025) | ≈SEK 715 (Q2-2026) | n/a | n/a |
| Costs ÷ average client assets | ≈92 bps | ≈314 bps | ≈35 bps | 13.5–14 bps | ≈13–15 bps | n/a | n/a |

Sources: as cited row by row in §§1–9. Key primary links:
- [Robinhood Q2-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results), [Aug-2026](https://investors.robinhood.com/news-releases/news-release-details/robinhood-markets-inc-reports-august-2026-operating-data), [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000023/hood-20251231.htm)
- [eToro Q2-2026](https://investors.etoro.com/news-releases/news-release-details/etoro-reports-second-quarter-2026-results), [eToro FY2025 20-F](https://www.sec.gov/Archives/edgar/data/0001493318/000121390026022034/ea0278371-20f_etoro.htm)
- [flatexDEGIRO Q2-2026](https://s206.q4cdn.com/770226284/files/doc_news/2026/07/260722-flatexDEGIRO_Press-Release_Q2-2026-Results.pdf)
- [Avanza Q2-2026](https://storage.mfn.se/bec572f7-2a0c-4659-a0e0-c6b1214b997f/avanza-bank-holding-ab-publ-interim-report-january-june-2026.pdf), [Avanza FY2025](https://storage.mfn.se/0fe566e9-ab2b-4934-9b74-a0c97530ebe3/avanza-bank-holding-ab-publ-preliminary-financial-statement-2025.pdf)
- [Nordnet Q2-2026](https://nordnetab.com/wp-content/uploads/2026/07/2Q26-report.pdf)
- [Webull Q2-2026](https://www.sec.gov/Archives/edgar/data/0001866364/000121390026091702/ea030257601ex99-1.htm)

### Inferences
Suggested priors for a generic mass-retail driver tree, with a central case and a range:

| Driver | Prior |
|---|---|
| ARPU | $150–250 a year |
| Revenue ÷ client assets | 45–70 bps (asset-gatherer) or 150–500 bps (activity-monetizer) |
| NII share | 20–40% |
| Net inflows | 7–11% of opening assets (EU) or 25–35% (US high-growth) |
| Trades per customer per year | 23–30 |
| Margin loans ÷ client assets | 2–6% |
| Uninvested cash ÷ client assets | 6–13% |
| Marketing | 9–25% of revenue |
| CAC | ≈$200–600 |
| Cost/income | 27–56% |

Interest-rate sensitivity: the NII node should take rate and balance inputs separately. The FY2024–FY2026 swings in the NII share (Robinhood 33.8% → 29.7%; Nordnet NII down in 2025, up 12% in Q2-2026) show that the share is cyclical.

### Gaps
- FY2023 figures were not captured, so a full rate-cycle range for NII is not available from this note.
- Robinhood options and crypto take rates, Avanza activity metrics, and any explicit churn or cohort data remain open. These are the highest-value items for a follow-up pass with document access or more search budget.
