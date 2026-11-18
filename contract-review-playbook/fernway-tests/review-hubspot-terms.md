PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT — PREPARED AT THE DIRECTION OF COUNSEL

# Vendor Agreement Review: HubSpot Customer Terms of Service (SaaS)

**Reviewed:** 2026-10-26
**Agreement:** HubSpot Customer Terms of Service, General Terms (last modified Sept. 16, 2026), plus the HubSpot Data Processing Agreement (last updated Sept. 16, 2026), which the Terms incorporate by reference
**Our role:** Customer. **Playbook applied:** Purchasing-side
**Use case:** Marketing and sales CRM. HubSpot holds prospect and customer-contact personal data, but not content from the Fernway platform.
**Contract value:** No order form, so no ACV. Routing goes to GC regardless, because the one-thing trigger fires (see Approval routing).
**Counterparty posture:** HubSpot is a large vendor and its online terms are effectively non-negotiable. However, under **§12.15 the Order Form takes precedence over the General Terms**. That makes the Order Form, or a rider attached to it, the realistic place for every fix below.

**Not reviewed:** Product Specific Terms (uptime SLA, data retrieval and deletion mechanics), the Sub-Processors page, the AUP, and the Product Catalog. Contract language below is paraphrased; check the exact wording against the live terms before sending anything.

---

## Bottom line

**Don't sign as-is.** By default, §5.3.1 lets HubSpot train its AI models on Fernway's CRM data. That is your purchasing-side "one thing," and it goes to GC. The fix is cheap: turn off the account-level opt-out now, and put a contractual no-training commitment in the Order Form, so the protection doesn't depend on a settings toggle that can change.

The other material asks also belong in the Order Form:
- a super-cap for data breach and confidentiality
- a narrower, capped Fernway indemnity
- a 5% renewal price cap

**Issues (legal risk):** 1🔴 4🟠 4🟡 2🟢
**Issues (business friction):** 0🔴 1🟠 1🟡 9🟢

**Approval needed from:** GC

---

## ⛔ Deal-breaker check: PRESENT

**§5.3.1 (Machine Learning and AI).** HubSpot may use Customer Data to develop and improve its AI features, and states that it "may also use Customer Data to train our AI models." Customers can opt out in account settings.

This hits playbook AI/ML #1 (hard no on training on Fernway data) and #5 (no-training must be a contractual default, not an opt-out). It is one of your two purchasing-side "always check first" terms, and it **escalates to GC**.

- [ ] **Now, operationally:** Turn off AI-training use in HubSpot account settings before any data goes in.
- [ ] **Push back:** Add the training prohibition to the Order Form (language in Issue 1).
- [ ] **Walk:** Only if HubSpot won't accept an Order Form commitment *and* GC won't accept relying on the opt-out alone.

The detailed review below assumes this gets resolved.

---

## Issues by severity

