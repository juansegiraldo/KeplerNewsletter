# **Weekly Sovereign‑Debt Digest — *Agent Prompt* (HTML Output)**

**Goal**
Produce an **HTML webpage** that summarizes the **10–20 most relevant sovereign‑debt news and analysis items from the last 7 days**, **one concise paragraph per item with the hyperlink below**. Everything must be **in English** and styled according to Kepler Karst brand guidelines.

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
   * **Embed the hyperlink in the item title.**
   * **British English**, concise, analytical, **no hype**.
   * Include **`[Score: xx/100]`** at the end of each paragraph.
   * **Dates in `DD-MM-YYYY`**.
   * **No hallucinations**: if a fact can't be validated in the article, omit it.
   * If two or more articles cover the **same development**, **merge into one paragraph** and link **all the sources found**.

6. **HTML & Branding Requirements**

   * **Use Kepler Karst brand colors and typography**:
     * Primary color: `#000000` (black)
     * Secondary color: `#F1EEA4` (light yellow)
     * Text color: `#000000` (black)
     * Primary font: "Blacker Pro" (700 weight for headings)
     * Secondary font: "Sharp Grotesk" (for body text)
   * **Include Kepler Karst logo and branding elements**
   * **Responsive design** that works on desktop and mobile
   * **Professional, legal-firm aesthetic** with the "#BRAVE ADVOCACY" theme
   * **Include proper meta tags** for SEO and social sharing

7. **Final section (Meta)**

   * Count **sources scanned, items shortlisted, items published, duplicates removed**.
   * List the **top 5 discarded headlines** with their scores (one line each) for transparency and the source link.
   * At the end of your output, generate a **downloadable CSV file** containing the following columns for both top news items and discarded items: Title, Paragraph, Source (URL). Ensure the CSV includes all published and discarded articles, with each row representing one article.

---

