# 03 — Bookkeeper Client-Chasing (docs, receipts, uncategorized transactions)

Research date: 2026-10-03. Niche: solo bookkeepers to ~20-person bookkeeping/accounting firms chasing clients for documents, receipts and answers on uncategorized transactions.

## Method and evidence limitations (read first)

- **WebFetch was blocked by the network egress proxy for every target domain tried**: capterra.com, g2.com, softwareadvice.com, apps.xero.com, uncat.com, financial-cents.com, getuku.com, doublehq.com, accountingweb.co.uk, quickbooks.intuit.com. Reddit could not be fetched or searched ("domains not accessible to our user agent").
- So **no page was read directly**. Everything below comes from WebSearch result summaries, which paraphrase the pages. Short phrases in quotation marks are wording the search tool gave as quotes; they **could not be checked against the source page**. Treat them as "reported quotes", not verified verbatim.
- The search budget ran out (200/200 calls across the session) before Xero App Store reviews, Trustpilot and the ReCats/Xero gap could be checked.
- Review "counts" are **the number of distinct complaint mentions found in search snippets**, not a census of reviews. They show what complaints exist, not how common they are.
- Reddit, r/taxpros, Indie Hackers and HN produced **no usable evidence** (blocked, or nothing relevant came up).

## Summary

The pain is real, well documented and **already monetized**. Several tools charge per client every month for exactly the "uncategorized transaction Q&A" job: Uncat at $9 per client per month, Financial Cents ReCats at $4 per client, Double (formerly Keeper) from $8–10 per client, and Client Hub from $49 per user. There are also many cheap indie document-collection tools: RequestLoops at $11/mo, ClientClose from $28–35/mo, Portico with a free tier, and Content Snare from $35/mo. QuickBooks Online Accountant and Xero HQ both have free, native "ask client" features. **Generic "chase clients for docs" and generic "uncategorized transaction portal" are saturated, including at the low end. A solo dev should not build either.**

The gaps that look least served (inference, moderate support):
1. **Answer-by-reply with no portal or link at all.** Clients answer by SMS, WhatsApp or plain email reply, and the replies get parsed back onto the transaction. Incumbents send text *reminders*, but the answer still happens in a portal or magic link. The evidence that clients avoid portals is consistent. WhatsApp capture tools exist for *receipts* (Nomi, Tofu, ClientWindow) but none were found for *transaction Q&A*.
2. **UK MTD for Income Tax (regulation).** Since April 2026, sole traders and landlords over £50k must file quarterly, and the threshold drops to £30k in April 2027. Annual chasing becomes quarterly chasing. Large UK suites (Bright, IRIS, TaxCalc) are moving in. Bright launched an AI "Document Collection" agent in Aug 2026, so a window exists but is closing.
3. **Native-QBO fallback.** There is a reported bug where QBO's free "Ask client" flow does not save a client's last answer. That suggests the free native tool is unreliable, but this is one thread and weak evidence.

Overall: strong evidence of willingness to pay, and weak evidence of an uncontested segment.

## Top 3 pain points

### 1. Getting clients to answer questions about uncategorized / "Ask My Accountant" transactions
- **Description:** Every month, transactions land in Uncategorized Expense/Income or Ask My Accountant. The traditional workflow is to copy them into a spreadsheet, email it, wait days, and get back a partly filled sheet. Uncat calls this "the #1 broken process in bookkeeping".
- **Evidence:**
  - Uncat blog describes the spreadsheet/email workflow and reports clients filling in "only a fraction of the cells". Vendor source. https://www.uncat.com/blog/the-1-broken-process-of-bookkeeping-resolving-uncategorized-transactions
  - Business Wire: Uncat users fixed 175,000+ transactions worth $450M+. This shows paid usage at scale. https://www.businesswire.com/news/home/20230112005186/en/Uncat-Helps-Accountants-and-Bookkeepers-Fix-More-Than-450-Million-Dollars-in-Uncategorized-Transactions-With-Their-Small-Business-Clients
  - Intuit community thread: "Books review - Client uncategorized transactions not saving their last answer". The free native QBO flow is reported to drop the last of five answers. https://quickbooks.intuit.com/learn-support/other-questions-9/books-review-client-uncategorized-transactions-not-saving-their-last-answer-85734
  - Uncat podcast transcript (per the search summary): "Uncategorized asset has been a pain for accountants for a very long time". https://uqb.show/27/transcript
  - Financial Cents sells ReCats as a separate $4/client add-on for this exact job. https://help.financial-cents.com/en/articles/8993246-recats-manage-uncategorized-transactions
  - Client Hub ships a QBO uncategorized-transaction integration. https://www.clienthub.app/blog/client-hub-quickbooks-uncategorized-transactions-integration