### Issue 1 — §5.3.1: Default right to train AI models on Customer Data
**Playbook says:** AI/ML #1: hard no on training on Fernway or customer data (inputs, uploaded data, outputs). #5: no-training must be a contractual default, not an opt-out.
**Contract says:** HubSpot may use Customer Data to develop, support, and improve its AI features, and to train its AI models. The customer can opt out through account settings. Opting out does not block use of the AI features.
**Gap:** Unacceptable (one-thing trigger)
**Legal risk:** 🔴 Critical | **Business friction:** 🟢 Invisible (the opt-out toggle exists; we're just asking HubSpot to commit to it in writing)
**Why it matters:** Prospect and customer-contact data would feed HubSpot's models. The only protection is a setting that any admin can flip back, and HubSpot can amend the terms around it.
**Proposed redline (Order Form rider):**
> "Notwithstanding Section 5.3.1 of the Customer Terms of Service, HubSpot will not use Customer Data, Customer Materials, or any inputs to or outputs of the AI features to train, fine-tune, or otherwise develop any artificial intelligence or machine learning model, and this restriction applies regardless of account settings and survives any revision to the Agreement under Section 12.1 for the Subscription Term and all renewals."

**If they won't move:** Fall back to the account-level opt-out, plus a written confirmation from HubSpot (email is fine) that the opt-out applies org-wide and survives renewals. Accepting that fallback is a GC call.

### Issue 2 — §12.1: Unilateral amendment by posting (durability of protections)
**Playbook says:** AI/ML #2: refuse an incorporated policy or terms that the vendor can change unilaterally to permit training. #5: protections must survive renewals and ToS updates.
**Contract says:** HubSpot can modify the Agreement by posting a revised version, effective the next business day after notice. A customer that objects in writing within 30 days keeps its existing terms only until its next renewal.
**Gap:** Weaker than standard
**Legal risk:** 🟠 High | **Business friction:** 🟢 Invisible
**Why it matters:** Any data-use protection Fernway gets only through the General Terms can be revised out at the next renewal.
**Proposed redline:** The "survives any revision under Section 12.1" language in Issue 1 handles this for AI training. If the rider carries other protections, add one line to it:
> "No revision to the Agreement under Section 12.1 will modify the terms of this Order Form."

**If they won't move:** Diary the 30-day objection window on every HubSpot terms-change notice. Escalate to GC if a revision touches data use.

### Issue 3 — §10.4: No super-cap. Data breach and confidentiality sit under the 1× cap
**Playbook says:** General 12-month cap is acceptable. Super-cap (mirroring sales side) up to 10× annual fees for confidentiality breach, IP indemnity, GN/WM, and data breach. **Floor 2×. Below 2× goes to GC.**
**Contract says:**
- **Cap:** Each party's aggregate liability is capped at amounts paid or payable for the Subscription Service in the prior 12 months (US$100 for Free Services).
- **Above the cap:** Customer's payment obligations, customer's indemnity obligations, HubSpot's IP indemnity, and customer's IP infringement.
- **Excluded for both parties:** Indirect, consequential, and punitive damages, and lost profits, revenue, or data.
- **Super-cap:** None.

**Gap:** Weaker than fallback (data breach, confidentiality, and GN/WM are effectively at 1×, below the 2× floor)

**The four dimensions:**
1. **Direct vs. indirect:** The cap is an aggregate cap on all liability. Indirect damages are excluded entirely for both sides, including lost data, which is the damage most likely in a CRM breach.
2. **Cap base:** Fees paid or payable for the Subscription Service in a 12-month period. Confirm against the live text which 12 months (preceding the claim, or the current term). Overages and add-ons may or may not count as "Subscription Service" fees.
3. **Carveout interaction:** The only HubSpot-side item above the cap is its IP indemnity. Everything Fernway would realistically claim for — a breach of contact data, a confidentiality failure — sits under a 1× cap, with lost data excluded. **The capped surface is the whole of Fernway's realistic exposure, so the cap is low in practice.**
4. **Your playbook:** Your playbook covers direct cap, super-cap, and floor, but not lost-data exclusions. Consider adding a position on whether "loss of data" may be excluded as indirect damages.

**Legal risk:** 🟠 High | **Business friction:** 🟡 HubSpot will resist. Expect this to slow the deal if pushed.
**Proposed redline (Order Form rider):**
> "Notwithstanding Section 10.4, each party's aggregate liability for (a) breach of Section 7 (Confidentiality), (b) breach of its data protection obligations under the Agreement or the DPA, and (c) its gross negligence or willful misconduct will not exceed [three (3)] times the amounts paid or payable in the twelve (12) months preceding the event giving rise to the claim, and the exclusion of loss of data in Section 10.3 will not apply to claims under (b)."

**If they won't move:** 2× is your floor. Anything less goes to GC. Given HubSpot's leverage and the low sensitivity of CRM data, GC may reasonably accept 1×. Record the decision in the deviation log either way.

### Issue 4 — §9.1 + §10.4: Fernway's indemnity is broad and uncapped
**Playbook says:** Fernway gives a very narrow indemnity that mirrors what we ask from customers: Fernway's data and content, and Fernway's AUP violations.
**Contract says:** Fernway must defend and indemnify HubSpot against third-party claims arising from:
- unauthorized or illegal use
- **any breach of the Agreement**
- use of Third-Party Products
- use under Fernway's credentials

Customer indemnity obligations are carved out of the cap, so this indemnity is **uncapped**.
**Gap:** Outside position (no stated fallback)
**Legal risk:** 🟠 High | **Business friction:** 🟢 Invisible
**Why it matters:** "Any breach" combined with no cap means an ordinary contract breach could become unlimited third-party exposure for Fernway, while HubSpot's own data-breach liability stays at 1×. That asymmetry is the core of the problem.
**Proposed redline (surgical edits to §9.1 and §10.4, via rider):**
> In Section 9.1, replace "(ii) your breach of the Agreement" with "(ii) your breach of Section 2.8 (Acceptable Use) or 2.9 (Prohibited and Unauthorized Use), or Customer Data or Customer Materials provided by you in violation of law or third-party rights". In Section 10.4, limit the uncapped carve-out for customer indemnity to the narrowed scope above, with all other customer liability subject to the cap.

**If they won't move:** No fallback is stated, so escalate to GC. An acceptable compromise is to leave the scope alone but cap Fernway's indemnity at the same super-cap you get in Issue 3.

### Issue 5 — §9.2: No AI output indemnity *(conditional, see note)*
**Playbook says:** AI vendors must give a market-standard conditional output indemnity. **No output indemnity at all goes to GC.** This is your second "always check first" term.
**Contract says:** HubSpot's IP indemnity covers only the Subscription Service itself. Nothing addresses AI-generated outputs, and the Terms don't define outputs at all.
**Gap:** Missing term
**Legal risk:** 🟠 High *if* Fernway uses HubSpot's AI (Breeze) to generate marketing or sales content. 🟢 if AI features are off or used only for internal summarization. | **Business friction:** 🟢 Invisible
**Playbook gap:** The playbook doesn't define what makes a vendor an "AI vendor." HubSpot is a CRM with AI features, not a model provider. **Decide whether this trigger applies to SaaS tools with bundled AI features, and I'll record it.**
**Proposed redline (if it applies):**
> "HubSpot's obligations under Section 9.2 extend to any Action alleging that output generated by the AI features of the Subscription Service, as provided by HubSpot and used in accordance with the Agreement and documentation, infringes a third party's copyright."

**If they won't move:** Go to GC. A practical alternative is a policy limiting Breeze-generated content to internal drafts that get human revision before external use.

### Issue 6 — §3.2: Renewal pricing up to list price
**Playbook says:** Renewal price increases capped at 5%.
**Contract says:** At renewal, HubSpot may raise Subscription Fees up to its then-current list price, with at least 30 days' notice before renewal. Fees are fixed during the current term.
**Gap:** Weaker than standard
**Legal risk:** 🟡 Medium | **Business friction:** 🟠 Slows deals. This is the renewal surprise that hits finance, especially if Fernway buys at a discount off list.
**Proposed redline (Order Form):**
> "Upon each renewal, Subscription Fees for the same products and quantities will not increase by more than five percent (5%) over the fees for the immediately preceding term."

**If they won't move:** No fallback is stated. At minimum, get the first-year discount locked for the next renewal. Accepting an uncapped increase is a commercial counsel call within deal authority, or GC if the ACV is over $250K.

### Issue 7 — §9.2: IP indemnity is narrow in scope
**Playbook says:** IP indemnity is required for SaaS. The playbook doesn't specify scope.
**Contract says:**
- **Covered:** Only valid patents in PCT member states, registered trademarks, and registered copyrights.
- **Excluded:** Combinations with non-HubSpot items, third-party modifications, use outside the Agreement, and claims based on **generic marketing or sales functions** or non-HubSpot interface design.
- **Remedies:** Modify or replace the service, procure a license, or terminate and refund prepaid unused fees.
- **Sole remedy:** Yes.

**Gap:** Weaker than standard (unregistered copyright and trade secret are not covered, and the "generic marketing or sales functions" exclusion covers much of what a CRM does)
**Legal risk:** 🟡 Medium | **Business friction:** 🟢 Invisible
**Proposed redline:** Strike "registered" before "copyright." Strike the generic-marketing/sales-functions exclusion.
**If they won't move:** Accept. For a non-core CRM, an IP claim against Fernway is unlikely, and the remedy ladder matches what you offer customers. **Consider adding a scope position to the playbook,** e.g., "registered-rights-only IP indemnity is acceptable for non-core SaaS."

### Issue 8 — Output ownership is silent
**Playbook says:** AI/ML #6: Fernway owns outputs, and the vendor may not keep them as training examples.
**Contract says:** Fernway owns its Customer Materials and Customer Data (§5.1). Outputs are neither defined nor mentioned.
**Gap:** Missing term
**Legal risk:** 🟡 Medium | **Business friction:** 🟢 Invisible
**Proposed redline (Order Form rider, pairs with Issue 1):**
> "Output generated by the AI features of the Subscription Service from Customer Data or Customer Materials is Customer Data for all purposes of the Agreement."

**If they won't move:** Issue 1's prohibition already covers training on outputs. Ownership is then a lower-stakes ask.

### Issue 9 — §5.3.2 + DPA §10: HubSpot as controller of tracking and enrichment data; no anonymization standard
**Playbook says:** AI/ML #3: aggregated or usage data is acceptable only under a defined de-identification standard.
**Contract says:**
- HubSpot may use data from its website Tracking Code, including IP addresses, to improve its datasets and services.
- Under the DPA, HubSpot acts as an independent **controller** for enrichment data, and for tracking-code data when Intent data sharing is on, including to develop its commercial dataset.
- The DPA says nothing in the agreement restricts HubSpot's use of data it processes independently.
- No anonymization or de-identification standard is defined anywhere.

**Gap:** Missing term
**Legal risk:** 🟡 Medium | **Business friction:** 🟢 Invisible
**Why it matters:** Data from visitors to Fernway's website flows into HubSpot's own commercial dataset outside processor limits. Fernway's privacy notice needs to cover that.
**Proposed approach:** This one is mainly operational, not a redline:
- Leave Intent data sharing and enrichment-data contribution **off**.
- Confirm Fernway's website privacy notice discloses HubSpot tracking.

If you want contract language, ask for a defined de-identification standard for any aggregated data HubSpot derives from Customer Data.
**If they won't move:** Accept, with the operational controls above.

### Issue 10 — §12.3: One-year limitation period on claims
**Playbook says:** Not addressed.
**Contract says:** Claims arising out of the Agreement must generally be brought within one year after they accrue (nonpayment and IP claims excepted).
**Legal risk:** 🟢 Low | **Business friction:** 🟢 Invisible
**Note:** This is shorter than the default statutory period under Massachusetts contract law `[model knowledge — verify]`. A data incident discovered late could be time-barred. Not worth negotiating capital; just diary it.

### Issue 11 — DPA §5: Subprocessor notice only if Fernway subscribes
**Playbook says:** Notice plus objection right, with notice ≥30 days.
**Contract says:**
- **Notice:** At least 30 days before a change, but only if the customer subscribes to email updates for the Sub-Processors page.
- **Objection:** Within 30 days on reasonable data-protection grounds, followed by good-faith discussion.
- **If unresolved:** HubSpot chooses between dropping the subprocessor and letting Fernway suspend or terminate the affected service without liability. Fees already incurred remain payable.

**Gap:** Within position, conditional on an action
**Legal risk:** 🟢 Low | **Business friction:** 🟢 Invisible
**Action:** Subscribe a legal or privacy inbox to HubSpot's sub-processor notifications at onboarding. Also check the Sub-Processors page for third-party LLM providers behind the AI features. (Not reviewed here.)

---

## Within playbook (no action)

| Term | Contract | Playbook |
|---|---|---|
| General cap | 12 months' fees, aggregate (§10.4) | 12-month cap acceptable ✅ |
| DPA | Incorporated. SCCs, UK Addendum, Swiss terms, and DPF certification | Vendor DPA OK if Art. 28-compliant ✅ (confirm Art. 28(3) terms in full DPA review if desired) |
| Breach notification | Without undue delay, ≤72 hours (DPA §3.5) | ≤72 hours ✅ |
| SOC 2 Type II | Annual SOC 2; Type II report available on request | Not required for this use case; available anyway ✅ |
| Termination for convenience | None. Cause-only (§4.3) | SaaS: only where offered ✅ |
| Governing law / venue | Massachusetts law, Boston courts, no arbitration (§11) | Vendor home state acceptable ✅ |
| Service changes | No material degradation of overall functionality during the term, with listed exceptions (§2.6) | Not addressed. Reasonable ✅ |

## Favorable terms (trade bait)

- **Auto-renewal opt-out has no fixed notice period.** Fernway just turns off auto-renew in Account & Billing before the term ends (§4.2). That's better than your 30-day maximum.
- **Fee lock during the term** (§3.1), with 30 days' notice of any renewal increase (§3.2).
- **Right to object to terms revisions** and keep current terms until renewal (§12.1). If HubSpot can't continue on those terms, Fernway terminates with a refund of prepaid fees.
- **Refund of prepaid unused fees** on termination for cause, on IP-indemnity termination, and when a performance-warranty problem goes unfixed for 60 days.

## Missing provisions

- **Insurance:** Not addressed (§12.13 is not a coverage commitment). Your purchasing playbook is silent on vendor insurance. Low priority for a CRM.
- **Defined usage data:** "Usage data" isn't defined, and analytics are carved out of hosting commitments (§5.5.1).
- **Not reviewed:** Data export format, timing, and cost (Product Specific Terms and DPA §3.6 say retrieval assistance is at customer cost). Uptime SLA and credits (Product Specific Terms). Review these before signing if the CRM will be business-critical.

---

## SaaS-specific findings

**Auto-renewal**
- **Renewal date:** Unknown (no Order Form).
- **Renewal term:** The shorter of the prior term or one year (§4.1).
- **Notice window:** Turn off auto-renewal in Account & Billing before the current term ends (§4.2). There's no fixed advance notice period, so it fits your 30-day maximum.
- **Notice method:** Portal setting only. There's no written-notice mechanism, so record who holds the admin login.
- **Renewal price:** Up to then-current list price (Issue 6).
- **Renewal tracker:** Yes. Hand off when the Order Form is signed. Missing fields: `signed_date`, `initial_term_end`, `cancel_by_effective`, `annual_value`, `business_owner`. Suggested internal cancel-by date: 30 days before term end, so the price-increase notice can be acted on.

**Price escalation:** Uncapped up to list at renewal (Issue 6). Overages and Limits follow the Product Catalog (not reviewed).

**Data exit:** Delete or return on termination per the Product Specific Terms. Retrieval assistance is at customer cost (DPA §3.6). Format and post-termination window weren't reviewed. **This is the piece the business owner should read before committing years of CRM history.**

**SLA:** Not reviewed (Product Specific Terms). Decide whether the CRM is business-critical before spending capital here.

**Subprocessors:** Within position, conditional on subscribing (Issue 11).

**Service changes:** HubSpot may change features and Limits but not materially degrade overall functionality during the term, subject to exceptions (§2.6). Acceptable.

---

## Jurisdiction check

- Massachusetts law governs. Your playbook accepts the vendor's home state.
- The state auto-renewal statutes flagged in the overlay (CA, NY, IL) are aimed mainly at consumer contracts and don't change this B2B analysis `[model knowledge — verify]`.
- Massachusetts enforces a contractual shortening of the limitations period if it's reasonable `[model knowledge — verify]`. This is relevant to Issue 10.

---

## Approval routing

- [ ] **GC approval required.**
  - The purchasing-side "one thing" is triggered: vendor training on Fernway data (Issue 1).
  - The super-cap is below the 2× floor (Issue 3).
  - Fernway's indemnity is outside position with no fallback (Issue 4).
  - The output-indemnity trigger fires if Breeze content generation is in use (Issue 5).

  This routing holds regardless of ACV.
- [ ] **Business owner (Marketing or RevOps) sign-off** on:
  - Turning off AI-training use in account settings.
  - Leaving Intent data sharing off.
  - Whether Breeze will generate external-facing content.
  - Whether the CRM is business-critical (drives SLA and data-exit review).
- [ ] **Finance** on the renewal-pricing exposure (Issue 6) once the Order Form price is known.

**Recommended next step:** Brief GC on Issue 1 and the Order Form rider strategy. In parallel, have the HubSpot admin toggle the AI-training opt-out now. Then send HubSpot's rep one consolidated Order Form rider covering Issues 1, 3, 4, 6, and 8. Treat Issues 2, 7, and 9 as fallbacks or operational controls.

---

## Next steps

1. **Draft the Order Form rider** as one clean exhibit carrying all the redlines above.
2. **Draft the GC escalation ask** via `/commercial-legal:escalation-flagger`.
3. **Get more facts:** The Order Form (ACV, dates), the Product Specific Terms (SLA, exit), and the Sub-Processors page (third-party LLMs).
4. **Stakeholder summary** for the business owner (five bullets, per house style).
5. **Something else.**

---

*Sources:* [HubSpot Customer Terms of Service](https://legal.hubspot.com/terms-of-service) · [HubSpot Data Processing Agreement](https://legal.hubspot.com/dpa)
