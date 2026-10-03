# 04 — STR Host Compliance (permits, registration, lodging tax) + adjacent ops

Research date: 2026-10-03. Niche: short-term rental hosts and small operators (1–30 units), US focus, with notes on EU registration.

## Method and evidence limits (read first)

- **WebFetch was blocked for every target domain** I tried: biggerpockets.com, community.withairbnb.com, strspecialist.com, trustpilot.com, capterra.com, and reddit.com. **WebSearch also refuses reddit.com.** No page in this report was opened directly.
- All evidence comes from **WebSearch result summaries**, meaning the search engine's paraphrase of each page. Text in quotation marks below is that summary wording. **Treat it as a paraphrase, not a verified verbatim user quote.** Every URL below appeared in a search result.
- **I could not count 1–3 star reviews**, because review pages could not be loaded. The review-mining table counts *distinct complaint mentions in search summaries*, not review totals.
- The session's web-search budget ran out before the Spain NRA (gestoría pricing) and Upwork job-post searches finished.
- Anything I inferred is labelled **(inference)**.

## Summary

There are real signals that people pay for STR compliance work. The clearest are **human services that file lodging tax every month for a recurring fee**:

- Vacation Home Help charges $25/mo plus $250 setup per property.
- A Maui bookkeeper charges $82.50–$150/mo for GET/TAT filing.
- STRpermit.com charges $360–$4,800 per Portland permit application, plus $260/hr consulting.
- Boost Rentals charges a $1,000 flat fee for permitting.

New rules keep adding work:

- Houston registration took effect 2026-01-01, with platform delisting from 2026-07-01.
- Connecticut requires DRS registration by 2027-01-01.
- EU Regulation 2024/1028 has applied since 2026-05-20.
- Spain's NRA has required a registration number on listings since 2025-07.

However, **the "permit/renewal tracker + rule-change alert" idea, the obvious build for a solo developer, is already crowded with cheap indie products.** At least eight exist: STR Comply, HostShield, PermitPath, PermitWise, RentPermit, STR Alert, STRWatch and STR Rule Watch. Prices run **$10–$40/mo**, and they compete hard on SEO (STR Comply publishes "alternatives to X" pages for its rivals). (Inference: the low price ceiling and the crowding suggest the alert/tracker layer is close to a commodity, and none of these products shows public evidence of traction.)

The most defensible gap is the work between "Airbnb collected some of the tax" and "the host files the rest":

- **Lodging tax return preparation for jurisdictions the platform does *not* remit**, using CSVs from Airbnb/Vrbo/PMS.
- This sits between Avalara MyLodgeTax at about $20–$27/property/mo plus setup, with no PMS integration according to TIDY's comparison, and human filers at $25–$150/mo.
- **Co-host owner statements** are a secondary adjacent pain. PMS tools have added the feature, so the evidence there is weaker.

## Top 3 pain points

### 1. Filing local lodging/occupancy tax that the platforms do not remit (multi-jurisdiction, monthly)