## **Output Template**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sovereign Debt Weekly — [WEEK_START] to [WEEK_END] | Kepler Karst</title>
    <meta name="description" content="Weekly digest of the most relevant sovereign debt news and analysis from the past 7 days.">
    <meta name="keywords" content="sovereign debt, restructuring, IMF, World Bank, Paris Club, debt sustainability">
    <meta property="og:title" content="Sovereign Debt Weekly — [WEEK_START] to [WEEK_END]">
    <meta property="og:description" content="Weekly digest of sovereign debt developments">
    <meta property="og:type" content="article">
    <meta property="og:url" content="[URL]">
    <meta name="twitter:card" content="summary_large_image">
    
    <style>
        :root {
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #F1EEA4;
            --e-global-color-text: #000000;
            --e-global-color-accent: #000000;
            --e-global-color-eafa1f3: #00000024;
            --e-global-color-04963ab: #FFFFFF;
            --e-global-typography-primary-font-family: "Blacker Pro";
            --e-global-typography-primary-font-weight: 700;
            --e-global-typography-secondary-font-family: "Blacker Pro";
            --e-global-typography-secondary-font-weight: 400;
            --e-global-typography-accent-font-weight: 500;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: "Sharp Grotesk", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: var(--e-global-color-text);
            line-height: 1.6;
            background-color: #fff;
        }
        
        .header {
            background-color: var(--e-global-color-secondary);
            padding: 1rem 2rem;
            border-bottom: 2px solid var(--e-global-color-primary);
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 1.5rem;
            color: var(--e-global-color-primary);
        }
        
        .logo-subtitle {
            font-size: 0.8rem;
            font-weight: 400;
            margin-top: -0.2rem;
        }
        
        .hero {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><rect width="1200" height="600" fill="%23f1eea4"/><text x="600" y="300" text-anchor="middle" font-family="Arial" font-size="48" fill="%23000">#BRAVE ADVOCACY</text></svg>');
            background-size: cover;
            background-position: center;
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }
        
        .hero h1 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }
        
        .hero .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .tldr {
            background-color: var(--e-global-color-secondary);
            padding: 2rem;
            margin: 2rem 0;
            border-left: 4px solid var(--e-global-color-primary);
        }
        
        .tldr h2 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }
        
        .items {
            margin: 3rem 0;
        }
        
        .item {
            margin-bottom: 2rem;
            padding: 1.5rem;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            transition: box-shadow 0.3s ease;
        }
        
        .item:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .item h3 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 0.5rem;
        }
        
        .item h3 a {
            color: var(--e-global-color-primary);
            text-decoration: none;
        }
        
        .item h3 a:hover {
            text-decoration: underline;
        }
        
        .item-meta {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1rem;
        }
        
        .item-content {
            margin-bottom: 1rem;
        }
        
        .score {
            font-weight: bold;
            color: var(--e-global-color-primary);
            background-color: var(--e-global-color-secondary);
            padding: 0.2rem 0.5rem;
            border-radius: 3px;
            font-size: 0.8rem;
        }
        
        .meta-section {
            background-color: #f8f8f8;
            padding: 2rem;
            margin-top: 3rem;
            border-radius: 4px;
        }
        
        .meta-section h2 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }
        
        .meta-stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .stat {
            background: white;
            padding: 1rem;
            border-radius: 4px;
            border-left: 3px solid var(--e-global-color-primary);
        }
        
        .stat-number {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--e-global-color-primary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: #666;
        }
        
        .discarded-items {
            margin-top: 1rem;
        }
        
        .discarded-items h3 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }
        
        .discarded-item {
            padding: 0.5rem 0;
            border-bottom: 1px solid #e0e0e0;
            font-size: 0.9rem;
        }
        
        .footer {
            background-color: var(--e-global-color-primary);
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }
        
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .container {
                padding: 1rem;
            }
            
            .meta-stats {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <div class="logo">
                KEPLER—KARST<br>
                <span class="logo-subtitle">LAW FIRM</span>
            </div>
            <nav>
                <span style="font-weight: bold; color: var(--e-global-color-primary);">Sovereign Debt Weekly</span>
            </nav>
        </div>
    </header>

    <section class="hero">
        <h1>#BRAVE ADVOCACY</h1>
        <p class="subtitle">Sovereign Debt Weekly — [WEEK_START] to [WEEK_END]</p>
    </section>

    <main class="container">
        <section class="tldr">
            <h2>TL;DR</h2>
            <p>A single paragraph capturing the week's sovereign-debt pulse: who restructured, who got an IMF/WB board approval, notable rating changes, innovative clauses, and what to watch next week.</p>
        </section>

        <section class="items">
            <h2 style="font-family: var(--e-global-typography-primary-font-family); font-weight: var(--e-global-typography-primary-font-weight); margin-bottom: 2rem; color: var(--e-global-color-primary);">Items (10–20, one paragraph each)</h2>

            <article class="item">
                <h3><a href="https://link.to/article">Headline of the item</a></h3>
                <div class="item-meta">[Country/ies] — [Date: DD-MM-YYYY]</div>
                <div class="item-content">
                    Write ONE paragraph (100–140 words) synthesising: what happened, where in the process (e.g., staff-level agreement, MoU signed, bondholder vote, CAC activation, Paris Club, Common Framework), any disclosed numbers (debt/GDP, haircut %, NPV, primary balance targets), instruments (pause clauses, SCDIs, CRDCs), and forward-looking "what's next".
                </div>
                <span class="score">[Score: xx/100]</span>
            </article>

            <!-- Repeat article structure for each item -->
        </section>

        <section class="meta-section">
            <h2>Meta</h2>
            <div class="meta-stats">
                <div class="stat">
                    <div class="stat-number">N</div>
                    <div class="stat-label">Sources scanned</div>
                </div>
                <div class="stat">
                    <div class="stat-number">Nshort</div>
                    <div class="stat-label">Articles shortlisted</div>
                </div>
                <div class="stat">
                    <div class="stat-number">Npub</div>
                    <div class="stat-label">Articles published</div>
                </div>
                <div class="stat">
                    <div class="stat-number">Ndup</div>
                    <div class="stat-label">Duplicates removed</div>
                </div>
            </div>
            
            <div class="discarded-items">
                <h3>Top 5 discarded headlines (with scores):</h3>
                <div class="discarded-item">1. [Headline] — [Score]</div>
                <div class="discarded-item">2. [Headline] — [Score]</div>
                <div class="discarded-item">3. [Headline] — [Score]</div>
                <div class="discarded-item">4. [Headline] — [Score]</div>
                <div class="discarded-item">5. [Headline] — [Score]</div>
            </div>
        </section>
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. All rights reserved.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Weekly sovereign debt analysis and insights</p>
    </footer>
</body>
</html>
```
