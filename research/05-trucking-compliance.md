# 05 — Small US Trucking Carriers (1–20 trucks): Recurring Compliance & Back-Office Paperwork

Research date: 2026-10-03

## Method and evidence caveats (read first)

- **Every WebFetch attempt was blocked by the environment's egress proxy** (capterra.com, softwareadvice.com, g2.com, trustpilot.com, apps.apple.com, thetruckersreport.com, landline.media, mysafetymanager.com, start4truckers.com, thedotdoctor.com). Reddit could not be fetched either ("unable to fetch from www.reddit.com").
- So all evidence below comes from **WebSearch result pages**. The search tool returns titles, URLs and a *machine-written summary* of the page content. **Text shown in quotes is what the search summary attributed to the page. I could not open the page to confirm the exact wording.** Treat the quotes as close paraphrases, not confirmed verbatim text.
- `site:reddit.com` searches returned **no Reddit threads** on any of 4 queries. I have **no Reddit evidence**. I also found no Indie Hackers or HN discussions of this niche.
- Review **counts** below are counts of distinct complaints that surfaced in search summaries. They are not counts of all 1–3 star reviews on each platform, because I could not page through review sites.

## Summary

The niche has real, recurring, legally required work, and people visibly pay humans for it. Managed DOT compliance runs about $49/driver/month at the low end and $100–250/driver/month for full service. Outsourced DQ-file management costs about $30/driver/month, and dispatchers charge 5–12% of gross, with paperwork and factoring submission bundled in. FMCSA enforcement data shows recordkeeping failures are common: missing Clearinghouse queries alone made up 48.4% of Part 382 violations.

The software side, however, is **crowded and priced near zero**:
- IFTA: $14/month (FleetCollect) or $14.90/quarter (ExpressIFTA).
- DQ files: free to $9/driver/month across FleetCollect, DOTDriverFiles, FleetDrive360, CoreCompliance, CDLSuite and Truck Docs AI.
- A wave of 2025–2026 entrants publish heavy SEO content: FleetCollect, SafeRoad Compliance, TruckComplianceHQ, Truck Docs AI, FleetRabbit, HVI, FileFlo, motorcarrier.ai and fasttruckingcompliance.

Owner-operators on TruckersReport mostly say IFTA is a ~30-minute spreadsheet job and "not worth paying" for. **Inference:** a generic "IFTA app" or "DQ file vault" built in 4 weeks would join a commoditized market where price is the main differentiator.

The more defensible gaps I found are narrower:
1. **State weight-distance taxes** (NY HUT, KY KYU, NM, OR, CT) and IRP renewal mileage, built on mileage data carriers already have. Motive users report having to log NY toll miles by hand.
2. **Driver settlements for 3–20 truck fleets.** Both the TruckLogics and TruckingOffice reviews call settlements weak, and settlement spreadsheet templates sell on Etsy.

Neither has strong "I'd pay" evidence yet.

## Top 3 pain points

### 1. Tracking driver qualification files, expirations and Clearinghouse queries (multi-driver carriers)
- **Description:** Each driver needs a DQ file with documents on different expiry cycles: medical card, annual MVR review, annual Clearinghouse query, application, and prior-employer inquiries. A missed date means a violation, and no small-carrier exemption applies.
- **Evidence:**
  - Clearinghouse query failures: "Failure to conduct required pre-employment and annual queries accounted for 5,682 violations, or 48.4% of the Part 382 total" (search summary). Sources: https://uscomplianceservices.org/what-carriers-are-getting-wrong-in-2026/ and https://saferoadcompliance.com/blog/drug-alcohol-violations-49-cfr-part-382-guide/
  - Incomplete DQ files are cited as a top new-entrant audit failure: https://www.mysafetymanager.com/new-entrant-audit/ , https://truckcompliancehq.com/blog/fmcsa-new-entrant-safety-audit , https://innovativelogisticsgroup.io/compliance-and-safety/how-to-pass-the-fmcsa-new-entrant-safety-audit-the-four-file-system-and-automatic-fail-sweep-that-protect-your-authority-in-the-first-12-months/
  - Paid outsourcing exists:
    - DotFleet Compliance: $30/driver/month for outsourced DQF management. https://www.dotfleetcompliance.com/
    - My Safety Manager: $49/driver/month. https://www.mysafetymanager.com/driver-qualification-file-cost/
    - A third-party provider charges $199/driver setup plus a $159 renewal (same search result set).
  - Clearinghouse II (Nov 18, 2024): states must downgrade the CDLs of drivers in "prohibited" status. Over 178,000 drivers were in prohibited status as of Oct 1, 2024. https://www.ttnews.com/articles/new-fmcsa-clearinghouse-ii , https://csa.fmcsa.dot.gov/WhatsNew/Article?articleId=696370
  - New 2025–26 driver-eligibility rules add hiring checks:
    - English-proficiency out-of-service enforcement since June 25, 2025. https://www.fmcsa.dot.gov/regulations/federal-register-documents/2026-16288
    - Non-domiciled CDL final rule, Feb 2026. https://www.freightwaves.com/news/fmcsa-final-rule-and-dalilahs-law-target-cdl-eligibility-what-trucking-needs-to-know
