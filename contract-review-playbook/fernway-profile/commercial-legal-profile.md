# Commercial Contracts Practice Profile

*Written by the cold-start interview on 2026-10-13. Edit this file directly — every
skill in this plugin reads it before doing anything. If something below is wrong,
fix it here and it's fixed everywhere.*

*Fernway, Inc. is a fictional company used to build and test in-house legal workflows.*

---

## Who we are

Fernway, Inc. is a Delaware C-corp headquartered in New York City. It sells a B2B SaaS
platform with AI features to enterprise and mid-market customers, some in regulated
industries. The AI features run on a third-party foundation model provider (assumed).

The contracts team is three people: a GC, a commercial counsel, and a contracts manager.
The CEO is the final escalation point. We process roughly 20–50 agreements per month.
Negotiation is mixed: mid-market customers mostly sign our paper with light redlines;
enterprise and regulated customers bring their own paper or mark ours up heavily.
No CLM is in use.

**Practice setting:** In-house

**The thing that hurts:** "Needless redlines from customer counsel. Mostly posturing, we
can accept the vast majority of their edits, but get stuck overanalyzing everything."

---

## Who's using this

**Role:** Lawyer / legal professional
**Attorney contact:** N/A (user is counsel)

---

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| CLM (Ironclad, Agiloft, etc.) | ✗ | Manual record-keeping; renewal-tracker runs against a local register |
| E-signature (DocuSign, etc.) | ✗ | User routes for signature outside the plugin |
| Document storage (Drive / SharePoint / Box) | ✗ | User uploads agreements directly for each review |
| Slack | ✗ | Alerts and stakeholder summaries delivered inline instead of posted |

*No connectors were found on 2026-10-13. Re-check: `/commercial-legal:cold-start-interview --check-integrations`*

---

## Playbook

**Active side:** both

*Sales-side = the company sells its products or services. We're the vendor. Usually our paper. Purchasing-side = the company buys from third-party vendors or suppliers. We're the customer. Usually their paper. The answer changes every playbook position.*

