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

## Open items — not published on the pages

The amber "to be completed" flags were removed from the live pages at the client's instruction
(19 August 2026). Nothing false was put in their place: the VAT row was dropped, processors are
now described by category with the names held in an internal register and given on request, and
the EU representative entry was removed rather than invented. The underlying items are still open
and are tracked here:

1. **EU Article 27 representative** — still legally required. A UK-established controller that
   regularly offers roles to people in the EU cannot use the "occasional processing" exemption,
   and Article 13(1)(a) expects the representative's identity in the privacy notice. Removing the
   placeholder changed the page, not the obligation. When one is appointed, add the name and
   address to `privacy-policy` §1 and `legal/index.html`.
2. **Register of processors** — the Processing Policy §10.2 and the Privacy Policy §9 now promise
   that this register exists, names each provider with its Article 28 contract date and transfer
   mechanism, and is disclosed on request. It has to actually exist and be answerable.
3. **VAT** — the row is gone, which is correct only while the partnership is not VAT registered.
   If it registers, reg. 6 of the E-Commerce Regulations 2002 requires the number back in
   `terms-of-use` §1.
4. **Partner list** — Part 41 Companies Act 2006 requires the names of the partners and an address
   for service to be available on request; §1 of the Terms promises this, so the list must exist.
   An attorney acting under a power of attorney is not a partner and does not satisfy this.
5. **Supporting records** referenced by the Processing Policy must actually be kept: the legitimate
   interests assessments (§5), the record of processing (§16), the deletion log (§9), the complaints
   log (§15) and the training record (§20).

**Never publish on the site:** the partnership UTR and the bank/IBAN/SWIFT details from the
establishment card. The UTR is a confidential tax identifier, and published bank details on a
recruitment site undercut the anti-fraud statement in Terms §4.

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