- **Frequency:** monthly, for every write-up client. High.
- **Who feels it:** the bookkeeper or staff accountant doing the close.
- **Who controls budget:** the firm owner. At a solo firm, the bookkeeper is the owner.
- **Current cost of workaround:** $4–$10 per client per month in tooling (Uncat, ReCats, Double), or bookkeeper time spent on spreadsheets and emails. Vendor-marketing figures put this at "10–30+ hours" a month (Enterprise DNA, onboardmap.com). These are unverified marketing numbers. https://enterprisedna.co/resources/guides/accounting-stop-chasing-client-documents/ , https://onboardmap.com/insights/onboarding/document-chase-is-killing-your-bookkeeping-practice/

### 2. Clients won't use portals (login friction), so everything falls back to email or WhatsApp
- **Description:** Firms set up portals and clients never log in. Clients send photos over WhatsApp or text instead, and the firm loses track.
- **Evidence:**
  - PacketDesk on "no-login" portals: clients never log in, and the accountant falls back to email. https://packetdesk.co/blog/no-login-client-portal-for-accountants
  - Accountex "Solving the WhatsApp Dilemma": practices gave out personal WhatsApp numbers, which led to "midnight messages, misplaced files". https://www.accountex.co.uk/insight/2024/07/25/solving-the-whatsapp-dilemma/
  - Nomi WhatsApp receipt capture is pitched as removing "another app, portal or login". https://www.nomi.co.uk/all-features/whatsapp-receipt-capture/
  - Tofu "WhatsApp bookkeeping". https://www.gotofu.com/features/whatsapp
  - Canopy review summary: "inability to communicate with other methods than email can be a hindrance", and the reviewer wants texting to the client's cell. https://www.capterra.com/p/150647/Canopy-Tax/reviews/
  - TaxDome review summary: the client portal was "difficult to navigate". https://www.capterra.com/p/186749/TaxDome/reviews/
  - Xero Ask requires the client to log in to Xero to reply. https://central.xero.com/s/article/Ask-in-Xero-HQ
- **Frequency:** high. This is behind the entire "magic link" trend (Uncat, PacketDesk).
- **Who feels it:** bookkeepers, and the clients who are small-business owners.
- **Who controls budget:** the firm owner.
- **Current cost of workaround:** manual re-keying of WhatsApp/email replies. Liscio charges extra for two-way texting on top of $45–75 per user per month. https://www.getapp.com/collaboration-software/a/liscio/

### 3. Document/receipt chasing as seasonal and recurring admin (tax season, month-end, now quarterly MTD in UK)
- **Description:** The cycle runs: identify what's missing, email, wait, follow up, receive incomplete files, repeat. UK MTD for Income Tax makes this quarterly for sole traders above £50k from April 2026 and above £30k from April 2027.
- **Evidence:**
  - AccountingWEB (11 Aug 2026): "AI agent takes on the job nobody wants: Chasing clients" (Bright Document Collection agent). https://www.accountingweb.co.uk/tech/accounting-software/ai-agent-takes-on-the-job-nobody-wants-chasing-clients
  - AccountingWEB Any Answers: "Best way to ask clients questions/collate records". Practitioners describe portals and online spreadsheets as workarounds. https://www.accountingweb.co.uk/any-answers/best-way-to-ask-clients-questionscollate-records
  - TaxCalc: "MTD for Income Tax: Solving the capacity puzzle before it breaks your firm". https://www.taxcalc.com/blog/mtd-solving-the-capacity-puzzle
  - IRIS: quarterly cycle; "manual processes for chasing information… quickly become reactive". https://www.iris.co.uk/blog/misc/making-tax-digital-for-accountants-practice-strategy/
  - ICAEW TAXguide 01/25 on MTD for Income Tax (regulation primary-ish source). https://www.icaew.com/technical/tax/tax-faculty/taxguides/2025/taxguide-01-25
  - Content Snare has 1,600+ customers paying $35–$215/mo for request/reminder automation. https://www.portico.run/blog/post/content-snare-pricing