- **Counter-evidence:** FMCSA ran about 12,300 compliance reviews in 2024 against roughly 800,000 active carriers (about 1.5%). The source frames this as "a carrier could operate for 65 years before facing a comprehensive audit." https://www.freightwaves.com/news/fmcsa-counts-inspections-nobody-counts-compliance . **Inference:** low audit odds weaken urgency for established carriers. New entrants, who face a mandatory 12-month safety audit, feel it most.
- **Frequency:** recurring per driver, annually or on each document's expiry; per hire for onboarding. Owner-operators with zero employees have a file only on themselves.
- **Who feels it / who pays:** the owner, or an office manager or spouse, at 2–20 truck carriers. The owner controls the budget.
- **Current workaround cost:** $30–49/driver/month outsourced, or $0–9/driver/month software, or owner time. Exact time costs are not sourced.

### 2. IFTA: reconciling miles by state with fuel purchases each quarter
- **Description:** Every quarter, carriers must combine miles by jurisdiction (from an ELD, GPS or paper log) with fuel receipts or fuel-card data, then file in their base state. Filings are due Apr 30, Jul 31, Oct 31 and Jan 31.
- **Evidence:**
  - TruckersReport thread titled "What's a good way to track IFTA is there a application??" One poster says they "keep track of my miles per state each day and keep a spread sheet on my tablet" (search summary). https://www.thetruckersreport.com/truckingindustryforum/threads/what%E2%80%99s-a-good-way-to-track-ifta-is-there-a-application.1541966/
  - "Anyone have a good program or spreadsheet for ifta/irp miles?" (multi-page thread). https://www.thetruckersreport.com/truckingindustryforum/threads/anyone-have-a-good-program-or-spreadsheet-for-ifta-irp-miles.332629/page-3
  - Paid help on forums: one agent quoted "$50 to file a simple form and $150 per quarter" and the poster felt it was overpriced; another poster paid "about $11 a month" (search summary). https://www.thetruckersreport.com/truckingindustryforum/threads/ifta-per-quarter-question-for-owner-operator-carrier-with-few-trucks.163265/ , https://www.thetruckersreport.com/truckingindustryforum/threads/new-owner-operator-ifta-question.149591/
  - Motive (Capterra): IFTA reports "do not break down toll miles vs regular road miles for New York State toll roads … drivers still have to manually keep a written record of toll miles." Another review: "Problem in calculating distance travelled by vehicle in case of IFTA filing." https://www.capterra.com/p/138669/Motive/reviews/ (could not fetch; via search summary). Motive's help center confirms that reports give jurisdiction totals only. https://helpcenter.gomotive.com/hc/en-us/articles/31101012037277-IFTA
  - TruckLogics (review via search): "has an IFTA function, but the program lags more than often during those times." https://www.capterra.com/p/136780/TruckLogics/reviews/
  - Paid spreadsheet products exist: Etsy IFTA and bookkeeping templates https://www.etsy.com/listing/4444974073/owner-operator-trucking-bookkeeping and DieselBoss's IFTA Excel product https://www.dieselboss.com/software/ifta.html
