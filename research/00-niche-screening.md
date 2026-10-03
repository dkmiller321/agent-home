# Phase 1 — Niche Screening

Date: 2026-10-03

**Read this first:** the scores below are a desk screen. They come from analyst judgment and
general market knowledge, not from fresh evidence. They only decide which niches get a deep dive.
They are not findings. Claims backed by evidence, with source links, are in the Phase 2 reports
(`01`–`05`). The Phase 3 synthesis (`99-synthesis.md`) relies only on those reports.

Scoring is 1–5 (5 = best for a solo builder):
- **WTP:** willingness to pay. Is there existing software spend or paid labor?
- **Freq:** pain frequency. Daily or weekly scores higher than yearly.
- **Reach:** reachability. Are there online communities, directories or associations?
- **Gap:** competitor weakness. Are incumbents absent, expensive, bloated or disliked?

Hard exclusions applied: well-funded incumbents with happy customers, consumer social,
two-sided marketplaces, and heavy licensing (medical devices, banking, HIPAA-heavy clinical).

| # | Niche | WTP | Freq | Reach | Gap | Total | Notes |
|---|-------|-----|------|-------|-----|-------|-------|
| 1 | Small GCs / property managers tracking subcontractor & vendor certificates of insurance (COI) | 5 | 4 | 4 | 4 | **17** | Expired COIs create real liability exposure. Many firms use a spreadsheet plus email chasing, or pay an admin to do it. Enterprise tools (myCOI, Jones, TrustLayer) are priced for larger firms. |
| 2 | Small e-commerce sellers (Shopify/Etsy) facing EU GPSR & product-compliance rules | 4 | 3 | 5 | 4 | **16** | GPSR has applied since Dec 2024 and creates new per-product work (EU responsible person, safety info, traceability). The community is very reachable. The tooling is young. |
| 3 | Bookkeeping / accounting firms chasing clients for docs & uncategorized transactions | 5 | 5 | 5 | 2 | **17** | Pain is weekly and certain, and firms already spend on software. But the space is crowded (TaxDome, Karbon, Financial Cents, Uncat, Canopy). It goes to deep dive to find the segment they ignore. |
| 4 | Small trucking carriers / owner-operators: IFTA, IRP, DQ files, compliance paperwork | 4 | 3 | 4 | 3 | **14** | Recurring regulatory work every quarter. Many carriers pay a compliance service or do it by hand. Reachable via r/Truckers, TruckersReport and FB groups. Some customers are not very tech-savvy. |
| 5 | Short-term rental hosts (1–20 units): local permits, occupancy tax, registration rules | 4 | 3 | 5 | 3 | **15** | City regulation keeps getting stricter (NYC LL18 and others). Owners are prosumer and already spend on PMS/dynamic pricing. Very reachable. |
| 6 | Small construction subs: lien waivers & preliminary notices | 4 | 3 | 3 | 2 | 12 | Strong regulatory deadlines, but Levelset (Procore) is entrenched and the rules differ in every state, so it is hard to build in 4 weeks. |
| 7 | Independent HVAC / plumbing contractors: field service mgmt | 4 | 5 | 4 | 1 | 14 | ServiceTitan, Jobber and Housecall Pro are well funded and broadly liked. Excluded on competition. |
| 8 | Small landlords (5–200 units): property mgmt | 4 | 4 | 5 | 1 | 14 | AppFolio, Buildium, DoorLoop, TurboTenant and Baselane are crowded and funded. |
| 9 | Etsy/eBay/Poshmark resellers: crosslisting & inventory | 3 | 5 | 5 | 2 | 15 | Vendoo, List Perfectly and Crosslist are established. Low price ceiling. |
| 10 | Amazon sellers: FBA reimbursement claims | 5 | 3 | 4 | 1 | 13 | People pay humans a % of recoveries, which is a strong signal. But Getida and many agencies already serve it, and it depends on Amazon's policies. |
| 11 | Wedding / event venues: inquiry → booking → payments | 4 | 4 | 3 | 2 | 13 | Tripleseat, Perfect Venue and HoneyBook are well covered. |
| 12 | Loan signing agents / notaries: journal, mileage, bookkeeping | 2 | 4 | 5 | 3 | 14 | Very reachable, but prices are low and some tools already exist (NotaryGadget, Signing Agent Pro). |
| 13 | Music teachers / tutors: scheduling & billing | 2 | 4 | 4 | 2 | 12 | Low WTP. My Music Staff and TutorBird are well liked. |
| 14 | Small nonprofits: grant deadlines & reporting | 3 | 2 | 4 | 3 | 12 | Budgets are thin. Pain is seasonal. |
| 15 | Small dental / therapy practices: insurance verification | 5 | 5 | 3 | 3 | 16 | Strong pain and WTP, but HIPAA/BAA and clearinghouse integrations mean it can't ship in 4 weeks and fails the licensing filter. Excluded. |

## Selected top 5 for deep dive

1. **Subcontractor/vendor COI tracking for small GCs & property managers (17).** The failure
   mode costs real money (an uninsured sub on a job site). The work is recurring (policies
   renew every year and there are dozens of subs). The common workaround is a spreadsheet or a
   paid admin, which is a strong signal. Incumbents look priced for mid-market. The core
   product (upload a COI, extract expiry dates, chase automatically by email) fits in 4 weeks.
2. **EU GPSR compliance for small e-commerce sellers (16).** This is a new regulation creating
   new work, which is the strongest kind of signal. Sellers are concentrated on Shopify and
   Etsy, and those platforms have app marketplaces, which gives a distribution channel. Tools
   are still immature. It could also be a seasonal spike, and Phase 2 needs to test whether
   the pain lasts.
3. **Bookkeeping firm client follow-up (17).** It had the highest WTP and frequency. It is
   crowded, so the deep dive has to find the segment the incumbents ignore (for example solo
   bookkeepers priced out, or one narrow job like uncategorized-transaction chasing).
4. **Short-term rental host compliance (15).** Regulation is rising and the audience is
   prosumer, spends money and is highly reachable. The open risk is that the rules are
   hyper-local, which may not generalize into one product.
5. **Trucking small-carrier compliance (14).** This scored below resellers (15), but resellers
   lose on competitor weakness and price ceiling. Trucking has quarterly regulatory deadlines
   (IFTA) and a paid-service market (compliance agencies). It is a "boring" niche that tests
   whether a software layer can replace paid humans.

Dental insurance verification (16) scored well but is excluded on HIPAA/integration grounds.
Resellers (15) are excluded on incumbent strength and low price ceiling.