- **Frequency:** seasonal spike (US tax season); monthly for write-up clients; quarterly for UK MTD clients.
- **Who feels it:** admins and preparers.
- **Who controls budget:** the firm owner or partner.
- **Current cost of workaround:** VA labor at about $20–28/hr US or $4–15/hr offshore (see Paid labor), or tooling at $11–$215/mo.

## Review-mining table

Caveat: none of these review pages could be fetched. "Mentions" are the distinct complaints surfaced in search snippets. Phrases in quotes come from the search tool's quoting and are unverified.

| Cluster | Tool(s) | Mentions found | Reported quotes / paraphrases | Source |
|---|---|---|---|---|
| Price too high for small/solo firms | TaxDome | 3 | "pretty pricey and payment plans would be a nice feature"; extra fees for extra users, recurring price increases | https://www.capterra.com/p/186749/TaxDome/reviews/ ; https://www.capterra.com/p/186749/TaxDome/reviews/?page=18 |
| Price / plan cost | Uncat | 2 | "High pricing on the plans offered"; "limitations with customization and pricing" | https://www.capterra.com/p/247759/Uncat/reviews/ ; https://www.g2.com/products/uncat/reviews |
| Limited customization / filtering / reporting | Uncat | 5 | "very limited customization and limited features"; "interface sometimes feels too minimal with limited filtering or tagging"; "limited customization options for categorization rules"; reports need more filtering | https://www.capterra.com/p/247759/Uncat/reviews/ ; https://www.softwareadvice.com/data-management/uncat-profile/reviews/ |
| Sync delays with QBO | Uncat | 1 | "occasional sync delays with QuickBooks" | https://www.capterra.com/p/247759/Uncat/reviews/ |
| Complexity / setup burden | TaxDome, Karbon | 3 | TaxDome: "overwhelming… still working through everything after 6 months"; Karbon "too difficult to use" (from a TaxDome reviewer); Karbon templates/automations "time-consuming and require precision" | https://www.capterra.com/p/186749/TaxDome/reviews/ ; https://www.capterra.com/p/156181/Karbon/reviews/ |
| Client-side portal/comms problems | Karbon, Canopy, TaxDome, Client Hub | 5 | Karbon: every task comment goes to the client as a separate email; client portal "needing much improvement". Canopy: portal errors after "upgrade"; email-only communication. Client Hub: "cannot access files on the mobile app", "conversations are delayed" | https://www.capterra.com/p/156181/Karbon/reviews/ ; https://www.capterra.com/p/150647/Canopy-Tax/reviews/ ; https://getuku.com/articles/client-hub-review/ |
| Xero support weaker than QBO | Client Hub, Financial Cents ReCats | 2 | Client Hub "Xero integration much narrower than QuickBooks"; ReCats docs describe pulling from QBO only (Xero support not confirmed; inference) | https://getuku.com/articles/client-hub-review/ ; https://help.financial-cents.com/en/articles/8993246-recats-manage-uncategorized-transactions |
| Recurring client requests awkward | Double (Keeper) | 1 | recurring client requests "less straightforward than competitors" (competitor-authored source; biased) | https://financial-cents.com/resources/articles/double-keeper-alternatives/ |

Not covered (blocked or out of budget): Xero App Store reviews, QuickBooks App Store reviews, Trustpilot.