- **Description:** Airbnb remits in some jurisdictions only. It sometimes collects the state rate and leaves city and county to the host. Hosts then file monthly, quarterly or annually with separate state, county and city agencies on different schedules. Some must file zero returns. In Florida, TDT goes to the county *or* the DOR depending on the county, and is reported on a different line of the return.
- **Evidence:**
  - Airbnb collects only in select areas; hosts file the rest. [Airbnb help 2309](https://www.airbnb.com/help/article/2309), [Airbnb help 2596](https://www.airbnb.com/help/article/2596)
  - Airbnb "collects the state rate and leaves the city and county rate to you"; state is due quarterly while the city is due monthly. [rakidzich.com occupancy tax 2026](https://www.rakidzich.com/articles/occupancy-tax-airbnb-host-collect-2026), [Avalara Airbnb occupancy tax guide](https://www.avalara.com/mylodgetax/en/resources/airbnb-occupancy-tax-guide.html)
  - Airbnb Community hosts describe Excel sheets for returns, monthly county forms "even if they have zero rent", and Texas counties Airbnb doesn't collect for. [Local Occupancy Taxes in Texas](https://community.withairbnb.com/t5/Help-with-your-business/Local-Occupancy-Taxes-in-Texas/m-p/2105046), [Hotel Occupancy Tax](https://community.withairbnb.com/t5/Help-with-your-business/Hotel-Occupancy-Tax/m-p/1841029), [Determining exact breakdown of Occupancy Taxes](https://community.withairbnb.com/t5/Help-with-your-business/Determining-the-exact-breakdown-of-Occupancy-Taxes-on-a-city/m-p/1825369), [Florida Sales Tax Tutorial (host-written guide)](https://community.withairbnb.com/t5/Host-guides/Florida-Sales-Tax-Tutorial-Revised-April-2024/m-p/1919540)
  - Florida county vs. DOR split. [FL DR-15TDT](https://floridarevenue.com/Forms_library/current/dr15tdt.pdf), [syncgtm line-D explainer](https://syncgtm.com/blog/on-what-line-do-i-report-tourist-development-tax-on-the-florida-sales-tax-return)
  - BiggerPockets threads asking whether paying for this is worth it. [Avalara for Lodging Tax](https://www.biggerpockets.com/forums/530/topics/1074473-avalara-for-lodging-tax), [MyLodgeTax worth it?](https://www.biggerpockets.com/forums/530/topics/1100417-wwwmylodgetaxcom-worth-it), [Miami MyLodgeTax worth it?](https://www.biggerpockets.com/forums/530/topics/751499-anybody-use-avalara-mylodgetax-in-miami-worth-it), [Lodging tax payment service thread](https://www.biggerpockets.com/forums/530/topics/715020-short-term-airbnb-vrbo-occupancy-lodging-tax-payment-service)
- **Frequency estimate:** monthly per jurisdiction for most hosts in non-remitting areas. Avalara says most agencies require monthly filing. (Inference: 12–36 returns a year per property in a stacked jurisdiction.)
- **Who feels the pain:** self-managing hosts and small operators in non-remitting jurisdictions (Florida counties, Texas counties, Hawaii, some Colorado/California cities).
- **Who controls the budget:** the owner-operator, who is the same person.
- **Current cost of the workaround:**
  - Avalara about $20–$27/property/mo plus $50–$299 setup (sources disagree, see the competitors table).
  - Human filers $25–$150/mo.
  - Doing it yourself: a spreadsheet plus agency portals.
  - A BiggerPockets-derived summary frames the break-even as "2+ hours of filing time per quarter" ([koohost summary of BP views](https://app.koohost.ai/blog/vacation-rental-tax-software)).

### 2. Permit / registration renewals and rule changes across cities

- **Description:**
  - Permits expire on a 1- or 2-year cycle, and cities often send only a mailed notice.
  - A lapsed permit invalidates the registration number, and platforms then delist the listing.
  - Fines can be per day.
  - New ordinances keep arriving: Houston 2026, Connecticut 2027, Minnetonka 2026.
- **Evidence:**
  - BiggerPockets thread "How are you guys tracking permit renewals and TOT changes across multiple cities?". The summary reports "giant spreadsheets and calendar reminders", mailed renewal notices, fines of "$500 to $1,000+ per violation", and tracking TOT rate changes "feels like a part-time job". [BP thread 1281391](https://www.biggerpockets.com/forums/517/topics/1281391-how-are-you-guys-tracking-permit-renewals-and-tot-changes-across-multiple-cities)
  - Lapse leads to an invalid number and automatic delisting; per-day fines are up to $2,000 in LA and $1,000–$2,000 in Austin. [beancount.io registration guide 2026](https://beancount.io/blog/2026/07/13/short-term-rental-registration-licensing-compliance-guide), [Airbnb help 3748](https://airbnb.com/help/article/3748)
  - Houston: annual registration of $275 per property; platform delisting within 10 days from 2026-07-01. [gowithsurge Houston](https://www.gowithsurge.com/blog/houston-short-term-rental-laws), [rentpermit Houston guide](https://www.rentpermit.com/blog/houston-rental-permit.html)
  - Connecticut DRS registration by 2027-01-01. [CT HB 5536](https://cga.ct.gov/2026/FC/PDF/2026HB-05536-R000669-FC.PDF)
  - Minnetonka ordinance. [Minnetonka](https://www.minnetonkamatters.com/short-term-rental-ordinance)
  - Government fee examples: Austin $836.30, San Bernardino County $1,144, Nashville $313. [Austin](https://www.austintexas.gov/development-services/short-term-rentals), [SB County](https://str.sbcounty.gov/getting-started/), [Nashville FAQ](https://www.nashville.gov/departments/codes/short-term-rentals/frequently-asked-questions)
- **Frequency estimate:** a renewal event once every 1–2 years per property per jurisdiction, plus ad hoc ordinance changes. It is low-frequency but high-consequence.
- **Who feels the pain:** multi-city operators (5–30 units). Single-city hosts said calendar reminders suffice (per the BP summary).
- **Who controls the budget:** the owner-operator or the PM company.
- **Current cost of the workaround:**
  - A spreadsheet plus calendar (free).
  - Tracker SaaS at $10–$40/mo.
  - Permit expediters at $360–$4,800 per application or $1,000 flat.

### 3. Co-host / small-PM owner statements and payout splits (adjacent ops)

- **Description:** Co-hosts must produce monthly per-owner statements covering gross revenue, platform fees, the co-host's cut, and expenses such as cleaning. Airbnb's native co-host payouts complicate reconciliation and 1099-K double reporting.
- **Evidence:**
  - OwnerRez owner statements are "not very robust", with "plenty of work arounds". [stayfi OwnerRez review](https://stayfi.com/vrm-insider/2025/10/28/ownerrez-review/)
  - OwnerRez forum threads exist on [owner statements](https://www.ownerrez.com/forums/general-help/owner-statements) and [monthly statements](https://www.ownerrez.com/forums/general-help/monthly-statements).
  - Hospitable shipped co-host owner statements in response, a signal that customers demanded it. [Hospitable changelog](https://community.hospitable.com/hospitable-changelog-3/owner-statements-and-invoices-for-airbnb-co-hosts-are-here-370)
  - Spreadsheet templates are being marketed. [rakidzich owner statement template](https://www.rakidzich.com/articles/airbnb-owner-statement-template)
  - 1099-K double reporting for co-hosts. [beancount.io co-host 1099-K](https://beancount.io/blog/2026/08/23/short-term-rental-co-host-1099k-double-reporting-reconciliation-bookkeeping-guide), [Airbnb Community co-host double tax](https://community.withairbnb.com/t5/Ask-about-your-listing/Is-Airbnb-double-taxing-co-host-payouts/m-p/2052032)
  - A dedicated tool already exists. [MagicBNB](https://magicbnb.io/)
- **Frequency estimate:** monthly per owner.
- **Who feels the pain:** co-hosts managing 2–20 units for other owners.
- **Who controls the budget:** the co-host, who is the user.
- **Current cost of the workaround:**
  - OwnerRez about $130–$150/mo for 5 properties ([magicbnb small-portfolio comparison](https://magicbnb.io/blog/best-airbnb-management-software-small-portfolios-2026)).
  - QuickBooks plus spreadsheets.
  - (Inference) The strength of this pain is **weaker evidence** than pains 1–2, because the major PMSs now cover it.

## Review-mining table

Counts are the number of distinct sources or summary mentions found, **not** the number of 1–3 star reviews. Review pages could not be loaded.

| Cluster | Tool(s) | Mentions found | Paraphrased quotes (from search summaries) + link |
|---|---|---|---|
| Billing after cancel / contract lock-in | Hostaway | 3 | "billed even after canceling and refused refunds"; kept charging for the full listing count "for two additional months" after a written request to reduce to 5; "owe the full year's contracted price" when trying to pause. [Capterra Hostaway reviews](https://www.capterra.com/p/152433/Hostaway/reviews/), [page 2](https://www.capterra.com/p/152433/Hostaway/reviews/?page=2), [perrycountykids Hostaway review](https://perrycountykids.org/reviews/hostaway) |
| Slow or no support | Hostaway, Hospitable, Avalara (corporate) | 4 | Hostaway: "sold on 24/7 phone support but no one picks up"; tickets "escalated" for almost 3 days. Hospitable: AI back-and-forth took "a day or so" to reach a human. Avalara: cases open "for months". [Capterra Hostaway](https://www.capterra.com/p/152433/Hostaway/reviews/), [Trustpilot Hospitable](https://www.trustpilot.com/review/hospitable.com), [BBB Avalara](https://www.bbb.org/us/wa/seattle/profile/computer-software-developers/avalara-inc-1296-22018273/complaints?page=8) |
| Sync failures, double bookings | Hospitable, Guesty | 3 | Hospitable: "Sync broke 3 times in course of a month", slow above 10 listings, a user "lost $300" compensating guests. Guesty: channel sync issues need support intervention. [Trustpilot Hospitable](https://www.trustpilot.com/review/hospitable.com), [Capterra Guesty](https://www.capterra.com/p/159377/Guesty/reviews/) |
| Too expensive for small hosts | Guesty, MyLodgeTax | 3 | Guesty: annual fee plus monthly, "more expensive" for small hosts, undisclosed add-on fees. MyLodgeTax: $299 setup per property "can add up"; a user "used to think the service was worth it but no longer does". [Capterra Guesty](https://www.capterra.com/p/159377/Guesty/reviews/), [strspecialist MyLodgeTax review](https://strspecialist.com/reviews/avalara-mylodgetax-tax-compliance-review) |
| Missed or incorrect tax filing, penalties | Avalara (corporate, **not confirmed MyLodgeTax-specific**) | 1–2 | "failed to file taxes … leaving them with state penalties"; "refused to pay the penalty". [BBB Avalara](https://www.bbb.org/us/wa/seattle/profile/computer-software-developers/avalara-inc-1296-22018273/complaints?page=8), [taxcloud Avalara reviews](https://taxcloud.com/blog/avalara-reviews/) |
| No PMS integration, manual export/import | MyLodgeTax | 1 | Users "need to export revenue data and import it"; Airbnb has no remittance agreement with Avalara. [TIDY vs Avalara](https://www.tidy.com/comparisons/avalara) (written by a competitor, so biased) |
| Cleaner marketplace issues | Turno | 3 | Background check about $90; hosts don't respond; rushed cleans; thin coverage in rural areas. Ratings 3.8 (App Store) and 3.3 (Google Play). [App Store Turno Cleaners](https://apps.apple.com/us/app/turno-cleaners/id1263301809?see-all=reviews&platform=iphone), [Google Play](https://play.google.com/store/apps/details?id=com.turnoverbnb.app&hl=en_US), [bnbcalc Turno review](https://www.bnbcalc.com/reviews/turno-review) |
| Owner statements weak | OwnerRez | 1 | "not very robust, though plenty of work arounds". [stayfi OwnerRez](https://stayfi.com/vrm-insider/2025/10/28/ownerrez-review/) |

Note: Granicus Host Compliance, Deckard Rentalscape and GovOS LODGINGRevs are **sold to cities, not hosts** ([shortrentalrules](https://shortrentalrules.com/best-str-compliance-tools), [Granicus](https://granicus.com/product/short-term-rentals-host-compliance/), [Deckard](https://deckard.com/short-term-rental)). They are the enforcement side that creates host pain.

## Paid-labor findings (strong signals)

| Service | What they do | Price | Source |
|---|---|---|---|
| Vacation Home Help | Done-for-you monthly lodging, TDT and sales tax filing (city, county, state); host uploads a booking report | **$25/mo + $250 setup per property** | [vacationhomehelp.com/lodging-tax](https://vacationhomehelp.com/lodging-tax/) |
| Maui Books | Monthly Hawaii GET/TAT filing | **$82.50/owner/mo** (PMs with 4+ properties); **$150/mo** filing-only | [mauibooks.net/vacationrentals](https://www.mauibooks.net/vacationrentals) |
| STRpermit.com (Portland) | Permit application submission | **$360** (Type A), **$4,800** (Type B), **$260/hr** consulting | [strpermit.com/services](https://strpermit.com/services) |
| Boost Rentals | Permitting with a 2-week guarantee | **$1,000 flat** (free if hired as PM) | [boost-rentals.com](https://www.boost-rentals.com/shorttermrentalpermitting) |
| shorttermrentalpermit.com | Permit handling in LA, Orange and Ventura counties | not found | [shorttermrentalpermit.com](https://shorttermrentalpermit.com/) |
| STR bookkeepers | Payout reconciliation, per-property P&L | from $75/mo; $400/mo for 1–5 units (Steph's Books) | [bookkeeping-services.com](https://bookkeeping-services.com/vacation-rental-bookkeeping/), [stephsbooks.com](https://stephsbooks.com/industries-served/rental-property-bookkeeping) |
| Fiverr Airbnb VAs | Guest messaging, listing management, co-hosting | $50–$125 gigs; experienced VAs up to $35/hr | [Fiverr integrated_serv $125](https://www.fiverr.com/integrated_serv/your-property-virtual-assistant-on-airbnb-vrbo-guesty-booking-com-and-more), [Fiverr zeechaudry $50](https://www.fiverr.com/zeechaudry/manage-vacation-rental-properties-on-airbnb-vrbo-tripadvisor-and-other-otas), [Turno VA guide](https://turno.com/blog/airbnb-virtual-assistant/) |
| Upwork tax preparers (general) | Generic tax prep | median $60/hr, range $40–$80 | [Upwork tax preparer rates](https://www.upwork.com/hire/tax-preparers/cost/) |

Gaps in this section:

- I found **no Fiverr or Upwork gigs specifically for lodging-tax filing or STR permit applications**. Searches returned only generic VA and tax-prep listings. (Inference: this work goes to local bookkeepers and specialist firms, not gig marketplaces.)
- I could not get Spain NRA gestoría pricing because the search budget ran out.

## Workaround findings

- **Spreadsheets plus calendar reminders** for permit renewals across cities ([BP thread 1281391](https://www.biggerpockets.com/forums/517/topics/1281391-how-are-you-guys-tracking-permit-renewals-and-tot-changes-across-multiple-cities)).
- **Airbnb earnings CSV turned into an Excel return**: hosts download the "Get Report" CSV and compute county tax each month ([Airbnb Community TX](https://community.withairbnb.com/t5/Help-with-your-business/Local-Occupancy-Taxes-in-Texas/m-p/2105046), [Accounting Spreadsheet thread](https://community.withairbnb.com/t5/Help-with-your-business/Accounting-Spreadsheet/td-p/367758)).
- **Hosts can't easily tell what Airbnb already remitted**, as in the thread "Where can I find a report that shows when and how much Airbnb remitted to state tax commission?" ([Airbnb Community](https://community.withairbnb.com/t5/Help-with-your-business/Where-can-I-find-a-report-that-shows-when-and-how-much-Airbnb/m-p/1459197)). (Inference: an "Airbnb-remitted vs. you-owe" reconciler is a concrete, buildable wedge.)
- **Paid spreadsheet templates** for STR finances are sold on Gumroad and in template blogs ([Gumroad planner](https://plannerandjournal.gumroad.com/l/rzhxx), [templacity](https://templacity.com/airbnb/airbnb-excel-spreadsheet/)). This is a weak-to-moderate signal.
- Reddit could not be searched or fetched. Indie Hackers and HN produced no STR-compliance threads in my searches.

## Competitors (host-facing)

| Name | Pricing | Segment | Weaknesses / notes | Source |
|---|---|---|---|---|
| Avalara MyLodgeTax | $27/mo per property + $299 setup (third-party, 2026); Avalara's PM page shows $50 setup/property, $2/property/mo for the first 50 properties, $15/return for 6+ properties; a BP-derived summary says $19.99/listing/mo | Hosts and PMs | Per-property setup adds up; no PMS integration (export/import CSV); no Airbnb remittance agreement; one user cancelling | [strhub](https://strhub.com/product/avalara-mylodgetax-2/), [Avalara PM page](https://www.avalara.com/mylodgetax/en/solutions/property-manager.html), [TIDY vs Avalara](https://www.tidy.com/comparisons/avalara), [koohost](https://app.koohost.ai/blog/vacation-rental-tax-software) |
| STR Comply | Free check; $14.99/mo (5 props); $39.99/mo (15 props) | Hosts | Claims 100+ US cities; aggressive "alternatives" SEO pages | [strcomply.us](https://www.strcomply.us/) |
| RentPermit | $19/mo, unlimited properties | Hosts in NYC, Austin, Nashville, Chicago, Denver, Portland | Covers 6 cities only | [rentpermit.com](https://www.rentpermit.com/) |
| STR Alert | $15/mo or $10/mo annual | Hosts | Ordinance alerts only | [stralert.com](https://www.stralert.com/) |
| STRWatch | Free (1 city); Pro $29/mo; Agency $99/mo (white-label, API) | Hosts, investors, agencies | Alert and checklist layer only | [strwatch.io](https://www.strwatch.io/) |
| HostShield | Pre-launch: first 50 hosts get 3 months free | Hosts | Covers Nashville, Denver and Austin only | [hostshield.app](https://hostshield.app/) |
| PermitPath, PermitWise, STR Rule Watch, HostReady, PermitPilot, PropertyZoned | Not found | Hosts | Indicates a crowded field | [PermitPath](https://str-compliance-app.vercel.app/), [PermitWise App Store](https://apps.apple.com/us/app/permitwise/id6760926380), [shortrentalrules list](https://shortrentalrules.com/best-str-compliance-tools) |
| Vacation Home Help (service) | $25/mo + $250 setup per property | Hosts | Human service; not software | [vacationhomehelp](https://vacationhomehelp.com/lodging-tax/) |
| OwnerRez | About $130–$150/mo for 5 properties | Hosts, co-hosts | Owner statements "not very robust" | [magicbnb comparison](https://magicbnb.io/blog/best-airbnb-management-software-small-portfolios-2026), [stayfi](https://stayfi.com/vrm-insider/2025/10/28/ownerrez-review/) |
| Hostaway / Guesty | Not public in findings; annual contracts | PMs | Contract lock-in, billing disputes, cost for small hosts | [Capterra Hostaway](https://www.capterra.com/p/152433/Hostaway/reviews/), [Capterra Guesty](https://www.capterra.com/p/159377/Guesty/reviews/) |
| Hospitable | Not found | Small hosts | Sync failures; AI-first support | [Trustpilot](https://www.trustpilot.com/review/hospitable.com) |
| MagicBNB | Not found | Co-hosts | Auto owner statements and split rules | [magicbnb.io](https://magicbnb.io/) |
| Unnamed 10-year STR SaaS (for sale) | About $43K MRR, 4,600 subscriptions, 430 accounts | PMs (compliance module bundled with a guest tablet) | Shows that PMs pay annually for bundled tools | [Quiet Light listing 38638](https://quietlight.com/listings/38638/) |

### Ignored segments and gaps

The following are inferences unless a source is cited.

1. **Return preparation, not alerts.** The trackers stop at telling a host a filing is due. Avalara does the filing but costs a lot per property and needs CSV import. Human services charge $25–$150/mo.
   - A tool that ingests Airbnb, Vrbo and PMS CSVs, subtracts what the platform already remitted per jurisdiction, and outputs a pre-filled amount and form per agency would sit in that gap.
   - It would need to start with 1–2 states, for example Florida county TDT or Texas county HOT.
   - It is buildable in under 4 weeks *for a narrow geography*. It is **not** buildable nationwide in that time.
2. **Selling to the human filers.** Firms like Vacation Home Help and Maui Books process the same monthly reports for many clients. A B2B tool for them avoids the crowded host-facing SEO fight.
3. **EU hosts and agencies.** EU 2024/1028 has applied since 2026-05-20, and Spain's NRA took effect 2025-07 with mass delistings ([idealista](https://www.idealista.com/en/news/property-for-rent-in-spain/2026/01/19/877614-2025-the-year-the-single-registry-revolutionised-tourist-and-short-term), [EU transition pathways](https://transition-pathways.europa.eu/tourism/articles/why-do-short-term-rental-hosts-now-need-registration-number), [minut](https://www.minut.com/blog/eu-short-term-rental-regulations), [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1028/oj/eng)). No EU-focused host tool turned up in my searches; propertyhost.es and majordia.fr publish guides. Language and legal barriers are high for a US solo developer.

## Confidence rating: **Medium-low**

Reasons confidence is not lower:

- Paid-labor evidence is concrete, with public prices from four services.
- Regulatory pressure is documented in primary sources (CT bill, EUR-Lex, city sites).
- Avalara shows that per-property subscriptions get paid.

Reasons confidence is not higher:

1. No page was fetched directly, so every quote is a search-engine paraphrase. Review counts could not be measured.
2. Reddit was inaccessible.
3. The host-facing tracker space is crowded and cheap ($10–$40/mo), and none of the competitors shows traction.
4. Tax return preparation needs per-jurisdiction rules and has liability exposure if wrong. A 4-week build is only realistic for a narrow geography.
5. No explicit "I'd pay for X" quote was found.

## Sources

- https://www.avalara.com/mylodgetax/en/index.html
- https://www.avalara.com/mylodgetax/en/solutions/property-manager.html
- https://www.avalara.com/mylodgetax/en/resources/airbnb-occupancy-tax-guide.html
- https://strspecialist.com/reviews/avalara-mylodgetax-tax-compliance-review
- https://strhub.com/product/avalara-mylodgetax-2/
- https://www.tidy.com/comparisons/avalara
- https://app.koohost.ai/blog/vacation-rental-tax-software
- https://www.biggerpockets.com/forums/530/topics/1100417-wwwmylodgetaxcom-worth-it
- https://www.biggerpockets.com/forums/530/topics/751499-anybody-use-avalara-mylodgetax-in-miami-worth-it
- https://www.biggerpockets.com/forums/530/topics/1074473-avalara-for-lodging-tax
- https://www.biggerpockets.com/forums/530/topics/715020-short-term-airbnb-vrbo-occupancy-lodging-tax-payment-service
- https://www.biggerpockets.com/forums/517/topics/1281391-how-are-you-guys-tracking-permit-renewals-and-tot-changes-across-multiple-cities
- https://community.withairbnb.com/t5/Help-with-your-business/Local-Occupancy-Taxes-in-Texas/m-p/2105046
- https://community.withairbnb.com/t5/Help-with-your-business/Hotel-Occupancy-Tax/m-p/1841029
- https://community.withairbnb.com/t5/Help-with-your-business/Determining-the-exact-breakdown-of-Occupancy-Taxes-on-a-city/m-p/1825369
- https://community.withairbnb.com/t5/Host-guides/Florida-Sales-Tax-Tutorial-Revised-April-2024/m-p/1919540
- https://community.withairbnb.com/t5/Help-with-your-business/Where-can-I-find-a-report-that-shows-when-and-how-much-Airbnb/m-p/1459197
- https://community.withairbnb.com/t5/Help-with-your-business/Accounting-Spreadsheet/td-p/367758
- https://community.withairbnb.com/t5/Ask-about-your-listing/Is-Airbnb-double-taxing-co-host-payouts/m-p/2052032
- https://www.airbnb.com/help/article/2309
- https://www.airbnb.com/help/article/2596
- https://airbnb.com/help/article/3748
- https://www.rakidzich.com/articles/occupancy-tax-airbnb-host-collect-2026
- https://www.rakidzich.com/articles/airbnb-owner-statement-template
- https://floridarevenue.com/Forms_library/current/dr15tdt.pdf
- https://syncgtm.com/blog/on-what-line-do-i-report-tourist-development-tax-on-the-florida-sales-tax-return
- https://beancount.io/blog/2026/07/13/short-term-rental-registration-licensing-compliance-guide
- https://beancount.io/blog/2026/08/23/short-term-rental-co-host-1099k-double-reporting-reconciliation-bookkeeping-guide
- https://www.gowithsurge.com/blog/houston-short-term-rental-laws
- https://www.rentpermit.com/blog/houston-rental-permit.html
- https://cga.ct.gov/2026/FC/PDF/2026HB-05536-R000669-FC.PDF
- https://www.minnetonkamatters.com/short-term-rental-ordinance
- https://www.austintexas.gov/development-services/short-term-rentals
- https://str.sbcounty.gov/getting-started/
- https://www.nashville.gov/departments/codes/short-term-rentals/frequently-asked-questions
- https://vacationhomehelp.com/lodging-tax/
- https://www.mauibooks.net/vacationrentals
- https://strpermit.com/services
- https://www.boost-rentals.com/shorttermrentalpermitting
- https://shorttermrentalpermit.com/
- https://bookkeeping-services.com/vacation-rental-bookkeeping/
- https://stephsbooks.com/industries-served/rental-property-bookkeeping
- https://www.fiverr.com/integrated_serv/your-property-virtual-assistant-on-airbnb-vrbo-guesty-booking-com-and-more
- https://www.fiverr.com/zeechaudry/manage-vacation-rental-properties-on-airbnb-vrbo-tripadvisor-and-other-otas
- https://turno.com/blog/airbnb-virtual-assistant/
- https://www.upwork.com/hire/tax-preparers/cost/
- https://www.capterra.com/p/152433/Hostaway/reviews/
- https://www.capterra.com/p/152433/Hostaway/reviews/?page=2
- https://perrycountykids.org/reviews/hostaway
- https://www.capterra.com/p/159377/Guesty/reviews/
- https://www.trustpilot.com/review/hospitable.com
- https://www.bbb.org/us/wa/seattle/profile/computer-software-developers/avalara-inc-1296-22018273/complaints?page=8
- https://taxcloud.com/blog/avalara-reviews/
- https://apps.apple.com/us/app/turno-cleaners/id1263301809?see-all=reviews&platform=iphone
- https://play.google.com/store/apps/details?id=com.turnoverbnb.app&hl=en_US
- https://www.bnbcalc.com/reviews/turno-review
- https://stayfi.com/vrm-insider/2025/10/28/ownerrez-review/
- https://www.ownerrez.com/forums/general-help/owner-statements
- https://www.ownerrez.com/forums/general-help/monthly-statements
- https://community.hospitable.com/hospitable-changelog-3/owner-statements-and-invoices-for-airbnb-co-hosts-are-here-370
- https://magicbnb.io/
- https://magicbnb.io/blog/best-airbnb-management-software-small-portfolios-2026
- https://www.strcomply.us/
- https://www.stralert.com/
- https://www.strwatch.io/
- https://hostshield.app/
- https://str-compliance-app.vercel.app/
- https://apps.apple.com/us/app/permitwise/id6760926380
- https://shortrentalrules.com/best-str-compliance-tools
- https://granicus.com/product/short-term-rentals-host-compliance/
- https://deckard.com/short-term-rental
- https://quietlight.com/listings/38638/
- https://plannerandjournal.gumroad.com/l/rzhxx
- https://templacity.com/airbnb/airbnb-excel-spreadsheet/
- https://eur-lex.europa.eu/eli/reg/2024/1028/oj/eng
- https://transition-pathways.europa.eu/tourism/articles/why-do-short-term-rental-hosts-now-need-registration-number
- https://www.minut.com/blog/eu-short-term-rental-regulations
- https://www.idealista.com/en/news/property-for-rent-in-spain/2026/01/19/877614-2025-the-year-the-single-registry-revolutionised-tourist-and-short-term