- **Counter-evidence:** the forum consensus summarized by search is that IFTA is "simple," takes "about 30 minutes," and that "paying someone … isn't worth it." Market prices are very low: $14/month (FleetCollect), $14.90/quarter (ExpressIFTA), $25/quarter (Permits Plus), from $10/truck (DOT Doctor). https://fleetcollect.net/ifta , https://www.permitsplus.com/iftaCalculator/ , https://thedotdoctor.com/quarterly_ifta_filing
- **Frequency:** quarterly, for every interstate carrier over 26,000 lbs.
- **Who feels it / who pays:** the owner-operator personally. Budget tolerance appears to be about $5–15/month (inference from market prices and forum sentiment).
- **Current workaround cost:** about 30 minutes to a few hours per quarter, plus $0–15/month for software or $25–150/quarter for a human service.

### 3. Weekly driver settlements and load paperwork (3–20 truck fleets)
- **Description:** Every week, fleets compute each driver's pay (per mile, percentage or flat) with accessorials and deductions, and produce a statement. A separate stream of load paperwork (rate confirmation, BOL, POD, invoice) goes to the factoring company.
- **Evidence:**
  - TruckLogics reviews (search summary): "Lacks a lot on the driver settlement end"; "does not track YTD Gross on the settlement statements"; "all loads and dispatches entered disappeared from the system without warning." https://www.capterra.com/p/136780/TruckLogics/reviews/
  - TruckingOffice: "driver settlement statements … do not provide a comprehensive breakdown of load payments"; no QuickBooks integration; "significant manual data entry." https://www.selecthub.com/p/trucking-software/truckingoffice/
  - TruckersReport "Settlement Software" thread: https://www.thetruckersreport.com/truckingindustryforum/threads/settlement-software.292165/
  - Settlement Excel templates sold on Etsy: https://www.etsy.com/market/trucking_settlement_excel_template
  - Free templates offered as lead magnets by TMS vendors: https://www.torotms.com/blog/free-truck-driver-settlement-sheet-template , https://fleetlegend.com/blog/owner-operator-settlement-template
  - Vendor claim (marketing, so weak): settlements "routinely take a full day or more of office time every week." https://www.fleetiveapp.com/guides/driver-settlements/
  - Paid labor: dispatchers charge 5–10% of gross, and up to 12% when they handle paperwork, invoicing and broker setup. Hidden fees include "paperwork processing fees ($5–15 per load)." https://idispatchhub.com/truck-dispatcher-fees/ , https://freightgirlz.com/truck-dispatcher-rates-2025/ , https://truckleap.com/dispatch/pricing
- **Frequency:** weekly.
- **Who feels it / who pays:** the owner or office manager at fleets with hired drivers (not solo owner-operators), and drivers who dispute their checks. The owner controls the budget.
- **Current workaround cost:** spreadsheets plus office hours. Bundled TMS from about $20/month (TruckingOffice) up to dispatch-service percentages.

## Review-mining table

Search summaries only. Pages were not fetched, so counts are a lower bound of what surfaced.

| Cluster | Tools | Count (surfaced) | Quotes (search-summary wording) + links |
|---|---|---|---|
| Contract lock-in and billing disputes | Motive | 3 | "no way to get out of a 3-year contract without continuing to pay"; double billed "over a year later and was refused refunds"; "charging more than committed." https://www.capterra.com/p/138669/Motive/reviews/ , https://www.truckingway.com/motive-eld-review/ |
| IFTA data accuracy and gaps | Motive, TruckLogics | 4 | NY toll miles must be logged "manually"; "Not very accurate"; "Problem in calculating distance travelled… IFTA filing"; TruckLogics IFTA "lags." https://www.capterra.com/p/138669/Motive/reviews/ , https://www.capterra.com/p/136780/TruckLogics/reviews/ |
| Reliability and data loss | TruckLogics, Motive | 3 | loads and dispatches "disappeared from the system without warning"; "app crashes a lot"; ELD "records drive time when parked." https://www.capterra.com/p/136780/TruckLogics/reviews/ , https://www.capterra.com/p/138669/Motive/reviews/ |
| Slow or uninformed support | TruckLogics, Motive | 3 | support "very slow to respond and sometimes unfamiliar with their own software"; Motive "say there's nothing they could do." Same URLs as above. |
| Weak settlements and payroll | TruckLogics, TruckingOffice, Rigbooks | 4 | "Lacks a lot on the driver settlement end"; no YTD gross; TruckingOffice statements lack a breakdown; Rigbooks has "no built-in payroll module." https://www.capterra.com/p/136780/TruckLogics/reviews/ , https://www.selecthub.com/p/trucking-software/truckingoffice/ , https://fitsmallbusiness.com/rigbooks-review/ |
| Manual entry, no integrations, dated UI | TruckingOffice, J.J. Keller | 4 | "significant manual data entry"; no QuickBooks integration; no mobile app; J.J. Keller Encompass is "dated feeling" with "confusing and complicated pricing." https://www.selecthub.com/p/trucking-software/truckingoffice/ , https://ratings.freightwaves.com/reviews/j-j-keller-elog/ , https://fleetlogging.com/jj-keller/ |
| Pricing and scale limits | Rigbooks, J.J. Keller | 2 | Rigbooks needs "special pricing for fleets over 10 trucks"; J.J. Keller adds a $3.50 extra-driver fee and locks features behind the Platinum tier. https://fitsmallbusiness.com/rigbooks-review/ , https://fleetlogging.com/jj-keller/ |