## Paid-labor findings

- Upwork lists a "bookkeeping virtual assistants" hire category. Its duties include following up with clients or vendors to gather missing receipts and statements, plus categorization. Typical focused projects run $500–$1,500; transaction entry and categorization runs $300–$600 per project. https://www.upwork.com/hire/bookkeeping-virtual-assistants/
- Upwork had an open listing for a part-time "Accounts Receivable / Client Follow-Up Specialist" supporting a CPA firm (seen via search summary only; listing not opened). https://www.upwork.com/freelance-jobs/bookkeeping/
- ZipRecruiter: US bookkeeping VA average **$24.40/hr**, mostly $20.43–$27.40 (as of Jul 2026). https://www.ziprecruiter.com/Salaries/Bookkeeping-Virtual-Assistant-Salary
- Indeed postings list "follow up with clients to collect missing documents" as a duty. https://www.indeed.com/q-virtual-bookkeeping-assistant-jobs.html
- Offshore VA shops advertise **$4–$8/hr** bookkeeping assistants. https://www.bruntwork.co/virtual-assistant-for-bookkeeping/
- Inference: a 10-client firm spending 5 hrs/month of VA time on chasing pays about $100–$125/month at US rates or $20–$40 offshore. That puts the willingness-to-pay ceiling for a chasing tool at about $30–$100/month for a small firm, which matches existing pricing.

## Workaround findings