> Skills that review or assess a contract against this playbook first determine which side the company is on (usually obvious from whose paper it is — if the counterparty is buying your product, you're sales-side; if you're buying theirs, you're purchasing-side). If it's not obvious, ask. Read the matching playbook section. Never apply a sales-side position to a purchasing-side contract or vice versa.

### Sales-side playbook

*Applies when Fernway is the vendor. Usually our paper. [LIMITED DATA — 0 agreements reviewed; positions are stated, not yet checked against signed deals]*

#### Limitation of liability

**Standard position:** General cap = 12 months of fees paid or payable. Same cap for direct damages and total liability.

**Super-cap:** One super-cap covers confidentiality breach, IP indemnity, gross negligence / willful misconduct, and data breach / data protection claims. Up to 10× the general cap (i.e., up to 10× annual fees), scaled to customer and deal size; may instead be tied to Fernway's applicable insurance limits.

**Acceptable fallbacks:** Super-cap multiples up to 5× within commercial counsel authority; above 5× requires GC.

**Never accept (without CEO sign-off):** Uncapped liability of any kind — including for data breach or IP. Uncapped data-breach or IP liability is an automatic CEO escalation.

**Carveouts we accept:** None fully uncapped. All of the above sit under the super-cap.

#### Indemnification

**Fernway gives (IP infringement):** Standard third-party IP infringement indemnity for the platform.
- Exclusions: combinations with non-Fernway products; customer modifications; customer data, content, or instructions; use outside the documentation.
- Remedy ladder: modify or replace; if that doesn't work, terminate and refund prepaid fees for the unused term.

**AI outputs:**
- **Standard (Option B):** Conditional output indemnity — copyright claims only; customer must have used Fernway's built-in guardrails/content filters and not disabled them; no intentional prompting for infringing material and no inputs the customer lacked rights to; covers unmodified output only; trademark claims from customer's commercial use of output excluded; customer stops using output once notified of a claim. Sits inside the 10× super-cap. Fernway's commitment never exceeds what its upstream model provider gives Fernway.
- **Fallback (Option A, low-value deals):** Platform-only indemnity; outputs excluded.
- **Watch for in markups:** redefining "Services" to sweep in Outputs; deleting the AI-output exclusion; originality / non-infringement warranties on outputs; training-data provenance warranties; uncapping the output indemnity; pass-through of the upstream provider's indemnity.

**Customer gives:** Customer indemnifies Fernway for anything outside the platform — customer data, content the customer uploads — and for violations of the acceptable use of the platform.

**Never give:** A general "any breach" indemnity; indemnity for regulatory fines.

#### Data protection

**DPA:** Fernway's own DPA preferred. Will use an enterprise customer's DPA if there is no choice.

**Breach notification:** "Without undue delay, but no later than 72 hours after discovery." Shortest acceptable: 48 hours.

**Subprocessors:** Notice of new subprocessors with a 15–30 day objection window and good-faith discussion; customer's sole remedy is termination of the affected service; no customer veto. (Objection right included because GDPR Art. 28(2) requires one where Fernway is a processor of EU/UK personal data.) Prior customer approval only in rare circumstances.

**AI model provider as subprocessor:** Name the provider specifically; disclose that customer data is sent to it; flow down the provider's no-training and limited-retention commitments; provider changes go through the standard notice-and-objection process; remedy for an objection is the ability to turn off AI features (not termination of the whole agreement). Do not commit to a specific model.

**Security / audit:** SOC 2 Type II report and penetration-test summary in place of on-site audits. Actual customer audits only for regulated customers.

**Training on customer data:** No training on customer content (inputs, uploaded data, outputs). Aggregated, de-identified usage data permitted under a defined de-identification standard. Opt-in programme available if Fernway ever wants one. Fernway demands the same from its own vendors (purchasing side).

#### Term and termination

**Termination for convenience:** Allowed, but no refund. Termination for convenience *with* a refund is an automatic CEO escalation.

**Renewal:** 12-month renewal terms; 30 days' notice to cancel. *(Changed from 60 days on 2026-10-26 to match the purchasing-side position — 60 days is too far in advance.)*

**Renewal price increases:** Capped — 7% standard, 5% floor in negotiation. *(Interpretation — confirm.)*

#### Insurance

**Position:** Fernway's paper has no insurance provision. Do not raise insurance proactively. Respond only if the customer requests it.

#### Governing law and venue

**Preferred:** New York law
**Acceptable:** Delaware law
**Escalate:** Other jurisdictions — not a dealbreaker; Fernway will compromise beyond Delaware
**Never:** None stated
**Venue:** Courts of the governing-law state (no arbitration) — assumed; not confirmed.

#### The one thing

Not a single walk-away. Two terms always require CEO sign-off and are checked first on every sales-side review:
1. Uncapped liability for data breach or intellectual property.
2. Termination for convenience with a refund.

#### NDA triage positions

Same positions on both sides. See `### NDA playbook (both sides)` below.

---

### Purchasing-side playbook

*Applies when Fernway is the customer. Usually the vendor's paper. Built by `--side purchasing` interview on 2026-10-26. [LIMITED DATA — 0 agreements reviewed; positions are stated, not yet checked against signed deals]*

#### Limitation of liability

**Standard position:** A general cap of 12 months of fees, with standard carveouts, is acceptable from vendors.

**Super-cap:** Mirror of the sales side — one super-cap covering confidentiality breach, IP indemnity, gross negligence / willful misconduct, and data breach / data protection claims, up to 10× annual fees.

**Acceptable fallbacks:** Super-cap down to 2× annual fees within commercial counsel authority. **Below 2× → GC.**

**Uncapped carveouts in Fernway's favor:** Acceptable as-is. Don't push back on a vendor leaving confidentiality, GN/WM, or similar uncapped.

**Lost-data exclusion:** A vendor excluding "loss of data" as indirect damages is acceptable. Expect it from large vendors.
- **Ask first:** Breach-response costs (notification, forensics, credit monitoring, regulator response) are treated as direct damages.
- **If refused:** Accept without escalation.

#### Indemnification

**Vendor gives (IP infringement):** Required for software, SaaS, and AI tools, and for any vendor licensing content, data, or code into the product. Not required for services-only vendors (consultants, facilities, events, etc.).

**IP indemnity scope:**
- **Business-critical vendor** = Fernway can't operate or deliver to customers if the service goes down, or the vendor is in Fernway's product stack. Everything else is non-core.
- **Non-core SaaS:** Registered-rights-only scope and feature-based exclusions (e.g., "generic marketing or sales functions") are acceptable.
- **Business-critical vendors:** Full scope required: unregistered copyright, trade secret, and patent, with no feature-based exclusions. **Narrower scope → GC.**

**AI output indemnity (tiered):**
- **Core AI vendor** = a model provider, or a tool whose primary function is generating content used externally.
  - Require a conditional copyright indemnity for AI output. Market-standard conditions are acceptable: paid tier, vendor guardrails left on, no deliberate infringement, no inputs Fernway lacks rights to.
  - **No output indemnity from a core AI vendor → GC.**
- **SaaS with bundled AI features** (e.g., a CRM with AI assist):
  - Ask for the output indemnity.
  - Acceptable without it if AI-generated content is human-revised before any external use. **Record that control in the review memo.**
- Note: Fernway's own sales-side output indemnity never exceeds what the upstream model provider gives Fernway, so the foundation-model provider's terms set the ceiling for what sales can offer.

**Fernway gives:** Very narrow indemnity — mirror of what Fernway asks from customers: Fernway's data and content provided to the vendor, and Fernway's violations of the vendor's acceptable use policy.

**Never give:** Nothing categorically refused at this point. (Sales-side "never give" items — general "any breach" indemnity, regulatory fines — are a reasonable reference if one comes up.)

#### Data protection

**DPA:** Required whenever the vendor processes personal data. The vendor's DPA is acceptable if it meets GDPR Art. 28.

**Security:** SOC 2 Type II required only for vendors touching customer data.

**Breach notification:** Mirror of sales side — without undue delay, no later than 72 hours after discovery. Longer → escalate.

**Subprocessors:** Notice of new subprocessors plus an objection right. The vendor's notice window must be at least as long as what Fernway promises its own customers — written as **≥30 days** to cover the long end of Fernway's 15–30 day range. (Matters most when the vendor is a Fernway subprocessor for customer data: its changes flow into Fernway's obligations to customers.)

**AI/ML training rights:**

1. **Explicit training grants:** Hard no on training on Fernway or customer data (inputs, uploaded data, outputs).
2. **Implicit grants via privacy policy / ToS incorporation:** Refuse if the vendor can unilaterally change the incorporated policy to permit training.
3. **Anonymization standard:** Aggregated usage data acceptable only under a defined de-identification standard; bare "anonymized" is not enough.
4. **Competitive contamination:** Case-by-case; the no-training commitment (#1) covers most of the risk.
5. **Opt-out scope and durability:** No-training must be a contractual default, not an opt-out. If only an opt-out is available, it must cover all AI uses and survive renewals and ToS updates.
6. **Output ownership:** Fernway owns outputs; vendor may not retain them as training examples.
7. **Downstream regulatory chain:** Required for AI vendors in Fernway's product stack — vendor must disclose and cooperate on EU AI Act / FTC / state AI-law obligations. Not required for internal-use tools.

#### Term and termination

**Auto-renewal notice to cancel:** Longest acceptable is 30 days. (Same position now applies on the sales side.)

**Renewal price increases:** Capped at 5%.

**Termination for convenience:**
- **Services contracts:** TfC required, with refund of prepaid fees.
- **SaaS:** TfC only where the vendor offers it; no refund required.

#### Insurance

**Require only when both are true:**
- ACV is $250K or more, **and**
- the vendor processes personal data beyond business contact information (name, work email, title, company).

**Then require:** Cyber liability coverage, with a certificate of insurance on request.

**Otherwise:** Don't raise insurance.

#### Governing law and venue

**Preferred:** Delaware or New York law
**Acceptable:** Vendor's home state
**Escalate:** None stated
**Never:** None stated
**Venue / dispute resolution:** Arbitration acceptable.

#### The one thing

Two terms always get checked first on every purchasing-side review and always escalate:
1. Vendor training on Fernway or customer data.
2. A core AI vendor offering no output indemnity. (Bundled-AI SaaS follows the human-revision control under Indemnification instead.)

*Escalation level: GC for both.*

#### NDA triage positions

Same positions on both sides. See `### NDA playbook (both sides)` below.

---

### NDA playbook (both sides)

*NDA triage positions. They apply whether Fernway is sales-side or purchasing-side. Added 2026-10-27 by Bill Littman (GC); attorney-reviewed. [LIMITED DATA — 0 NDAs reviewed against these positions]*

#### Mutuality

Required.

#### Definition of confidential information

Information that is marked confidential, or that a reasonable person would understand to be confidential given its nature and the circumstances of disclosure. No marking requirement and no written confirmation of oral disclosures.

#### Exclusions

All four standard exclusions required:
1. Publicly available
2. Already known to the recipient
3. Received from a third party without restriction
4. Independently developed

#### Term

3 years from disclosure. Trade secrets stay protected for as long as they remain trade secrets.

#### Non-solicit

**Position:** Strike.
**Fallback:** 12 months, limited to employees met through the deal, with a carve-out for general solicitations not targeted at the other party's employees.

#### Residuals

- **Sales or deal NDAs:** Reject.
- **Technical NDAs** (e.g., engineers discussing APIs or integrations): Acceptable, with guardrails:
  - Covers only information retained in unaided memory, with no intentional memorization.
  - Grants no license under the discloser's patents or copyrights.
  - Excludes source code, customer personal data, and anything marked as a trade secret.

#### Hidden business restrictions

E.g., a bar on dealing with portfolio companies. **Reject.** Out of policy; needs a business decision.

#### Return or destroy

30 days, with a carve-out for automatic backups and legal-hold copies.

#### Assignment

Mutual, with consent not unreasonably withheld.

#### Notices

Email notice effective on confirmation of receipt or the next business day.

#### Acceptable as drafted

- Compelled disclosure with prompt notice and cooperation.
- Delaware or New York governing law.
- Standard injunctive relief clause.

---

## Escalation

| Can approve | Without escalation | Escalate to | Via |
|---|---|---|---|
| Contracts manager | NDAs on Fernway paper; order forms with no changes to legal terms | Commercial counsel | Ticket |
| Commercial counsel | Deviations within playbook fallbacks, on deals up to $250K a year | GC | Ticket |
| GC | Anything outside fallbacks short of the CEO triggers; super-cap above 5×; deals above $250K a year | CEO | Ticket |
| CEO | Uncapped data-breach or IP liability; termination for convenience with a refund; anything above GC authority | — | — |

**Dollar thresholds:** $250K annual contract value separates commercial counsel and GC authority.

**Automatic escalations regardless of dollar value (to CEO):**
- Uncapped liability for data breach or IP
- Termination for convenience with a refund

**Turnaround:** Ticket acknowledged within 24 hours. Substantive response in 48–96 hours depending on the length and complexity of customer paper; heavily regulated customers (e.g., a large bank) take longer.

---

## House style

**Triage customer redlines first.** Most customer-counsel edits are posturing that Fernway can accept. Every review sorts customer edits into three groups — **accept as-is**, **accept with a light tweak**, and **actually matters** — and keeps the third group short. Do not flag every change as a deviation.

**Tone in redlines:** Collaborative. Short, friendly rationale on real issues; accept posturing edits quietly. The goal is to make the counterparty's counsel and buyer comfortable.

**Stakeholder summaries:** For the sales rep. Five bullets: can we sign, what changed, what's still open, who owns it, expected timing.

**Where work product goes:** Attached to the legal ticket.

**Where signed contracts live:** Manual upload (no CLM).

---

## Outputs

**Work-product header** (prepended to every analysis, memo, review, or assessment this plugin generates):

- If Role is Lawyer / legal professional: `PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT — PREPARED AT THE DIRECTION OF COUNSEL`
- If Role is Non-lawyer: `RESEARCH NOTES — NOT LEGAL ADVICE — REVIEW WITH A LICENSED ATTORNEY, SOLICITOR, BARRISTER, OR OTHER AUTHORISED LEGAL PROFESSIONAL IN YOUR JURISDICTION BEFORE ACTING`

Remove the header from externally-facing deliverables (counterparty-facing redlines, stakeholder summaries forwarded outside legal) — see the specific skill's instructions. Confirm the correct marking for your jurisdiction and matter.

---

## Seed documents reviewed

| Agreement | Counterparty | Date signed | Notable terms |
|---|---|---|---|
| — | — | — | None yet. Skipped at setup; test with public SaaS agreements (e.g., SEC EDGAR exhibits). |

---

## Review preferences

confirm_routing: true   # Set to false to skip routing confirmation and proceed automatically

---

## NDA triage preferences

closing_action: "Attach this triage output and the NDA to the legal ticket. GREEN: route to the contracts manager to sign. YELLOW/RED: commercial counsel picks up from the ticket."

---

## Playbook monitor settings

pattern_threshold: 5
lookback_months: 12

*Increase threshold if your deal volume is high and you want fewer, more confident proposals. Decrease if you want earlier signals.*

---

*To re-run the interview: `/commercial-legal:cold-start-interview --redo`*