I could not locate an ExpressIFTA Trustpilot page; search returned none. ExpressIFTA was acquired by TruckLogics and merged into it in March 2022 (https://www.crunchbase.com/organization/expressifta), so its reviews now fall under TruckLogics.

## Paid-labor findings

| Service | Price | Source |
|---|---|---|
| Fiverr: FMCSA/USDOT setup plus IFTA filing gig | $45 | https://www.fiverr.com/xanderkimin/provide-expert-fmcsa-compliance-usdot-mc-number-setup-and-ifta-filing |
| IFTA quarterly filing services | $30–100/quarter typical; Permits Plus $25/quarter; DOT Doctor from $10/truck | https://fleetrabbit.com/blogs/post/ifta-reporting-owner-operators , https://www.permitsplus.com/iftaCalculator/ , https://thedotdoctor.com/quarterly_ifta_filing |
| Forum-reported agent prices | "$50 … simple form and $150 per quarter" (seen as overpriced); "about $11 a month" | TruckersReport threads above |
| Managed DOT compliance (MCS-150, UCR, IFTA, drug pool, DQ, IRP, 2290) | $49/driver/month (My Safety Manager); $50–100 basic and $100–250 full service per driver/month; a 5-truck fleet pays about $500–1,250/month | https://www.mysafetymanager.com/ , https://movingauthority.com/dot-compliance-services-pricing/ , https://start4truckers.com/services/ongoing-dot-compliance/ |
| Outsourced DQF | $30/driver/month; $199 setup plus $159/year renewal | https://www.dotfleetcompliance.com/ , https://www.mysafetymanager.com/driver-qualification-file-cost/ |
| Weight-distance tax permits (NY HUT, KYU, NM, CT, OR) | $75 per state permit; $149 "Big Four" bundle | https://www.fastpermitfiling.com/ |
| UCR third-party "filers" | "2–3x what it would cost you to file it yourself"; OOIDA warns of predatory notices | https://landline.media/ucr-fee-season-pay-the-fund-not-the-hustlers/ , https://landline.media/ooida-beware-of-predatory-ucr-fee-collection-schemes/ |
| Dispatch with paperwork and factoring submission | 5–12% of gross; $5–15/load paperwork fees | https://idispatchhub.com/truck-dispatcher-fees/ , https://freightgirlz.com/truck-dispatcher-rates-2025/ |
| Trucking bookkeepers (IFTA, settlements) | $19–33/hour (ZipRecruiter listing range) | https://www.ziprecruiter.com/Jobs/Trucking-Company-Bookkeeper |
| Form 2290 e-file | $14.90 for 1 vehicle; $44.90 for 3–24 vehicles | https://www.expresstrucktax.com/pricing/ |

**Inference:** the strongest willingness to pay is for *bundled done-for-you compliance* ($49–250/driver/month), not for single-form software. UCR scam-filers profiting from carriers' confusion about what is due and when show that a trustworthy "what's due, and is it already paid?" signal has value.

## Workaround findings

- **Spreadsheets for IFTA and IRP miles:** several TruckersReport threads (links in Pain #2), including a member who shared an Excel IFTA template with locked cells. https://www.thetruckersreport.com/truckingindustryforum/threads/anyone-have-a-good-program-or-spreadsheet-for-ifta-irp-miles.332629/page-3
- **Paid spreadsheets:** Etsy sells owner-operator bookkeeping, IFTA and settlement templates (links above), and DieselBoss sells an IFTA Excel product.
- **Paper or spreadsheet reminders for annual inspections (§396.17):** described as a cause of the second-most-common vehicle maintenance violation (12 CSA points). This source is a vendor blog, so treat it as weak. https://saferoadcompliance.com/blog/dot-vehicle-maintenance-violations/ , https://heavyvehicleinspection.com/blog/post/annual-dot-inspection-guide-2026
- **Handwritten NY toll-mile logs** alongside Motive (Pain #2).
- **Not found:** no explicit "I'd pay for this" quote, and no Reddit, Indie Hackers or HN threads, because Reddit was unreachable and not indexed by search.

## Recent regulatory changes (2024–2026)

| Change | Status | Source |
|---|---|---|
| Clearinghouse II: CDL downgrade for prohibited drivers | In force since Nov 18, 2024 | https://www.ttnews.com/articles/new-fmcsa-clearinghouse-ii |
| English-language-proficiency out-of-service enforcement | Since Jun 25, 2025; 12,308 OOS violations in H2 2025 (search summary) | https://www.fmcsa.dot.gov/regulations/federal-register-documents/2026-16288 , https://otrsolutions.com/blog/new-trucking-laws-in-2025-what-drivers-and-fleets-need-to-know |
| Non-domiciled CDL restrictions | Final rule Feb 2026 | https://www.freightwaves.com/news/fmcsa-final-rule-and-dalilahs-law-target-cdl-eligibility-what-trucking-needs-to-know |
| ELD revocations (79 removed since Jan 2025; 60 days to replace) | Ongoing | https://www.truckinginfo.com/news/fmcsa-stop-using-these-15-electronic-logging-devices , https://eld.fmcsa.dot.gov/File/OpenKey/ELD_Removals_Sep_4_2025 |
| MC number elimination (URS) | **Contradictory sources.** Some say it was retired Oct 1, 2025; others say it was delayed and not finalized as of May 2026. Treat as unresolved. | https://www.freightwaves.com/news/what-it-means-for-the-industry-as-fmcsa-eliminates-mc-numbers-in-2025 , https://tiproservices.com/articles/fmcsa-reverses-mc-plans , https://www.foley.io/articles/mc-numbers-eliminated-what-this-means-for-your-business |

## Competitors

| Name | Pricing (as surfaced) | Segment | Weaknesses (sourced) | Source |
|---|---|---|---|---|
| TruckLogics (includes ExpressIFTA) | ExpressIFTA $14.90/quarter | Owner-operators and small fleet TMS | Data loss, crashes, slow support, weak settlements | https://www.capterra.com/p/136780/TruckLogics/reviews/ , https://www.expressifta.com/ |
| TruckingOffice | About $20/month | 1–20 trucks moving off spreadsheets | Manual entry, no QuickBooks integration, no mobile app, dated UI | https://www.selecthub.com/p/trucking-software/truckingoffice/ , https://www.datatruck.io/blog/trucking-compliance-software |
| Rigbooks | Not surfaced | Owner-operator bookkeeping | No payroll, special pricing over 10 trucks, limited invoice customization | https://fitsmallbusiness.com/rigbooks-review/ |
| Motive | About $35/vehicle/month plus hardware; 3-year contracts | ELD/telematics | Lock-in, billing disputes, IFTA gaps (NY toll miles) | https://www.truckingway.com/motive-eld-review/ , https://fleetcollect.net/blog/best-ifta-software-comparison |
| Samsara | $27–33/vehicle/month; 3-year minimum; $99–148 hardware | Telematics | Cost and contract terms are heavy for 1–5 trucks (inference) | https://fleetcollect.net/blog/best-ifta-software-comparison |
| J.J. Keller Encompass | Tiered; $3.50/month per extra driver | Small and mid fleets, compliance | Dated UI, confusing pricing, features locked to Platinum | https://fleetlogging.com/jj-keller/ , https://ratings.freightwaves.com/reviews/j-j-keller-elog/ |
| FleetCollect | IFTA $14/month solo, $19/month for 2–5; DQF free tier, $39–59/month or $7/driver | New entrant; IFTA, DQF and IRP content | No independent reviews found; its own blog is the source of most comparisons (bias) | https://fleetcollect.net/ifta , https://fleetcollect.net/ |
| DOTDriverFiles / FleetDrive360 / CoreCompliance / CDLSuite / Truck Docs AI / FileFlo | About $5–9/driver/month (DOTDriverFiles, FleetDrive360); others not surfaced | DQF software | Crowded; differentiation unclear | https://dotdriverfiles.com/ , https://www.fleetdrive360.com/pricing/ , https://corecompliance.io/pricing , https://www.capterra.com/p/10039100/Truck-Docs-AI/ , https://www.getfileflo.com/blog/best-dqf-management-software-2026 |
| My Fuel Tax (Road Tax Upgrade) | Not surfaced | IFTA plus NY HUT, KYU, NM and OR returns from the same miles | Possibly the only tool explicitly covering weight-distance returns | https://myfueltax.net/new-york-hut-report/ |
| My Safety Manager, DotFleet, Start4Truckers, DOT Doctor (services) | $30–49/driver/month; $10+/truck IFTA | Done-for-you compliance | Human-labor cost; quality unverified | Links in the paid-labor table |

**Ignored or thin segments (inference):**
1. Weight-distance tax returns (NY/KY/NM/OR/CT) generated from data a carrier already holds in its ELD or IFTA tool. Only My Fuel Tax surfaced as covering these.
2. IRP renewal mileage packages built from four quarters of IFTA data.
3. A cross-filing "compliance calendar plus verification" view: what is due for UCR, 2290, MCS-150, IRP, annual inspections, medical cards and Clearinghouse queries, and whether each is already done. This would counter the UCR scam-notice problem.
4. Settlements for 3–20 truck fleets that already have an ELD and factoring but no full TMS.

## Confidence rating: **Low–Medium**

- **Why not higher:**
  - Every page fetch was blocked, so quotes are search-engine summaries, not verified verbatim text, and review counts are small and partial.
  - No Reddit, Indie Hackers or HN evidence was found.
  - Many sources are vendor blogs with an incentive to inflate pain (FleetCollect, SafeRoad, HVI, Fleetive).
  - The MC-number status is contradictory across sources.
- **What is reasonably solid:**
  - Pricing of human compliance services and of incumbent software is consistent across several sources.
  - FMCSA rule changes are confirmed via fmcsa.dot.gov and trade press (TT News, FreightWaves).
  - The Motive NY toll-mile gap is corroborated by Motive's own help center.
  - The forum-wide sentiment that IFTA alone is low-WTP is consistent.
- **Key inference for the goal:** a solo dev's 4-week product should avoid generic IFTA or DQ-vault software, which is a race to the bottom. The best leads to validate next, ideally by interviewing 10 small-fleet owners, are weight-distance and IRP filings derived from existing ELD exports, and settlements for 3–20 truck fleets.

## Sources

- https://www.capterra.com/p/136780/TruckLogics/reviews/ (fetch blocked; search summary only)
- https://www.capterra.com/p/138669/Motive/reviews/ (fetch blocked; search summary only)
- https://capterra.com/p/122284/TruckingOffice/reviews/ (fetch blocked)
- https://www.selecthub.com/p/trucking-software/truckingoffice/
- https://fitsmallbusiness.com/rigbooks-review/
- https://www.truckingway.com/motive-eld-review/
- https://ratings.freightwaves.com/reviews/j-j-keller-elog/
- https://fleetlogging.com/jj-keller/
- https://helpcenter.gomotive.com/hc/en-us/articles/31101012037277-IFTA
- https://www.crunchbase.com/organization/expressifta
- https://www.expressifta.com/
- https://www.thetruckersreport.com/truckingindustryforum/threads/what%E2%80%99s-a-good-way-to-track-ifta-is-there-a-application.1541966/ (fetch blocked)
- https://www.thetruckersreport.com/truckingindustryforum/threads/anyone-have-a-good-program-or-spreadsheet-for-ifta-irp-miles.332629/page-3
- https://www.thetruckersreport.com/truckingindustryforum/threads/ifta-per-quarter-question-for-owner-operator-carrier-with-few-trucks.163265/ (fetch blocked)
- https://www.thetruckersreport.com/truckingindustryforum/threads/new-owner-operator-ifta-question.149591/
- https://www.thetruckersreport.com/truckingindustryforum/threads/settlement-software.292165/
- https://www.etsy.com/listing/4444974073/owner-operator-trucking-bookkeeping
- https://www.etsy.com/market/trucking_settlement_excel_template
- https://www.dieselboss.com/software/ifta.html
- https://www.torotms.com/blog/free-truck-driver-settlement-sheet-template
- https://fleetlegend.com/blog/owner-operator-settlement-template
- https://www.fleetiveapp.com/guides/driver-settlements/
- https://www.fiverr.com/xanderkimin/provide-expert-fmcsa-compliance-usdot-mc-number-setup-and-ifta-filing
- https://fleetrabbit.com/blogs/post/ifta-reporting-owner-operators
- https://www.permitsplus.com/iftaCalculator/
- https://thedotdoctor.com/quarterly_ifta_filing (fetch blocked)
- https://start4truckers.com/services/ongoing-dot-compliance/ (fetch blocked)
- https://www.mysafetymanager.com/ and https://www.mysafetymanager.com/driver-qualification-file-cost/ (fetch blocked)
- https://www.mysafetymanager.com/new-entrant-audit/
- https://movingauthority.com/dot-compliance-services-pricing/
- https://www.dotfleetcompliance.com/
- https://dotdriverfiles.com/
- https://www.fleetdrive360.com/pricing/
- https://corecompliance.io/pricing
- https://www.capterra.com/p/10039100/Truck-Docs-AI/
- https://www.getfileflo.com/blog/best-dqf-management-software-2026
- https://fleetcollect.net/ifta
- https://fleetcollect.net/
- https://fleetcollect.net/blog/best-ifta-software-comparison
- https://www.datatruck.io/blog/trucking-compliance-software
- https://myfueltax.net/new-york-hut-report/
- https://www.fastpermitfiling.com/
- https://www.apexcapitalcorp.com/blog/four-states-with-additional-registration-requirements-for-truckers/
- https://www.expresstrucktax.com/pricing/
- https://landline.media/ucr-fee-season-pay-the-fund-not-the-hustlers/ (fetch blocked)
- https://landline.media/ooida-beware-of-predatory-ucr-fee-collection-schemes/
- https://idispatchhub.com/truck-dispatcher-fees/
- https://freightgirlz.com/truck-dispatcher-rates-2025/
- https://truckleap.com/dispatch/pricing
- https://www.ziprecruiter.com/Jobs/Trucking-Company-Bookkeeper
- https://uscomplianceservices.org/what-carriers-are-getting-wrong-in-2026/
- https://saferoadcompliance.com/blog/drug-alcohol-violations-49-cfr-part-382-guide/
- https://saferoadcompliance.com/blog/dot-vehicle-maintenance-violations/
- https://heavyvehicleinspection.com/blog/post/annual-dot-inspection-guide-2026
- https://truckcompliancehq.com/blog/fmcsa-new-entrant-safety-audit
- https://innovativelogisticsgroup.io/compliance-and-safety/how-to-pass-the-fmcsa-new-entrant-safety-audit-the-four-file-system-and-automatic-fail-sweep-that-protect-your-authority-in-the-first-12-months/
- https://www.freightwaves.com/news/fmcsa-counts-inspections-nobody-counts-compliance
- https://www.ttnews.com/articles/new-fmcsa-clearinghouse-ii
- https://csa.fmcsa.dot.gov/WhatsNew/Article?articleId=696370
- https://www.fmcsa.dot.gov/regulations/federal-register-documents/2026-16288
- https://otrsolutions.com/blog/new-trucking-laws-in-2025-what-drivers-and-fleets-need-to-know
- https://www.freightwaves.com/news/fmcsa-final-rule-and-dalilahs-law-target-cdl-eligibility-what-trucking-needs-to-know
- https://www.truckinginfo.com/news/fmcsa-stop-using-these-15-electronic-logging-devices
- https://eld.fmcsa.dot.gov/File/OpenKey/ELD_Removals_Sep_4_2025
- https://www.freightwaves.com/news/what-it-means-for-the-industry-as-fmcsa-eliminates-mc-numbers-in-2025
- https://tiproservices.com/articles/fmcsa-reverses-mc-plans
- https://www.foley.io/articles/mc-numbers-eliminated-what-this-means-for-your-business