- **Spreadsheet + email** is the default the incumbents explicitly sell against (Uncat blog, above). Accountants also describe "shared spreadsheets", per the Uncat review snippets. https://www.capterra.com/p/247759/Uncat/reviews/?page=2
- **Online spreadsheets/forms plus email reminders** are described on AccountingWEB as homemade portals. https://www.accountingweb.co.uk/any-answers/best-way-to-ask-clients-questionscollate-records
- **Native free tools:** QBO Accountant "Ask client" / My Accountant → Requests (https://quickbooks.intuit.com/learn-support/en-us/help-article/manage-client/month-end-reviews-finish-clients-open-tasks/L4GubaqKy_US_en_US), Xero HQ Ask (client must log in) and Xero "Discuss" on bank lines (https://central.xero.com/s/article/Ask-in-Xero-HQ ; https://vhaccounting.ca/2020/09/22/ask-your-accountant-a-question-in-xero/).
- **Personal WhatsApp** as a channel, with resulting chaos. https://www.accountex.co.uk/insight/2024/07/25/solving-the-whatsapp-dilemma/
- Reddit, Indie Hackers and HN: **no evidence obtained** (Reddit blocked; IH/HN searches returned nothing relevant). No explicit "I'd pay for this" quote was found.

## Competitors table

| Name | Pricing (as reported) | Segment | Weaknesses (reported) | Source |
|---|---|---|---|---|
| Uncat | $9/client/mo; 7-day trial | Uncategorized txn Q&A; QBO, Xero, QBD; magic link | Limited customization/filtering, price, occasional QBO sync delay | https://www.softwareadvice.com/data-management/uncat-profile/ ; https://www.capterra.com/p/247759/Uncat/reviews/ |
| Financial Cents (+ ReCats) | Solo $19, Team $49/user, Scale $69/user; ReCats $4/client; Month-End Close $5/client (annual) | Practice mgmt for small firms | ReCats documented for QBO (Xero unconfirmed) | https://financial-cents.com/pricing/ ; https://help.financial-cents.com/en/articles/8993246-recats-manage-uncategorized-transactions |
| Double (formerly Keeper) | ~$8–10/client entry; Core $10, Plus $25, Scale $50 per client | Month-end close/review; QBO + Xero; email/text reminders | Per-client cost scales; recurring requests clunky (competitor claim) | https://www.g2.com/products/double-formerly-keeper/pricing ; https://curatesuite.com/accounting/tools/keeper |
| Client Hub | $49 / $79 / $99 per user/mo | Practice mgmt + QBO uncategorized resolution | Xero narrower; mobile app issues; no native billing | https://getuku.com/articles/client-hub-review/ |
| TaxDome | Essentials $800/yr (single user), Pro $1,000/user/yr, Business $1,200/user/yr; Pro monthly $100/seat | Tax-heavy all-in-one | Expensive for solos; complex; portal navigation | https://toolradar.com/tools/taxdome/pricing ; https://www.capterra.com/p/186749/TaxDome/reviews/ |
| Karbon | Team $59, Business $89/user/mo annual ($79/$99 monthly) | Mid-size firms, workflow | Hard to use, client portal weak, email noise to clients | https://financial-cents.com/resources/articles/karbon-pricing/ ; https://www.capterra.com/p/156181/Karbon/reviews/ |
| Canopy | Not captured (budget) | Tax practice mgmt | Portal errors; email-only client comms | https://www.capterra.com/p/150647/Canopy-Tax/reviews/ |
| Liscio | ~$45–75/user/mo; extra fees for two-way texting, e-sign, organizers | Secure client messaging (CPA) | Add-on fees | https://www.getapp.com/collaboration-software/a/liscio/ |
| Content Snare | $35 / $71 / $119 / $215+ per mo (annual), by active requests | Generic doc/info collection | Not ledger-aware (inference) | https://www.portico.run/blog/post/content-snare-pricing |
| RequestLoops | $11 / $22 / $57 per mo | Cheap request/reminder tool | Small indie | https://requestloops.com/en/compare/content-snare/ |
| ClientClose | $35/mo (5 clients) or $28 annual; $59/mo tier | Bookkeeper close + receipt portal | New indie | https://clientclose.app/ |
| Portico | Free (3/mo); $39 / $79 / $149 | Onboarding / doc chase | Generic | https://www.portico.run/ |
| QBO Accountant / Xero HQ native | Free with ledger | Built-in ask-client | QBO answer-save bug reported; Xero requires client login | links in Workaround findings |
| Bright Document Collection (UK) | Not captured | UK practices, AI chasing agent | New (Aug 2026) | https://www.accountingweb.co.uk/tech/accounting-software/ai-agent-takes-on-the-job-nobody-wants-chasing-clients |

### Segments the incumbents appear to ignore (inference)
1. **Zero-portal answering.** No tool found lets a client answer "what was this $84 at Amazon?" by replying to an SMS, WhatsApp message or email, with the reply written back to the QBO/Xero transaction. Receipt-photo WhatsApp tools exist (Nomi, Tofu), but nothing found for categorization Q&A. Note that Uncat's magic link already removes logins, so the improvement is incremental. **4-week buildable:** QBO/Xero OAuth, pull uncategorized lines, send one message per batch, parse replies with an LLM into category + memo, accountant approves, write back.
2. **Xero-first and non-QBO ledgers.** Several tools are documented QBO-first (ReCats, Client Hub). Evidence is thin (2 mentions).
3. **UK MTD ITSA quarterly sole-trader chase.** This is a new regulatory forcing function. Incumbents there are UK suites rather than the US tools listed. A narrow "quarterly MTD readiness chaser" (checklist + reminders + uncategorized Q&A for sole-trader clients on Xero/QBO/FreeAgent) fits a solo-dev scope. Bright's agent and Xero's own MTD tooling are direct threats.

## Confidence rating

**Medium on the existence of the pain and willingness to pay; low on finding an uncontested segment.**
- For the pain and willingness to pay: there are multiple independent paid products at $4–$10 per client per month, Content Snare has 1,600+ customers, VA job duties explicitly include chasing, and a UK regulatory driver exists.
- Against: no review page or forum thread could be read directly (egress blocked; Reddit blocked), so the quotes are unverified search-tool paraphrases and the counts are not representative. Much of the "hours lost" data is vendor marketing. No explicit "I'd pay for X" statement was found. The market is crowded at the cheap end too: RequestLoops at $11, ClientClose at $28, Portico free.
- The proposed gaps are **inferences**. The next steps should be direct reading of r/Bookkeeping threads and Xero App Store reviews of Uncat, plus 5–10 bookkeeper interviews asking "would you pay $X for reply-by-text categorization?"

## Sources

- https://www.businesswire.com/news/home/20230112005186/en/Uncat-Helps-Accountants-and-Bookkeepers-Fix-More-Than-450-Million-Dollars-in-Uncategorized-Transactions-With-Their-Small-Business-Clients
- https://www.uncat.com/blog/the-1-broken-process-of-bookkeeping-resolving-uncategorized-transactions
- https://www.softwareadvice.com/data-management/uncat-profile/
- https://www.softwareadvice.com/data-management/uncat-profile/reviews/
- https://www.capterra.com/p/247759/Uncat/reviews/
- https://www.capterra.com/p/247759/Uncat/reviews/?page=2
- https://www.g2.com/products/uncat/reviews
- https://www.capterra.com/p/186749/TaxDome/reviews/
- https://www.capterra.com/p/186749/TaxDome/reviews/?page=18
- https://toolradar.com/tools/taxdome/pricing
- https://www.capterra.com/p/156181/Karbon/reviews/
- https://financial-cents.com/resources/articles/karbon-pricing/
- https://www.capterra.com/p/150647/Canopy-Tax/reviews/
- https://getuku.com/articles/client-hub-review/
- https://www.clienthub.app/blog/client-hub-quickbooks-uncategorized-transactions-integration
- https://financial-cents.com/pricing/
- https://help.financial-cents.com/en/articles/8993246-recats-manage-uncategorized-transactions
- https://financial-cents.com/resources/articles/double-keeper-alternatives/
- https://www.g2.com/products/double-formerly-keeper/pricing
- https://curatesuite.com/accounting/tools/keeper
- https://www.getapp.com/collaboration-software/a/liscio/
- https://www.portico.run/blog/post/content-snare-pricing
- https://requestloops.com/en/compare/content-snare/
- https://clientclose.app/
- https://www.portico.run/
- https://quickbooks.intuit.com/learn-support/other-questions-9/books-review-client-uncategorized-transactions-not-saving-their-last-answer-85734
- https://quickbooks.intuit.com/learn-support/en-us/help-article/manage-client/month-end-reviews-finish-clients-open-tasks/L4GubaqKy_US_en_US
- https://uqb.show/27/transcript
- https://central.xero.com/s/article/Ask-in-Xero-HQ
- https://vhaccounting.ca/2020/09/22/ask-your-accountant-a-question-in-xero/
- https://www.accountingweb.co.uk/any-answers/best-way-to-ask-clients-questionscollate-records
- https://www.accountingweb.co.uk/tech/accounting-software/ai-agent-takes-on-the-job-nobody-wants-chasing-clients
- https://www.taxcalc.com/blog/mtd-solving-the-capacity-puzzle
- https://www.iris.co.uk/blog/misc/making-tax-digital-for-accountants-practice-strategy/
- https://www.icaew.com/technical/tax/tax-faculty/taxguides/2025/taxguide-01-25
- https://dext.com/uk/blog/single/how-to-answer-critical-questions-sole-traders-have-on-the-mtd-itsa-2026-deadline
- https://www.accountex.co.uk/insight/2024/07/25/solving-the-whatsapp-dilemma/
- https://www.nomi.co.uk/all-features/whatsapp-receipt-capture/
- https://www.gotofu.com/features/whatsapp
- https://packetdesk.co/blog/no-login-client-portal-for-accountants
- https://enterprisedna.co/resources/guides/accounting-stop-chasing-client-documents/
- https://onboardmap.com/insights/onboarding/document-chase-is-killing-your-bookkeeping-practice/
- https://www.upwork.com/hire/bookkeeping-virtual-assistants/
- https://www.upwork.com/freelance-jobs/bookkeeping/
- https://www.ziprecruiter.com/Salaries/Bookkeeping-Virtual-Assistant-Salary
- https://www.indeed.com/q-virtual-bookkeeping-assistant-jobs.html
- https://www.bruntwork.co/virtual-assistant-for-bookkeeping/
