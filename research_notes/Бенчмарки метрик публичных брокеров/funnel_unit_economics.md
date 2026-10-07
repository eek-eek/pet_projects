# Client lifecycle funnel and unit economics benchmarks: retail and affluent brokerage / investment platforms

*How the data was collected (October 2026).* The network proxy blocked direct fetching of primary documents in this session (SEC EDGAR, company IR sites, vendor sites, cbr.ru). Partway through the research, the shared web-search budget also ran out. Every figure below therefore comes from a **search-engine extract of the cited page**: the URL given is the page the extract came from, but the full document was not opened. Figures marked **(calc)** are my own arithmetic on cited inputs.

**Confidence levels:**
- **A**: company, regulator or exchange disclosure.
- **B**: reputable press, an analyst summary of a disclosure, or an independent survey.
- **C**: vendor marketing, an aggregator, or a figure whose source is unclear. Treat these as lower confidence.

---

## 1. Onboarding funnel: install/visit → registration → KYC → account opened → funded → first trade; time to fund and first trade; first deposit; KYC pass and auto-approval rates; drop-off during identity verification

### Takeaway
No listed broker publishes step-by-step funnel conversion. The best public proxies are ratios between the funnel layers that brokers do disclose:
- **Registered users → funded accounts:** ≈9% at eToro, ≈11.5% at Futu (users → funded) and ≈19–23% at Webull.
- **Brokerage account opened → funded:** ≈57%, from Futu (2025) only.

Benchmarks for KYC and identity verification (IDV) come almost entirely from vendors. They report 60–90% completion for fully digital KYC, and 68% of European consumers say they have abandoned at least one financial application. I found no reliable public benchmark for time to fund, time to first trade or broker auto-approval rates.

### Cited Findings

