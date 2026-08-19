# Legal documents — maintenance notes

Three published documents, all in English, all version 2.0 (19 August 2026):

| File | Document | Audience |
|---|---|---|
| `terms-of-use/index.html` | Terms of Use | Any visitor; the site–user agreement |
| `privacy-policy/index.html` | Privacy Policy | Candidates and visitors; the Article 13/14 notice |
| `personal-data-processing/index.html` | Personal Data Processing Policy | The operational standard behind the notice, published for accountability |
| `index.html` | Hub page linking the three | — |

The documents describe the site as it is actually built: no server-side form, applications
composed in the browser and sent by the user through WhatsApp (`wa.me`), tests scored entirely
client-side, and one `pc_lang` preference cookie with no analytics or advertising technology.
If any of that changes, the documents must change with it — in particular sections 7 and 10 of
the Terms, sections 4, 7, 8 and 9 of the Privacy Policy, and sections 4, 10 and 19 of the
Processing Policy.

## Open items that need the company's input

Marked in the pages with an amber `.fill` highlight so they are impossible to miss:

1. **EU Article 27 representative** — required, because a UK-established controller that
   regularly offers roles to people in the EU cannot use the "occasional processing" exemption.
   Name and address needed in `privacy-policy` §1, `personal-data-processing` §1 and `legal/index.html`.
2. **Processor names and Article 28 contracts** — CRM, hosting, payroll/accounting.
   `personal-data-processing` §10 and `privacy-policy` §9. Version 1.0 asserted SalesRender and
   Netlify; that was not verifiable from the codebase, so the entries are now marked "to be confirmed".
3. **VAT number** — `terms-of-use` §1, or state that the partnership is not VAT registered.
4. **Partner list** — Part 41 Companies Act 2006 requires the names of the partners and an address
   for service to be available on request; §1 of the Terms promises this, so the list must exist.
5. **Supporting records** referenced by the Processing Policy must actually be kept: the legitimate
   interests assessments (§5), the record of processing (§16), the deletion log (§9), the complaints
   log (§15) and the training record (§20).

## Legal basis of the drafting (checked August 2026)

- **UK GDPR + Data Protection Act 2018, as amended by the Data (Use and Access) Act 2025.**
  Main data protection provisions commenced 5 February 2026; the duty to handle complaints from
  data subjects (DUAA s.103) applies from 19 June 2026 — acknowledge within 30 days, respond
  without undue delay, tell the complainant the outcome. Also: recognised legitimate interests
  (Art. 6(1)(ea) + Annex 1), Articles 22A–22D replacing Article 22 on automated decisions,
  "reasonable and proportionate" searches and stop-the-clock for access requests.
- **PECR as amended by DUAA**, from 5 February 2026: consent exemptions for analytics,
  functionality, security, software-update and interface-customisation storage, with information
  and an opt-out; penalties raised to UK GDPR levels. The EU has no equivalent exemption, so the
  documents commit to asking consent everywhere if anything non-essential is ever added.
- **EU GDPR (Regulation (EU) 2016/679)** applying through Article 3(2)(a); Article 27
  representative; Article 14 for referred candidates.
- **EU Digital Omnibus on data protection** (proposed 19 November 2025, incl. draft Articles 88a/88b
  on cookie consent) — still in trilogue as of August 2026, so current EU rules were applied.
- **UK adequacy** — Commission decisions renewed 19 December 2025, valid to 27 December 2031.
- **AI Act (Regulation (EU) 2024/1689)** — recruitment systems are high-risk under Annex III;
  those obligations were deferred to 2 December 2027 by the AI digital omnibus in force from
  27 July 2026, while Article 50 transparency and Article 4 AI literacy apply from 2 August 2026.
  The site uses no AI system; the documents say so and commit to disclosure if that changes.
- **Pay Transparency Directive (EU) 2023/970** — transposition deadline 7 June 2026: pay or pay
  range before the first interview, no questions about pay history. Applied to all recruitment.
- **ICO employment guidance** on recruitment and selection — legitimate interests rather than
  contract before an offer is accepted; this is why §5 of both privacy documents moved from
  Article 6(1)(b) to Article 6(1)(f) in version 2.0.
- **E-commerce and trading disclosure** — reg. 6 Electronic Commerce (EC Directive) Regulations 2002
  and Part 41 Companies Act 2006 (business name, address for service).
- **EU ODR platform** — discontinued 20 July 2025 (Regulation (EU) 524/2013 repealed by
  Regulation (EU) 2024/3228), so no ODR link is given or required.

## Review triggers

Annually at minimum, and immediately if: the application channel changes; analytics, a chatbot or
any AI screening is added; a new processor or country is introduced; the EU Digital Omnibus is
adopted; or a supervisory authority raises something.
