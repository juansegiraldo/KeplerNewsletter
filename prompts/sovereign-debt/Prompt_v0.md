# **Weekly Sovereign‑Debt Digest — *Agent Prompt* (“PPT” slides)**

**Goal**
Produce a **PowerPoint deck** that summarizes the **10–20 most relevant sovereign‑debt news and analysis items from the last 7 days**, **one concise paragraph per item with the hyperlink embedded**. Everything must be **in English**.

---

## **Instructions (follow strictly)**

1. **Time window**
   * the last 7 calendar days

2. **Topical filter (must‑match domain): `sovereign_debt`**
   Include only items clearly related to sovereign debt topics such as (non‑exhaustive): **G20 Common Framework for Debt Treatments beyond the Debt Service Suspension Initiative (Common Framework); International Monetary Fund / World Bank (IMF/WB) programmes; sovereign restructurings; the Paris Club; the Heavily Indebted Poor Countries (HIPC) Initiative; state‑contingent debt instruments (SCDIs); collective action clauses (CACs); pari passu clauses; negative pledge clauses; comparability of treatment; preferred creditor status (PCS); debt sustainability analyses (DSA) and debt‑to‑GDP ratios; Eurobonds; green/blue/climate‑resilient bonds; pause clauses; climate‑resilient debt clauses (CRDCs); hidden debts; sovereign immunity; defaults; haircuts; contingent liabilities; primary balances; domestic debt markets; and governance & transparency.**

3. **Sources to crawl (non‑exhaustive):**
   Use all sources you see fit but you might want to focus con the following list. De‑duplicate aggressively across outlets and wires; prefer the **earliest / original** publication. (You may ignore an entry if it yields nothing relevant this week.)

**list of sources**
Financial Times
ABC News
CNN
CBS News
New York Times
Wall Street Journal
USA Today
Christian Science Monitor
NBC News
Reuters
Associated Press
Huffington Post
BBC News
Yahoo News
Newsweek
The Daily Beast
Quartz
The Guardian
Politico
The New Yorker
PBS NewsHour
US News
NPR
The Atlantic
LA Times
BreakingNews
VICE News
Talking Points Memo
Salon
TIME
Fox News
Mashable
Bloomberg
Reddit
WSJ World News
Washington Post
S&P Global
Moody’s
FT Alphaville
ODI
Sustainable Sovereign Debt Hub
Bretton Woods Project
World Bank
IMF
Oxford Business Law Blog
CLS Blue Sky Blog
Debt Justice
Eurodad
African Development Bank
European Investment Bank
CAF (Development Bank of Latin America)
Clifford Chance

4. **Relevance rule & scoring (use to decide the 10–20 that make the cut):**

   * Start at **0** and add points:

     * +30 if headline or lede contains ≥2 of the sovereign\_debt keywords above.
     * +20 if the piece is an **official communiqué / filing** (IMF, WB, Paris Club, MoF/DMO, rating agency).
     * +15 if it **moves a restructuring forward** (term sheet, MoU, staff‑level agreement, board approval, disbursement, CAC vote, haircut size disclosed).
     * +10 if it introduces **innovative instruments** (pause clauses, SCDIs, CRDCs, climate‑resilient debt, swaps).
     * +10 if it **quantifies** debt metrics (DSA, debt/GDP, NPV reduction, primary balance).
     * −20 if it’s a **duplicate / pure republication**.
   * Keep only the **top‑scoring 10–20**; drop the rest.

5. **Style constraints**

   * **One paragraph per item (100–140 words max)**.
   * **Embed the hyperlink in the item title.**
   * **British English**, concise, analytical, **no hype**.
   * Include **`[Score: xx/100]`** at the end of each paragraph.
   * **Dates in `DD-MM-YYYY`**.
   * **No hallucinations**: if a fact can’t be validated in the article, omit it.
   * If two or more articles cover the **same development**, **merge into one paragraph** and link the **most authoritative** source; name the rest as “see also: …”.

6. **Final slide (Meta)**

   * Count **sources scanned, items shortlisted, items published, duplicates removed**.
   * List the **top 5 discarded headlines** with their scores (one line each) for transparency.

---

## **Output Template**

```
# Sovereign Debt Weekly — [WEEK_START] to [WEEK_END]

---

## TL;DR (≤120 words)
A single paragraph capturing the week’s sovereign-debt pulse: who restructured, who got an IMF/WB board approval, notable rating changes, innovative clauses, and what to watch next week.

---

## Items (10–20, one paragraph each)

### 1) **[Headline of the item](https://link.to/article)** — [Country/ies] — [Date: DD-MM-YYYY]
Write ONE paragraph (100–140 words) synthesising: what happened, where in the process (e.g., staff-level agreement, MoU signed, bondholder vote, CAC activation, Paris Club, Common Framework), any disclosed numbers (debt/GDP, haircut %, NPV, primary balance targets), instruments (pause clauses, SCDIs, CRDCs), and forward-looking “what’s next”. End with **[Score: xx/100]**.

---

### 2) **[Headline](link)** — …
[Paragraph…] **[Score: xx/100]**

---

<!-- Repeat until you reach 10–20 items -->

---

## Meta
- **Sources scanned:** N  
- **Articles shortlisted:** Nshort  
- **Articles published:** Npub  
- **Duplicates removed:** Ndup  
- **Top 5 discarded headlines (with scores):**  
  1. [Headline] — [Score]  
  2. [Headline] — [Score]  
  3. [Headline] — [Score]  
  4. [Headline] — [Score]  
  5. [Headline] — [Score]
```