| Metric | Value / range | Period | Population / market | Definition / notes | Source | Conf. |
|---|---|---|---|---|---|---|
| Futu funnel layers | 29.2M users (+16.0% YoY) → 5,948,093 brokerage accounts (+29.8%) → 3,365,414 funded accounts (+39.6%); client assets HK$1.23T (+65.9%) | 31 Dec 2025 | Futu / moomoo, multi-market online broker (HK-based) | Cumulative counts. "Users" includes app users who have no brokerage account. Earlier releases used "paying clients" (2.41M at end-2024, +41% YoY), which is consistent with the +39.6% growth. | [Futu Q4/FY2025 results](https://futuholdings.gcs-web.com/news-releases/news-release-details/futu-announces-fourth-quarter-and-full-year-2025-unaudited) | A |
| Futu conversion ratios (calc) | User → brokerage account **20.4%**; brokerage account → funded **56.6%**; user → funded **11.5%** | 31 Dec 2025 | Same as above | Ratios between cumulative counts, not flow conversion of a single cohort | Calc from [Futu FY2025](https://futuholdings.gcs-web.com/news-releases/news-release-details/futu-announces-fourth-quarter-and-full-year-2025-unaudited) | calc |
| eToro registered users vs funded accounts | ~40M registered users; 3.58M funded accounts on 31 Mar 2025 (+14% YoY from 3.13M, helped by the 2024 Spaceship acquisition in Australia); 3.61M funded and AUA $16.9B on 31 May 2025 | 2025 | eToro, global multi-asset / CFD platform | — | [eToro Q1 2025 results](https://investors.etoro.com/news-releases/news-release-details/etoro-reports-first-quarter-2025-results); [eToro F-1 (SEC)](https://www.sec.gov/Archives/edgar/data/1493318/000121390025039451/ea0223534-11.htm) | A |
| eToro "Funded Account" definition | A user who completed KYC, AML and other onboarding, activated the account, deposited funds, **executed at least one trade at any time** and has a positive balance (invested or uninvested) | 2025 | eToro | This is stricter than a "funded" definition based on balance only. eToro's "funded" stage is effectively "funded + first trade". | [eToro Q1 2025 results](https://investors.etoro.com/news-releases/news-release-details/etoro-reports-first-quarter-2025-results) | A |
| eToro historic layers | 1.6M new registered users in the quarter; 24.8M registered in total; 2.14M funded accounts | Q3 2021 (pre-2022) | eToro | — | [eToro Q3 2021 press release](https://www.etoro.com/wp-content/uploads/2021/11/eToro_Q3_2021_PR_Draft_FINAL.pdf) | A |
| eToro funded ÷ registered (calc) | ≈**9.0%** (May 2025); ≈8.6% (Q3 2021) | 2021, 2025 | eToro | Cumulative registrations since launch, including never-converted and dormant users | Calc from the sources above | calc |
| Webull registered users vs funded accounts | Registered users 16.2M (end-2022) → 26.8M (end-2025, +15% YoY); funded accounts 3.7M (2022) → just over 5.0M (end-2025, +8% YoY) | 2022–2025 | Webull, US and international | — | [Webull investor presentation (SEC EX-99.2)](https://www.sec.gov/Archives/edgar/data/1866364/000121390025046933/ea024314301ex99-2_webull.htm); [Finance Magnates](https://www.financemagnates.com/forex/brokers/webull-posts-record-571m-revenue-in-first-year-as-public-company) | A/B |
| Webull funded ÷ registered (calc) | **22.8%** (2022) → **18.7%** (2025) | 2022–2025 | Webull | Registrations grew faster than funded accounts | Calc | calc |
| Robinhood funnel lever | Referral-program shares were awarded **when a new user first linked a bank account**, rather than at account approval. This rewarded only higher-intent users and lowered the cost per new funded account. | S-1, 2021 (covers 2020) | Robinhood, US | A documented intervention at a specific funnel step | [Robinhood S-1](https://www.sec.gov/Archives/edgar/data/1783879/000162828021013318/robinhoods-1.htm) | A |
| Initial net inflow per new funded client (UP Fintech / Tiger) | > **US$32,000** on average (a record), of which Singapore ≈US$62,000 and Hong Kong ≈US$30,000 | Q3 2025 | Tiger Brokers, Asia-focused affluent online broker | Average net asset inflow of newly funded clients in the quarter. This is a proxy for first deposit, not first deposit strictly. | [UP Fintech Q3 2025 results (Nasdaq)](https://www.nasdaq.com/press-release/fintech-holding-limited-reports-unaudited-third-quarter-2025-financial-results-2025); [GuruFocus transcripts](https://www.gurufocus.com/stock/STU:1M5/transcripts/3234514) | A/B |
| Average first-time deposit (Tiger Singapore) | About $5,000 (currency probably SGD) "since October" | c. 2021 (pre-2022) | Tiger Brokers Singapore | Company news item | [Tiger Brokers SG news](https://www.itiger.com/sg/about/news/828) | B |
| Average first deposit at FX / CFD brokers | US$3,800 globally; US$6,600 in the US | Undated; probably pre-2022 | Retail FX brokers on MT4/MT5 | Different product (FX / CFD), shown for context only | [FinanceFeeds](https://financefeeds.com/retail-fx-deposits-still-way-traditional-funds-investments-cost/) | C |
| Average deposit per active customer (Plus500, CFD) | ≈$6,150 (headline: "active users rise to 121k") | Quarter not confirmed in extract (2024–25) | Plus500, CFD | Average deposit per active customer, not first deposit | [Finance Magnates](https://www.financemagnates.com/forex/brokers/plus500-active-users-rise-to-121k-as-average-deposits-surge-to-6150) | B/C |
| Digital KYC completion (vendor) | Fully digital KYC typically converts **60–90%**. IDV conversion ranges from 50% to over 90% depending on industry, geography and workflow. Claim: "70% of users abandon KYC flows that take > 3 minutes". | 2024–25 blog | Cross-industry (fintech, crypto, gaming) | Completion = share of users who start KYC and finish it. Vendor marketing. | [Didit blog](https://didit.me/blog/benchmarking-kyc-conversion-rates/) | C |
| Consumer abandonment of financial onboarding (vendor survey) | **68%** of consumers had abandoned a financial application (63% in 2020; the highest since the series began in 2016). Estimated loss to financial institutions: > €5bn/yr. | 2022 | 7,600 consumers, 14 European countries | Share of consumers who have *ever* abandoned an application, **not** a step drop-off rate | [Signicat "Battle to Onboard 2022"](https://www.signicat.com/press-releases/the-battle-to-onboard-2022) | C |

### Inferences
- **Planning ranges for the driver tree (stock-based):**
  - Registered → funded: about 9–23%.
  - Account opened (KYC passed) → funded: about 55–60%. This rests on a single source (Futu).
  - Registered/app user → brokerage account: about 20% (Futu).
- **Why the registered → funded ranges diverge:**
  - What counts as a "user". Futu counts app users, including community and quote users. eToro counts every registration since launch. Webull counts registrations.
  - The "funded" definition. eToro requires at least one trade plus a positive balance.
  - Stock vs flow. Cumulative registrations pile up never-converters, so flow conversion for recent cohorts is likely higher than these stock ratios.
- Webull's ratio fell from 22.8% to 18.7% between 2022 and 2025. Faster top-of-funnel growth (international expansion and marketing) dilutes stock conversion, so funnel KPIs for hypotheses should be measured per cohort.
- Robinhood moved its reward trigger from approval to bank linking. This marks "funding source linked" as the key intent signal; it is a natural place for an activation milestone and for incentive gating.
- **First deposits differ by orders of magnitude across markets and products:**
  - Asia affluent online brokers: initial net inflow of ~US$30–60k per new funded client (2025).
  - US mass-market apps: historically small balances.
  - FX / CFD: average first deposit of ~$4–7k (older data).
- Vendor KYC completion of 60–90% implies **10–40% drop-off at the identity-verification step** as a low-confidence planning range.

### Gaps
- No step-level conversion (install → registration → KYC start → KYC pass → funded → first trade) was found for any listed broker. The S-1/F-1 extracts did not contain one. The full Robinhood S-1, eToro F-1, Webull and Wealthfront filings could not be opened (proxy block).
- Time to fund and time to first trade: no reliable public benchmark found.
- Broker KYC auto-approval or straight-through account-opening rates: not found. Only generic vendor claims exist, and none were verified.
- Average or median first deposit for US/EU stock brokers in 2022–2026: not found in disclosures.
- Not reached before the search budget ran out: Public.com, Acorns and Stash disclosures; Apex, Alpaca and DriveWealth data; Onfido/Entrust, Jumio and Veriff fraud/IDV reports; Plaid funding-conversion case studies.

---

## 2. Activation and engagement: share of funded accounts trading monthly; new funded accounts still active at 30/90/365 days; recurring investment adoption and its effect on retention

### Takeaway
Engagement disclosures are sparse. The best anchors are:
- **Robinhood:** monthly active users (MAU) ÷ funded customers ≈ **47%** (Q4 2023).
- **Moscow Exchange (2025):** **8.7%** of all individual account holders trade in an average month, and **25%** trade at least once in the year.
- **App analytics:** trading apps retain ≈23% of installers on day 1 and ≈12% on day 30 (Adjust). Finance apps overall retain ≈5–9% on day 30 (Liftoff/AppsFlyer, Q4 2025).

No public figures were found for recurring-investment adoption. Academic evidence shows that automated investment rules causally raise savings and reduce trend-chasing.

### Cited Findings

| Metric | Value / range | Period | Population / market | Definition / notes | Source | Conf. |
|---|---|---|---|---|---|---|
| Robinhood MAU vs funded customers | 10.9M MAU vs 23.4M funded customers → MAU/funded ≈ **47%** (calc) | Q4 2023 | Robinhood, US mass market | Robinhood's own MAU definition (not re-verified) | [Benzinga, Robinhood Q4 2023](https://benzinga.com/news/earnings/24/02/37107009/robinhood-q4-earnings-highlights-revenue-beat-eps-beat-strong-start-to-q1-and-more) | B |
| Robinhood funded customers | **27.0M** (+1.8M, +7% YoY) | Q4 2025 | Robinhood, US | — | [Robinhood Q4/FY2025 results](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-fourth-quarter-and-full-year-2025-results) | A |
| Moscow Exchange activity | 40.1M individuals with brokerage accounts (+5M in 2025). **10.2M** traded on the stock market during 2025 (**25.4%**, calc). **3.5M** traded in an average month (**8.7%**, calc). | 2025 | Russia, all retail account holders | "Traded" = concluded at least one deal on the MOEX stock market. The denominator includes empty accounts. | [MOEX](https://www.moex.com/n96827); [SPMag summary](https://spmag.ru/news/itogi-deyatelnosti-mosbirzhi-za-2025) | A |
| Trading-app retention (Adjust) | Stock-trading apps: day-1 **23%** → day-30 **12%**. Bank apps: 22% → 10%. | 2023–2024 data (published 2025) | Global, Adjust measurement panel | Retention of installers | [Adjust, Finance app insights 2025](https://www.adjust.com/blog/finance-app-insights-2025/) | B |
| Finance-app retention and engagement (Adjust) | Finance apps overall: day-1 retention 13.8% (2023) → 12.5% (H1 2025); banking apps 20.6%. Stock-trading apps in H1 2025: installs +1% YoY, sessions +8% YoY (+34% in Q3), session length 12.1 minutes. | 2023 – H1 2025 | Global | — | [Adjust 2025](https://www.adjust.com/blog/finance-app-insights-2025/); [Business Wire, Oct 2025](https://www.businesswire.com/news/home/20251029280342/en) | B |
| Finance-app retention (Liftoff / AppsFlyer) | Day-30 ≈ **9% on iOS** and ≈ **5% on Android** (Q4 2025). iOS day-1 retention was 21–25% throughout 2025. Finance user-acquisition spend +47% and re-engagement spend ×2.15 in 2025. | 2025 | Global finance and crypto apps | The extract did not make clear which figures are Liftoff's and which are AppsFlyer's | [Liftoff 2026 Finance & Crypto App Benchmark](https://liftoff.ai/?p=35649); [AppsFlyer newsroom](https://www.appsflyer.com/company/newsroom/pr/europe-fintech-growth/) | C |
| International share of European investment-app installs | > **85%** of investment-app installs in Europe go to international providers | 2025 | Europe | — | [AppsFlyer newsroom](https://www.appsflyer.com/company/newsroom/pr/europe-fintech-growth/) | B |
| Wealthfront cross-product adoption | Clients who first funded a cash account or an advisory account and later funded the other type: **27% of funded clients** holding **59% of platform assets** | 31 Jul 2025 | Wealthfront, US digital wealth (>1.3M funded clients, ~$88B platform assets) | — | [Wealthfront S-1](https://www.sec.gov/Archives/edgar/data/1524566/000162828025043113/wealthfront-sx1.htm) | A |
| Automated (recurring) investment rules: causal effects | Automated rules **causally increase average savings** without crowding out manual contributions. Automated deposits do not chase recent returns, unlike manual ones. Adopters cite avoiding procrastination and reducing cognitive load. | Working paper (Georgetown's Alberto Rossi et al.; year not confirmed) | Users of a fintech mutual-fund app | Academic study | [Rutgers-hosted paper "Set it and Forget it"](https://www.business.rutgers.edu/sites/default/files/documents/set-it-and-forget-it.pdf); [Tsinghua PBCSF seminar listing](https://www.pbcsf.tsinghua.edu.cn/info/1504/10114.htm) | B |
| Trade Republic scale (savings-plan-led model) | 8M customers and ~€100bn in assets. Savings plans auto-invest chosen amounts at chosen intervals. More than 1M French customers can use commission-free savings plans inside a PEA. | Jan 2025 | Europe (DE, FR, ES, IT, …) | Share of customers with an active savings plan **not disclosed** in the extract | [Trade Republic press release, Jan 2025](https://assets.traderepublic.com/assets/files/250109_TradeRepublic_PressRelease_BirthdayAnnouncement_DE_EN.pdf); [Crowdfund Insider](https://www.crowdfundinsider.com/?p=235098) | A/B |
| Recurring investments → engagement and LTV (vendor claim) | "Automated recurring investments boost investing activity, drive consistent engagement, and increase customer lifetime value". Qualitative, no figures. | 2025 | Upvest (B2B investment API vendor) | Marketing claim | [Upvest](https://upvest.co/use-cases/savings-plans) | C |

### Inferences
- **Monthly active share of funded accounts:** about 45–50% is a reasonable anchor for a US mass-market app in a normal market (Robinhood, Q4 2023). It is much lower when the denominator includes unfunded accounts: 8.7% of all MOEX account holders.
- Applying the ~65% zero-balance account share (section 3) gives roughly 25% of non-empty Russian accounts trading monthly. This is a rough calc that mixes sources and treats accounts as if they were investors.
- Day-30 app retention of 5–12% means most installs never become engaged users. Funnel models should start from registrations (or KYC starts), not installs.
- Webull and Futu keep ≥97–98% of funded accounts each quarter (section 3). Once an account is funded, closure is rare. **Inactivity, not account closure, is the main way funded clients drop off.** Activation hypotheses should therefore target recurring behaviour, such as deposits, auto-invest and cross-product use.
- Wealthfront's concentration (27% of clients holding 59% of assets) and the causal academic evidence on automation point to **automation and multi-product adoption** as the main levers for deepening activation. No public source quantifies the retention uplift.

### Gaps
- Share of new funded accounts still active at 30, 90 or 365 days: not disclosed by any broker found.
- Recurring-investment adoption (Robinhood, Acorns, Stash, Betterment, Trade Republic, Scalable, eToro) and its measured effect on retention: not found before the search budget ran out.
- Robinhood MAU for 2024–2025: one extract quoted "16.6M MAU as of February 2026". That is inconsistent with the ~11M level of 2023–24, possibly because of a definition change. It is **unverified** and left out of the findings.
- Sensor Tower data: not searched.

---

## 3. Retention and churn: annual customer churn and asset attrition; cohort retention curves; dormant account share; documented drivers of churn

### Takeaway
Listed brokers lose few funded accounts:
- **Quarterly funded-account retention:** ≥97–98% at Webull and Futu, which annualises to ≈88–92%.
- **Annual client retention at UK and US investment platforms:** 91–95% (Hargreaves Lansdown, AJ Bell, Wealthfront).
- **Asset retention at Hargreaves Lansdown:** 87.7–91.4%.

Mass-market markets show dormancy rather than closure. In Russia about 65% of brokerage accounts have a zero balance, and about 80% of investors hold zero or less than 10k RUB. High costs and fees are the most documented reason for switching (30% of switchers in a 2023 Canadian study).

### Cited Findings

| Metric | Value / range | Period | Population / market | Definition / notes | Source | Conf. |
|---|---|---|---|---|---|---|
| Webull quarterly funded-account retention | Consistently **> 97%**; ≈98% during 2025, ≈97% by end-2025 | 2022–2025 | Webull | Company-defined "retention rate"; exact definition not verified | [Webull investor presentation (SEC EX-99.2)](https://www.sec.gov/Archives/edgar/data/1866364/000121390025046933/ea024314301ex99-2_webull.htm); [Investing in the Web (aggregator)](https://investingintheweb.com/brokers/webull-statistics) | A/C |
| Futu quarterly funded-account retention | "Well above **98%**" | Q2 2025 | Futu / moomoo | Company-defined | [Futu Q2 2025 results (SEC 6-K)](https://www.sec.gov/Archives/edgar/data/1754581/000110465925080455/tm2523738d1_ex99-1.htm); [Tiger news mirror](https://www.itiger.com/hans/news/2560112000) | A |
| Implied annual retention (calc) | 0.97⁴ = **88.5%**; 0.98⁴ = **92.2%** → annual funded-account churn ≈ 8–11.5% | — | Webull, Futu | Assumes quarters are independent | Calc | calc |
| Wealthfront annual client retention | **95%** in FY2024 and FY2025. Annual net revenue retention **> 120%** in each of the last 11 fiscal years, driven by clients adding deposits. | FY to 31 Jan 2024 and 2025 | Wealthfront, US | The 95% figure comes from analyst summaries of the S-1; the net revenue retention figure is from the S-1 | [Wealthfront S-1](https://www.sec.gov/Archives/edgar/data/1524566/000162828025043113/wealthfront-sx1.htm); [Mridul Kabra S-1 analysis](https://mridulkabra.substack.com/p/wealthfronts-ipo-a-high-margin-fintech); [MostlyMetrics](https://www.mostlymetrics.com/p/wealthfront-ipo-s1-breakdown) | A/B |
| Hargreaves Lansdown client and asset retention (annual) | Client retention fell from 92.1% to **91.4%**, and asset retention from 91.4% to **88.5%**, "over the three-year period" reported with the FY2024 results (the exact base year is not clear in the extract) | Three years to FY2024 (FY to 30 Jun 2024) | UK, D2C investment platform | HL-defined retention rates; see trading-update footnotes | [Investment Week](https://investmentweek.co.uk/news/4345064/hargreaves-lansdown-net-inflows-dip-client-asset-retention-rates-decline) | B |
| Hargreaves Lansdown quarterly retention (annualised) | Q4 FY24 (3 months to 30 Jun 2024): client **91.1%**, asset **87.7%**. Q1 FY25 (3 months to 30 Sep 2024): client **92.0%**, asset **88.6%**, both below HL's medium- to longer-term ambitions. | 2024 | UK | — | [HL Q4 trading update, Jul 2024](https://hl.co.uk/__data/assets/pdf_file/0004/20046514/Q4-Trading-Update-19-July-2024.pdf); [HL Q1 trading update, Oct 2024](https://www.hl.co.uk/__data/assets/pdf_file/0008/20260871/Q1-Trading-Update-29-October-2024.pdf) | A |
| AJ Bell customer retention | **94.2%** in FY2024 vs **95.2%** in FY2023. 542k platform customers (+66k, +14%); AUA £86.5bn; net inflows £6.1bn. | FY to 30 Sep 2024 | UK, advised and D2C platform | — | [AJ Bell FY2024 results](https://www.ajbell.co.uk/group/investor-relations/market-announcements/final-results-3) | A |
| eToro tenure by loyalty tier | **72%** of eToro Club members have had a funded account for ≥3 years, vs **62%** of non-members. The share rises with Club tier. | F-1, 2025 | eToro, global | Tenure distribution of current accounts, **not** a cohort survival rate | [eToro F-1 (SEC)](https://www.sec.gov/Archives/edgar/data/1493318/000121390025039451/ea0223534-11.htm) | A |
| Robinhood net deposits (asset flow) | $68.1B in 2025 = **35%** of Total Platform Assets at end-2024 | FY2025 | Robinhood, US | Net deposits ÷ opening platform assets | [Robinhood FY2025 results](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-fourth-quarter-and-full-year-2025-results) | A |
| Robinhood cohort economics (S-1) | 2017 cohort deposits 1,731 in the first year → 6,127 by end-2020. 2020 cohort > 18,000 in deposits by end-2020. 2017 cohort revenue 17 (2017) → 130 (2020). 2020 cohort revenue 326 in 2020. | 2017–2020 (pre-2022) | Robinhood annual cohorts | **Units are ambiguous.** The secondary summary presents these as per-user dollars, but the sizes fit cohort totals in **$ millions** (2020 revenue was ≈$959M in total). Verify against the S-1 cohort charts. The direction is clear either way: older cohorts' deposits and revenue grew over time (net expansion). | [Vested Finance S-1 summary](https://vestedfinance.com/blog/robinhoods-ipo/) | B |
| Russia: dormant and empty accounts | More than 40M investors. About **80%** hold zero or less than 10k RUB. About **65%** of open brokerage accounts have a **zero balance**. Brokerage-account holders = 51% of the economically active population. | 2025 | Russia | Press summaries of Bank of Russia data; which article/report gives which figure was not verified | [Expert.ru](https://expert.ru/finance/dengi-zabili-klyuchom); [Sovcombank Journal](https://journal.sovcombank.ru/news/brokerskie-scheta-okazalis-ne-nuzhni-rossiyanam); [Bank of Russia, "Portrait of a broker client"](https://www.cbr.ru/content/document/file/143859/portrait_client_brok.pdf) | B |
| Russia: inflow from funding new accounts | Record **872bn RUB** in Q3 2025 (Bank of Russia broker KPI review, 3 Nov 2025) | Q3 2025 | Russia | — | [Expert.ru](https://expert.ru/finance/dengi-zabili-klyuchom) | B |
| Kazakhstan: accounts | **5.06M** accounts at the Central Securities Depository at end-2025 (+44.6% YoY). Growth came mainly from accounts opened through bank and fintech mobile apps (+55%, +1.5M). | 2025 | Kazakhstan | Share of active or funded accounts not found | [Kapital.kz](https://kapital.kz/finance/145760/v-35-raz-vyroslo-chislo-schetov-roznichnyh-investorov-za-pyat-let.html); [Inbusiness.kz](https://inbusiness.kz/ru/news/armiya-roznichnyh-investorov-v-kazahstane-vyrosla-v-35-raz) | B |
| Churn drivers: reasons for switching | High costs/fees **30%**; better products, tools or services elsewhere **17%**; poor service **13%** | 2023 | Canada, self-directed investors (J.D. Power survey) | Survey of investors who switched firms | [J.D. Power 2023 Canada Self-Directed Investor Satisfaction Study](https://www.jdpower.com/business/press-releases/2023-canada-self-directed-investor-satisfaction-study); [Business Wire](https://www.businesswire.com/news/home/20230511005029/en/Most-Self-Directed-Investor-Companies-in-Canada-Failing-to-Create-Fans-J.D.-Power-Finds) | A/B |
| Churn drivers: UK switching | More than 1 in 10 investors are switching platforms, often for lower costs or better access. Top priorities: low fees, platform usability, and access to international (especially US) shares. | 2025 | UK online investors (Investment Trends survey) | — | [IFA Magazine on Investment Trends 2025](https://ifamagazine.com/investment-trends-2025-uk-online-investing-report/) | B |
| Loyalty and retention of assets | Brokerages with higher loyalty scores retain customers and their assets better when an individual adviser leaves | Year not confirmed | US brokerages (Bain brief) | — | [Bain](https://www.bain.com/insights/to-earn-greater-loyalty-investment-brokerages-should-think-digital/) | B |

### Inferences
- **Annual churn of funded or active clients at established platforms (2023–2025):**
  - ≈5–6%: AJ Bell, Wealthfront.
  - ≈8–9%: Hargreaves Lansdown.
  - ≈8–12% implied from quarterly figures: Webull, Futu.
- **Annual asset attrition:** ≈9–12% at Hargreaves Lansdown.
- Asset retention runs below client retention at Hargreaves Lansdown (87.7–91.4% vs 91.1–92.1%). Asset outflows matter as much as client losses, so the driver tree should model client churn and asset attrition separately.
- **The metrics are not like-for-like:**
  - Hargreaves Lansdown and AJ Bell measure clients leaving the platform.
  - Webull and Futu measure funded accounts that stay funded from one quarter to the next.
  - eToro's figure is a tenure snapshot.
  - None is a cohort survival curve.
- **For mass-market apps, model attrition in two parts:**
  1. Account closure or defunding of ≈2–3% per quarter.
  2. Dormancy (zero balance or inactive), which can reach most opened accounts (≈65% zero-balance in Russia).
- **Documented churn drivers:**
  - Fees and costs: the #1 reason for switching.
  - Product breadth and tools, especially access to US shares in the UK.
  - Service quality.
  - Engagement tier: eToro Club members have longer tenure (72% vs 62% with ≥3 years).

### Gaps
- Cohort retention curves (month 1, 3, 12) were not found for any broker. The Robinhood S-1 cohort charts track deposits and revenue, not customer survival, and their units need checking.
- US incumbents' client churn (Schwab, Fidelity, IBKR): not found.
- ESMA and FINRA Investor Education Foundation data on dormant accounts: not searched (budget).
- Kazakhstan's active or funded share of accounts: not found.

---

## 4. Acquisition: CAC (blended and by channel), referral bonus economics, CAC payback, LTV/CAC

### Takeaway
Disclosed customer acquisition costs (CAC) span about two orders of magnitude, depending on business model and market:

| Segment | CAC | Period |
|---|---|---|
| US mass-market app, referral-led (Robinhood) | **$15–53** | 2019 – Q1 2021 |
| US robo-adviser, fully loaded (Wealthfront, analyst estimate) | **~$85–131** | FY2024–25 |
| Asian online brokers: Tiger | **~$150–400** | 2024–25 |
| Asian online brokers: Futu | **≈HK$2,300 ≈ US$295** | Q3 2025 |
| CFD broker (Plus500) | **~$1,300–1,530** | 2023–24 |

Reported or derived payback periods are short:
- Tiger Hong Kong: ~2 quarters (management).
- Wealthfront: ~6 months of revenue (calc).
- Plus500: about one quarter, measured as the ratio of quarterly revenue per user to acquisition cost (calc).

### Cited Findings

| Metric | Value / range | Period | Population / market | Definition / notes | Source | Conf. |
|---|---|---|---|---|---|---|
| Robinhood average cost to acquire a new funded account | **$53** (FY2019) → **$20** (FY2020), a drop of more than 60%. **$32** (Q1 2020) → **$15** (Q1 2021). | 2019 – Q1 2021 (pre-2022) | Robinhood, US | "Average cost to acquire a new Funded Account" as defined in the S-1 (definition not re-verified) | [Robinhood S-1](https://www.sec.gov/Archives/edgar/data/1783879/000162828021013318/robinhoods-1.htm) | A |
| Robinhood channel mix | Word-of-mouth referral and bank-linking channels brought in **> 80% of new funded accounts in 2020**. These channels have lower direct expense than paid digital and broad-scale advertising. | 2020 | Robinhood, US | S-1 wording as extracted. PYMNTS describes it more narrowly: 80% of new accounts in 2020 – Q1 2021 came from the Referral Program. | [Robinhood S-1](https://www.sec.gov/Archives/edgar/data/1783879/000162828021013318/robinhoods-1.htm); [PYMNTS](https://www.pymnts.com/ipo/2021/robinhood-filing-shows-continued-surge-in-retail-investing) | A/B |
| Robinhood referral reward ("free stock") | One share each to referrer and referred customer; potential value **$2.50–$225** per share | 2021 | Robinhood, US | Expected value and odds not in the extract | [PYMNTS](https://www.pymnts.com/ipo/2021/robinhood-filing-shows-continued-surge-in-retail-investing) | B |
| Wealthfront referral-led acquisition | **> 50%** of new clients were referred by existing clients (last two fiscal years). **40%** of clients sent at least one referral (Oct 2022 – Jul 2025). | FY2024–25 | Wealthfront, US | — | [Wealthfront S-1](https://www.sec.gov/Archives/edgar/data/1524566/000162828025043113/wealthfront-sx1.htm) | A |
| Wealthfront marketing intensity | Marketing expense = **10%** of revenue in FY2024, **17%** in FY2025, and **11%** in the six months to 31 Jul 2025 | FY2024 – H1 FY2026 | Wealthfront | — | [Wealthfront S-1](https://www.sec.gov/Archives/edgar/data/1524566/000162828025043113/wealthfront-sx1.htm) | A |
| Wealthfront CAC | Fully loaded (P&L marketing ÷ new clients): **$85** (FY2024), **$131** (FY2025). "Paid CAC" (advertising plus referral bonus): ≈**$95**. | FY2024–25 | Wealthfront | Analyst calculations or estimates from the S-1; which analyst said what was not verified | [MostlyMetrics](https://www.mostlymetrics.com/p/wealthfront-ipo-s1-breakdown); [Mridul Kabra](https://mridulkabra.substack.com/p/wealthfronts-ipo-a-high-margin-fintech) | B/C |
| Wealthfront referral incentives | Fee waivers (e.g., $5,000 managed free per referral) and APY boosts on the cash account | 2025 | Wealthfront | — | [Wealthfront support](https://support.wealthfront.com/hc/en-us/articles/209353126-Does-Wealthfront-offer-any-referral-benefits); [MoneysMyLife](https://www.moneysmylife.com/wealthfront-promotions/) | B/C |
| Futu CAC | ≈**HK$2,300** (≈US$295, calc at 7.8 HKD/USD), slightly up QoQ and **below the FY2025 target range of HK$2,500–3,000** (≈US$320–385) | Q3 2025 | Futu / moomoo, multi-market | Management statement on the earnings call | [Futu Q3 2025 earnings call (AOL / Motley Fool)](https://www.aol.com/articles/futu-futu-q3-2025-earnings-135047058.html) | B |
| Futu acquisition volume | S&M expense +26.8% YoY in Q2 2025, driven by more new funded accounts and partly offset by lower CAC. FY2025 guidance: 800k net new paying clients; actual ≈955k (calc). Q4 2025: ≈230k net new funded accounts (−8% QoQ, +9% YoY). | 2025 | Futu | — | [Futu Q2 2025 results (SEC 6-K)](https://www.sec.gov/Archives/edgar/data/1754581/000110465925080455/tm2523738d1_ex99-1.htm); [Futu FY2025 results](https://futuholdings.gcs-web.com/news-releases/news-release-details/futu-announces-fourth-quarter-and-full-year-2025-unaudited) | A |
| Tiger CAC | ≈**US$150** (Q1 2024); FY2024 range US$150–180; expected **US$250–300** in 2025. Singapore: > US$100 (2024) → **> US$400** (2025). Hong Kong: ≈**US$400**, with **payback ≈ 2 quarters**. | 2024–2025 | UP Fintech / Tiger Brokers, Asia-focused (incl. Singapore and Hong Kong) | Management statements on earnings calls | [Insider Monkey, Q1 2024 call](https://www.insidermonkey.com/blog/up-fintech-holding-limited-nasdaqtigr-q1-2024-earnings-call-transcript-1310710/); [GuruFocus transcripts](https://www.gurufocus.com/stock/STU:1M5/transcripts/3234514); [MarketBeat, Q1 2025 call](https://www.marketbeat.com/earnings/reports/2025-5-30-up-fintech-holding-limited-stock) | B |
| Tiger new funded accounts | 2024: 187.4k (target 150k); total funded accounts 1.09M (+20.7%); client assets US$41.7B. 2025 by quarter: 60.9k / 39.8k / 31.5k / 29.7k (≈162k for the year, calc). | 2024–2025 | Tiger | — | [Insider Monkey, Q4 2024 call](https://www.insidermonkey.com/blog/up-fintech-holding-limited-nasdaqtigr-q4-2024-earnings-call-transcript-1486675/); [finsee.ai, Q4 2025 review](https://finsee.ai/earnings/tigr/2025/q4/en/) | B |
| Plus500 average user acquisition cost (AUAC) vs revenue per user (ARPU) | AUAC **$1,320** (Q1 2024; Q1 2023: $1,381), **$1,527** (Q3 2024; Q3 2023: $1,398), **$1,501** (9M 2024; 9M 2023: $1,463). ARPU **$1,600** (Q1 2024), **$1,548** (Q3 2024; Q3 2023: $1,418). | 2023–2024 | Plus500, global CFD | Company KPIs, read as AUAC = acquisition cost per new customer and ARPU = revenue per active customer in the period (standard Plus500 usage; not re-verified) | [FX News Group, Q1 2024](https://fxnewsgroup.com/forex-news/retail-forex/plus500-sees-revenue-edge-higher-in-q1-2024/); [FX News Group, Q3 2024](https://fxnewsgroup.com/forex-news/retail-forex/plus500-registers-11-y-y-increase-in-revenues-in-q3-2024/) | A/B |
| eToro marketing spend | **$60M** (Q1 2025) vs $64M (Q1 2024) | 2024–2025 | eToro | Gross new funded accounts not found, so CAC cannot be computed | [eToro Q1 2025 results](https://investors.etoro.com/news-releases/news-release-details/etoro-reports-first-quarter-2025-results) | A |

### Inferences
- **CAC tiers for benchmarking (2022–2025 unless noted):**

  | Segment | CAC range |
  |---|---|
  | Mass-market US stock app, referral-led (2019–21 data) | $15–55 |
  | US robo / digital wealth | $85–130 |
  | Asia online brokers (rising in 2025 as SG and HK competition intensified) | $150–400 |
  | CFD / derivatives | $1,300–1,500 |

- **Why the CAC ranges diverge:**
  1. **Product economics.** CFD revenue per user is ≈$1,500 per *quarter*, against ≈$120–190 per *year* for a stock app.
  2. **Customer value.** Tiger's new funded clients bring ≈$30–60k each, so a CAC of $250–400 is ≈1% of initial net inflow (calc).
  3. **Definitions.** CAC may be fully loaded or paid media only, and the denominator may be gross or net new funded accounts.
  4. **Channel mix.** Referral-heavy models (Robinhood >80% in 2020, Wealthfront >50%) have the lowest CAC.
- **Payback:**
  - Tiger Hong Kong: ~2 quarters (management).
  - Wealthfront: ≈0.5 years of revenue (calc). Fully loaded CAC of $131 against ≈$260 revenue per client, where revenue per client = ~$339M revenue ÷ ~1.3M funded clients (July 2025). The $339M is the headline figure in the MostlyMetrics S-1 breakdown; whether it covers the fiscal year to Jan 2025 or the trailing twelve months to July 2025 was not confirmed. If it is fiscal-year revenue, the July 2025 client count understates revenue per client and so overstates payback.
  - Plus500: revenue per user ÷ acquisition cost ≈ 1.21 (Q1 2024) and ≈ 1.01 (Q3 2024), i.e. about one quarter to repay acquisition cost, assuming new users generate average revenue.
  - Robinhood (illustrative only, periods mismatched): a $15–53 CAC from 2019–21 against 2025 ARPU of $191 per year implies about 1–3.3 months.
- **LTV/CAC (illustrative):** with 95% annual retention (≈20-year expected life) and net revenue retention above 120%, Wealthfront's undiscounted revenue LTV/CAC would be well above 10×. Wealthfront does not disclose such a figure; treat it as an inference only.
- **Referral economics:** the free-stock range of $2.50–225 says nothing about expected cost per referral. Robinhood's stated lever was triggering the reward at bank link, which cut CAC by ~60% in a year.

### Gaps
- CAC by channel (paid, referral, partnership) in dollars: not disclosed by any broker found.
- Robinhood CAC after 2021: not disclosed in the extracts. Gross funded adds are not public.
- eToro and Webull CAC: not found.
- Expected value per free-stock reward (Robinhood's odds table): not retrieved.
- CAC for UK platforms (Freetrade, Moneybox, Nutmeg, Trading 212) and for Public.com, Acorns and Stash: not searched (budget exhausted).
- LTV/CAC disclosed directly by any broker: not found.

---

## 5. Cost-to-serve: support contacts per client, cost per contact, KYC cost per verification, straight-through processing (STP), operating cost per account

### Takeaway
Brokers rarely publish servicing-cost KPIs. The usable anchors are:
- **Robinhood fully loaded operating expense per funded customer:** ≈$78 (2024) → ≈$91 (2025) (calc).
- **Cost per contact (Gartner, 2019, cross-industry):** $8.01 per live contact vs $0.10 for self-service.
- **Vendor list prices for KYC:** $0.80–1.85 per verification.
- **STP proxy (DTCC, US, institutional):** ≈94.5–94.8% of trades affirmed on trade date after the T+1 switch.

No broker publishes contacts per client.

### Cited Findings

| Metric | Value / range | Period | Population / market | Definition / notes | Source | Conf. |
|---|---|---|---|---|---|---|
| Robinhood revenue and operating expenses | Total net revenues **$4.47B** in FY2025 (+52%) vs $2.95B in FY2024. Total operating expenses **$2.38B** (+25%) vs **$1.90B**. Q4 2025 opex $633M (+38%). Q4 2025 ARPU **$191** (+16%; annualised). | FY2024–25 | Robinhood, US | — | [Robinhood FY2025 results](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-fourth-quarter-and-full-year-2025-results); [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/robinhood-closes-out-strong-2025-with-record-q4-revenues-of-1-28-billion/) | A/B |
| Robinhood opex and revenue per funded customer (calc) | Opex per average funded customer ≈ **$78** (FY2024) and ≈ **$91** (FY2025). Revenue per average funded customer ≈ $121 (FY2024) and ≈ $171 (FY2025). | FY2024–25 | Robinhood | Average funded customers taken as the mean of year-start and year-end: FY2024 (23.4M + 25.2M)/2; FY2025 (25.2M + 27.0M)/2. Opex is fully loaded (marketing, stock-based compensation, transaction costs). | Calc from the sources above | calc |
| Webull revenue per funded account (calc) | ≈ **$119** (FY2025 revenue $571M, +46%, ÷ ≈4.8M average funded accounts) | FY2025 | Webull | Average estimated from end-2025 ≈5.0M and the implied end-2024 ≈4.6M | [Finance Magnates](https://www.financemagnates.com/forex/brokers/webull-posts-record-571m-revenue-in-first-year-as-public-company); [Finviz](https://finviz.com/news/332826/webull-bull-reports-2025-revenue-of-571m-46-yoy-growth) | calc |
| Cost per contact by channel | Live channels (phone, chat, email): **$8.01** per contact. Self-service (website, app): **$0.10**. Only 9% of customers fully resolve issues through self-service. | 2019 (older than preferred) | Cross-industry (Gartner poll of service leaders) | — | [Gartner press release, 2019](https://www.gartner.com/en/newsroom/press-releases/2019-09-25-gartner-says-only-9--of-customers-report-solving-thei) | A |
| KYC cost per verification (vendor list prices) | Sumsub Basic **$1.35** per verification ($149/month minimum). Sumsub Compliance **$1.85** (adds AML screening and proof of address). Veriff Essential from **$0.80** ($49/month minimum). | 2025–2026 | Global, self-serve tiers | List prices; enterprise volume pricing is usually negotiated lower | [Sumsub pricing](https://sumsub.com/pricing/); [CostBench: Veriff](https://costbench.com/software/kyc-aml/veriff/); [CostBench: Sumsub](https://costbench.com/software/kyc-aml/sumsub/) | C |
| STP proxy: US same-day affirmation rate | Share of trades affirmed by the 9pm ET trade-date cutoff: 69% (Dec 2023), 73% (Jan 2024), 74.95% (Mar 2024), 83.5% (Apr 2024), **≈94.55%** after the T+1 go-live on 28 May 2024, **94.80%** (Apr 2026). | 2023–2026 | US institutional equities (DTCC) | Institutional post-trade, not retail onboarding or servicing | [DTCC press release](https://www.dtcc.com/press-releases/2024/dtcc-comments-on-industrys-affirmation-progress-with-t1-implementation-one-month-away); [Global Trading](https://www.globaltrading.net/?p=34533); [DTCC Equities by the Numbers](https://www.dtcc.com/equity-trade-volume-insights) | A/B |
| Same-day affirmation by segment, after T+1 | Prime brokers 81% → **98.6%**. Investment-manager auto-affirmation (central matching) 92% → **97.5%**. Custodian or investment-manager self-affirmation 51% → **84.29%**. | Jan 2024 → post-May 2024 | US institutional | — | [Global Trading](https://www.globaltrading.net/?p=34533) | B |
| Profitability of automated digital wealth | Wealthfront: ≈$339M revenue and ≈47% EBITDA margin | 2025 S-1 (fiscal year vs trailing twelve months not confirmed) | Wealthfront, US | Analyst headline figures from the S-1 | [MostlyMetrics](https://www.mostlymetrics.com/p/wealthfront-ipo-s1-breakdown) | B |

### Inferences
- A scaled US mass-market app runs at ≈**$80–90 fully loaded opex per funded customer per year** (2024–25). Against revenue of $171–191 per customer, that is an operating margin of roughly 50%. Customer support is only part of that opex; the split is not disclosed.
- **Contact cost vs revenue:** one live contact (≈$8, Gartner 2019) ≈ 4.7% of Robinhood's 2025 annual revenue per funded customer (calc). A rate of 2–3 contacts per customer per year would consume ~10–15% of revenue (illustrative; contact rate unknown). This is the case for self-service and AI deflection hypotheses.
- **KYC cost is small next to CAC but multiplies through the funnel:**
  - Per passed KYC: $1.35 ÷ (0.60–0.90 completion) ≈ $1.50–2.25.
  - Per funded account: ≈$2.4, using Futu's 57% account → funded ratio (illustrative).
- DTCC affirmation rates measure *institutional* STP. For retail brokers, STP happens mostly inside the firm (automated routing, clearing and account opening) and has no comparable public metric.

### Gaps
- Support contacts per client or per 1,000 active clients: no broker disclosure found. Robinhood S-1 statements on support headcount and contact volumes could not be retrieved.
- Cost per contact specific to brokerage, and newer (2022–2026) cross-industry figures: not found.
- In-house KYC cost per verification at brokers: not found (vendor list prices only).
- Operating cost per account for Schwab, IBKR, Hargreaves Lansdown and AJ Bell: not computed (inputs not retrieved).
- McKinsey, BCG, Oliver Wyman, Deloitte, Accenture and Celent cost-to-serve studies: not reached before the search budget ran out.

---

## 6. Customer satisfaction: NPS benchmarks for brokers and studied correlation with retention or asset flows

### Takeaway
Average NPS for self-directed brokers is low: **7** for the Canadian industry in 2023 (J.D. Power). US DIY investor satisfaction averages **676/1,000**, with leaders around 700 (J.D. Power 2025).

Evidence linking NPS to retention and flows is directional rather than quantified:
- **Bain:** clients who use digital tools score **11–20 points** higher on NPS, and higher-loyalty firms retain customers and assets better.
- **Schwab:** reports all-time-high Client Promoter Scores alongside strong flows.
- **Behavioural proxies:** advocacy shows up as referrals (Wealthfront >50% of new clients referred; Robinhood >80% of 2020 adds via referral/word-of-mouth), which links satisfaction directly to CAC.

### Cited Findings

| Metric | Value / range | Period | Population / market | Definition / notes | Source | Conf. |
|---|---|---|---|---|---|---|
| J.D. Power U.S. Investor Satisfaction, DIY segment | Segment average **676** (1,000-point scale). Vanguard 704, Fidelity 703, T. Rowe Price 691. Sample: 7,876 advised and 3,723 DIY investors, fielded Jan–Dec 2024. Seven dimensions: digital channels, ease of doing business, people, products and services, resolving problems, trust, value for fees. Younger DIY investors are turning to human advice. | 2025 study | US | Satisfaction index, not NPS | [J.D. Power 2025 U.S. Investor Satisfaction Study](https://www.jdpower.com/business/press-releases/2025-us-investor-satisfaction-study); [Business Wire](https://www.businesswire.com/news/home/20250320745594/en) | A |
| Self-directed broker NPS | Industry average NPS **7** (scale −100 to +100). Reasons for switching: fees 30%, products/tools 17%, poor service 13%. | 2023 | Canada, self-directed investors | — | [J.D. Power 2023 Canada study](https://www.jdpower.com/business/press-releases/2023-canada-self-directed-investor-satisfaction-study) | A |
| Schwab Client Promoter Score (CPS) | CPS at **all-time highs** (Winter Business Update, Jan 2025). In 2025: Investor Services CPS **+7 points**, Advisor Services **+5 points**; Forbes best customer service award. | 2024–2025 | Schwab, US | Absolute CPS values not in the extracts | [Schwab Winter Business Update, Jan 2026](https://content.schwab.com/web/retail/public/about-schwab/schwab_winter_business_update_012126.pdf); [Insider Monkey, Schwab Q4 2024 call](https://www.insidermonkey.com/blog/the-charles-schwab-corporation-nyseschw-q4-2024-earnings-call-transcript-1432658/) | A/B |
| Digital use and loyalty (Bain) | Customers who use digital tools to manage their accounts give NPS **11–20 points higher**. Loyalty leaders (USAA, Fidelity, Schwab) are also the most digital and self-serve. Adviser relationships correlate with share of wallet but not with loyalty. Higher-loyalty firms retain customers and assets better. | Year not confirmed | US brokerages | — | [Bain brief](https://www.bain.com/insights/to-earn-greater-loyalty-investment-brokerages-should-think-digital/); [Bain PDF](https://preprodcms.bain.com/contentassets/2ddba60765dd4cb49e9b1c87cb4a9c51/bain_brief_investment_brokerages_should_think_digital.pdf) | B |
| Advocacy as a behavioural proxy (Wealthfront) | > 50% of new clients were referred, and 40% of clients referred at least one person. The S-1 credits high satisfaction for this word-of-mouth growth engine. | FY2024–25 | Wealthfront, US | — | [Wealthfront S-1](https://www.sec.gov/Archives/edgar/data/1524566/000162828025043113/wealthfront-sx1.htm) | A |

### Inferences
- **NPS ranges:** self-directed broker industry averages sit in single digits to low positive values (Canada 2023: 7). Leaders are clearly higher, but no public absolute values were found.
- **What to use in the driver tree:** observable advocacy metrics are a better fit than survey NPS, because they connect directly to CAC. Examples: share of clients who referred (Wealthfront 40%) and share of new clients from referral (50–80%).
- **Satisfaction levers that matter for retention:**
  - Fees and value for money (the #1 switching reason).
  - Ease of doing business and digital self-service (Bain: +11–20 NPS points).
  - Problem resolution. J.D. Power's dimensions put trust, products and services, and people at the base of the investor experience, with ease of doing business just below them.

### Gaps
- No quantified study from 2022–2026 linking broker NPS or satisfaction to retention or asset flows was found. J.D. Power's loyalty statistics and Bain's quantified NPS-to-flows analyses were not retrieved.
- Not retrieved: Schwab's absolute CPS values, the J.D. Power 2026 study, UK platform NPS (e.g., Boring Money) and NICE/Satmetrix brokerage NPS benchmarks.
