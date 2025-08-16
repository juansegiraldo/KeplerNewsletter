# **Weekly Sovereign‑Debt Digest — *Agent Prompt* (JSON Output)**

**Goal**
Produce a **structured JSON file** that summarizes the **20 most relevant sovereign‑debt news and analysis items from the last 7 days**, **one concise paragraph per item with source URLs**. Everything must be **in English** and ready for conversion to Kepler Karst branded content.

---

## **Instructions (follow strictly)**

1. **Time window**
   * the last 7 calendar days

2. **Topical filter (must‑match domain): `sovereign_debt`**
   Include only items clearly related to sovereign debt topics such as (non‑exhaustive): **G20 Common Framework for Debt Treatments beyond the Debt Service Suspension Initiative (Common Framework); International Monetary Fund / World Bank (IMF/WB) programmes; sovereign restructurings; the Paris Club; the Heavily Indebted Poor Countries (HIPC) Initiative; state‑contingent debt instruments (SCDIs); collective action clauses (CACs); pari passu clauses; negative pledge clauses; comparability of treatment; preferred creditor status (PCS); debt sustainability analyses (DSA) and debt‑to‑GDP ratios; Eurobonds; green/blue/climate‑resilient bonds; pause clauses; climate‑resilient debt clauses (CRDCs); hidden debts; sovereign immunity; defaults; haircuts; contingent liabilities; primary balances; domestic debt markets; and governance & transparency.**

3. **Sources to crawl (non‑exhaustive):**
   Use all sources you see fit but you might want to focus on the following list. De‑duplicate aggressively across outlets and wires; prefer the **earliest / original** publication. (You may ignore an entry if it yields nothing relevant this week.)

**list of sources**
Financial Times (FT)
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
Moody's
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

4. **Relevance rule & scoring (use to decide the top 20 that make the cut):**

   * Start at **0** and add points:

     * +30 if headline or lede contains ≥2 of the sovereign\_debt keywords above.
     * +20 if the piece is an **official communiqué / filing** (IMF, WB, Paris Club, MoF/DMO, rating agency).
     * +15 if it **moves a restructuring forward** (term sheet, MoU, staff‑level agreement, board approval, disbursement, CAC vote, haircut size disclosed).
     * +10 if it introduces **innovative instruments** (pause clauses, SCDIs, CRDCs, climate‑resilient debt, swaps).
     * +10 if it **quantifies** debt metrics (DSA, debt/GDP, NPV reduction, primary balance).
     * −20 if it's a **duplicate / pure republication**.
   * Keep only the **top‑scoring 20**; drop the rest.

5. **Style constraints**

   * **One paragraph per item (100–140 words max)**.
   * **British English**, concise, analytical, **no hype**.
   * Include **score** for each item.
   * **Dates in `DD-MM-YYYY`**.
   * **No hallucinations**: if a fact can't be validated in the article, omit it.
   * If two or more articles cover the **same development**, **merge into one paragraph** and include **all the sources found**.

6. **JSON Structure Requirements**

   * **Structured data** with clear separation of content from presentation
   * **All URLs must be valid and accessible**
   * **Metadata for each item** (country, date, source, score)
   * **Aggregated statistics** for transparency
   * **Discarded items list** with scores and reasons

7. **Final section (Meta)**

   * Count **sources scanned, items shortlisted, items published, duplicates removed**.
   * List the **top 5 discarded headlines** with their scores (one line each) for transparency and the source link.
   * Include **processing metadata** (generation timestamp, version, etc.)

---

## **Output Template**

```json
{
  "metadata": {
    "title": "Sovereign Debt Weekly — [WEEK_START] to [WEEK_END]",
    "subtitle": "#BRAVE ADVOCACY",
    "period": {
      "start": "[WEEK_START]",
      "end": "[WEEK_END]"
    },
    "generated_at": "[TIMESTAMP]",
    "version": "2.0",
    "brand": "Kepler Karst"
  },
  "tldr": {
    "summary": "A single paragraph capturing the week's sovereign-debt pulse: who restructured, who got an IMF/WB board approval, notable rating changes, innovative clauses, and what to watch next week."
  },
  "items": [
    {
      "id": 1,
      "title": "Headline of the item",
      "url": "https://link.to/article",
      "country": "[Country/ies]",
      "date": "[DD-MM-YYYY]",
      "source": "[Source Name]",
      "score": 85,
      "content": "Write ONE paragraph (100–140 words) synthesising: what happened, where in the process (e.g., staff-level agreement, MoU signed, bondholder vote, CAC activation, Paris Club, Common Framework), any disclosed numbers (debt/GDP, haircut %, NPV, primary balance targets), instruments (pause clauses, SCDIs, CRDCs), and forward-looking 'what's next'.",
      "keywords": ["keyword1", "keyword2", "keyword3"],
      "category": "restructuring|IMF|rating|innovation|analysis"
    }
  ],
  "statistics": {
    "sources_scanned": 45,
    "articles_shortlisted": 67,
    "articles_published": 15,
    "duplicates_removed": 23,
    "average_score": 78.5,
    "score_distribution": {
      "90-100": 3,
      "80-89": 7,
      "70-79": 4,
      "60-69": 1
    }
  },
  "discarded_items": [
    {
      "title": "Discarded headline",
      "url": "https://link.to/discarded/article",
      "score": 45,
      "reason": "Below threshold",
      "source": "[Source Name]",
      "date": "[DD-MM-YYYY]"
    }
  ],
  "processing_notes": {
    "topics_covered": ["restructuring", "IMF programs", "rating changes"],
    "geographic_focus": ["Global", "Latin America", "Africa"],
    "key_developments": ["Major restructuring completed", "New IMF program approved"],
    "next_week_watch": ["Upcoming bondholder votes", "IMF board meetings"]
  }
}
```

---

## **Benefits of JSON Output**

1. **Easy Editing**: Modify content without touching presentation code
2. **Valid URLs**: All links are stored as plain text, easy to validate
3. **Structured Data**: Clear separation of metadata, content, and statistics
4. **Multiple Output Formats**: Can be converted to HTML, Markdown, PDF, etc.
5. **Version Control Friendly**: JSON is easier to diff and merge
6. **API Ready**: Can be consumed by other applications
7. **Validation**: JSON schema can validate structure and data types
8. **Automation**: Easy to process programmatically for different outputs

---

## **Post-Processing Instructions**

After generating the JSON, you can:

1. **Validate URLs** using a link checker
2. **Convert to HTML** using a template engine
3. **Generate Markdown** for documentation
4. **Create CSV exports** for analysis
5. **Build APIs** for web applications
6. **Generate PDFs** for distribution

The JSON structure ensures that content and presentation are completely separated, making it much easier to maintain and update the weekly digest. 