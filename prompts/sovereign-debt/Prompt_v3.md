# **Weekly Sovereign‑Debt Digest — *Agent Prompt* (JSON Output) v3.0**

## **PRIMARY OBJECTIVE**
Generate a **structured JSON file** containing the **20 most relevant sovereign‑debt news items from the past 7 days**. Each item must include one concise analytical paragraph (100-140 words) with validated source URLs. Output must be in British English and ready for Kepler Karst brand conversion.

---

## **EXECUTION FRAMEWORK**

### **1. TEMPORAL SCOPE**
- **Time Window**: Exactly 7 calendar days from current date backwards
- **Date Format**: DD-MM-YYYY throughout all outputs
- **Time Zone**: Use UTC for consistency

### **2. CONTENT FILTER: SOVEREIGN DEBT DOMAIN**
**INCLUDE ONLY** articles explicitly related to these sovereign debt topics:

**Core Mechanisms:**
- G20 Common Framework for Debt Treatments
- International Monetary Fund (IMF) programmes and World Bank operations
- Paris Club negotiations and agreements
- Heavily Indebted Poor Countries (HIPC) Initiative

**Financial Instruments:**
- State-contingent debt instruments (SCDIs)
- Collective action clauses (CACs)
- Pari passu clauses and negative pledge clauses
- Climate-resilient debt clauses (CRDCs)
- Eurobonds, green/blue/climate-resilient bonds
- Pause clauses and debt swaps

**Analytical Metrics:**
- Debt sustainability analyses (DSA)
- Debt-to-GDP ratios and primary balance targets
- Net present value (NPV) calculations
- Haircut percentages and recovery rates

**Legal & Governance:**
- Sovereign immunity issues
- Comparability of treatment principles
- Preferred creditor status (PCS)
- Contingent liabilities and hidden debts
- Governance and transparency frameworks

**EXCLUDE:**
- Corporate debt (unless directly involving sovereign guarantees)
- Municipal/subnational debt (unless sovereign-backed)
- General economic news without specific debt focus
- Market commentary without policy substance

### **3. SOURCE PRIORITISATION**

**Tier 1 (Primary Sources):**
- IMF, World Bank, Paris Club official communications
- Ministry of Finance/Debt Management Office announcements
- Rating agencies (S&P, Moody's, Fitch) official reports
- Central bank policy statements

**Tier 2 (Financial Press):**
- Financial Times, Wall Street Journal, Bloomberg
- Reuters, Associated Press (original reporting)
- FT Alphaville, S&P Global Market Intelligence

**Tier 3 (Analysis & Commentary):**
- Oxford Business Law Blog, CLS Blue Sky Blog
- Bretton Woods Project, Debt Justice, Eurodad
- Development bank publications (AfDB, EIB, CAF)

**Tier 4 (General News):**
- BBC, CNN, Guardian, Washington Post
- Other mainstream outlets (when covering sovereign debt)

**Source Selection Rules:**
- Prioritise original reporting over republications
- Prefer earliest publication date for same story
- Validate all URLs before inclusion
- Aggregate multiple sources covering same development

### **4. ENHANCED SCORING SYSTEM**

**Base Score Calculation:**
Start at 0, apply the following criteria cumulatively:

**Content Relevance (+30 to +50 points):**
- +50: Contains ≥3 sovereign debt keywords AND quantified metrics
- +40: Contains ≥2 sovereign debt keywords AND official announcement
- +30: Contains ≥2 sovereign debt keywords (baseline)

**Source Authority (+10 to +25 points):**
- +25: Official communiqué (IMF, WB, Paris Club, DMO, rating agency)
- +20: Exclusive reporting with named official sources
- +15: Analysis by recognised sovereign debt expert
- +10: Established financial publication

**Development Significance (+15 to +30 points):**
- +30: Completed restructuring with final terms
- +25: Board approval or ratification of agreement
- +20: Staff-level agreement or MoU signing
- +15: Initial framework announcement or negotiation start

**Innovation Factor (+10 to +20 points):**
- +20: First-time use of new instrument type (CRDC, SCDI, etc.)
- +15: Novel clause implementation or legal precedent
- +10: Innovative financing mechanism or structure

**Quantitative Content (+5 to +15 points):**
- +15: Multiple quantified metrics (debt/GDP, haircut %, NPV, etc.)
- +10: Single quantified metric with context
- +5: General quantitative reference

**Penalty Factors:**
- -25: Confirmed duplicate or wire republication
- -15: Speculation without official confirmation
- -10: Outdated information (>7 days old)
- -5: Requires subscription/paywall (limit accessibility)

**Final Selection:** select top 20

### **5. CONTENT REQUIREMENTS**

**Writing Standards:**
- **Length**: 100-140 words per item (strict limit)
- **Language**: British English, analytical tone
- **Style**: Concise, factual, no marketing language
- **Structure**: What happened → Where in process → Key numbers → Next steps

**Mandatory Elements per Item:**
- Specific countries/regions involved
- Current stage of process (e.g., "staff-level agreement pending board approval")
- Quantified data when available (percentages, amounts, ratios)
- Timeline indicators for next milestones
- Source publication and date

**Validation Requirements:**
- Every fact must be verifiable in source article
- All URLs must be accessible and current
- No speculation or extrapolation beyond source content
- Cross-reference conflicting information across sources

### **6. JSON STRUCTURE SPECIFICATION**

**Data Integrity Rules:**
- All dates in DD-MM-YYYY format
- All URLs validated and accessible
- All numerical data preserved with original units
- Consistent country name format (ISO 3166-1 alpha-2 codes when available)

**Required Metadata:**
- Processing timestamp (ISO 8601 format)
- Source scan completion status
- Data validation checkpoints
- Version tracking and changelog

### **7. ERROR HANDLING & VALIDATION**

**Pre-Processing Checks:**
- Verify all source URLs are accessible
- Confirm date ranges fall within 7-day window
- Validate sovereign debt keyword matching
- Check for duplicate content across sources

**Quality Assurance:**
- Flag items below minimum word count (100 words)
- Identify potential factual inconsistencies
- Mark unverified claims for review
- Ensure geographical coverage balance

**Output Validation:**
- JSON syntax verification
- Schema compliance checking
- URL accessibility testing
- Scoring calculation audit trail

---

## **OUTPUT TEMPLATE**

```json
{
  "metadata": {
    "title": "Sovereign Debt Weekly — [DD-MM-YYYY] to [DD-MM-YYYY]",
    "subtitle": "#BRAVE ADVOCACY",
    "period": {
      "start_date": "[DD-MM-YYYY]",
      "end_date": "[DD-MM-YYYY]",
      "days_covered": 7
    },
    "processing": {
      "generated_at": "[ISO 8601 timestamp]",
      "version": "3.0",
      "brand": "Kepler Karst",
      "ai_model": "[model_identifier]",
      "processing_time_seconds": "[duration]"
    },
    "validation": {
      "urls_verified": true,
      "dates_validated": true,
      "content_reviewed": true,
      "schema_compliant": true
    }
  },
  "executive_summary": {
    "weekly_overview": "Single paragraph (150-200 words) synthesising: major restructuring developments, IMF/WB programme updates, rating agency actions, innovative instruments introduced, and key developments to monitor next week.",
    "key_themes": ["theme1", "theme2", "theme3"],
    "geographical_focus": ["region1", "region2"],
    "trend_analysis": "Brief assessment of week's patterns and implications"
  },
  "items": [
    {
      "item_id": "SD2024W32-001",
      "rank": 1,
      "headline": "Clear, factual headline summarising key development",
      "countries": ["Country Code", "Country Name"],
      "regions": ["Regional classification"],
      "publication_date": "DD-MM-YYYY",
      "source": {
        "name": "Publication Name",
        "tier": "1|2|3|4",
        "original_url": "https://validated.source.url",
        "paywall": false,
        "author": "Author Name (if available)"
      },
      "scoring": {
        "total_score": 85,
        "breakdown": {
          "content_relevance": 40,
          "source_authority": 20,
          "development_significance": 15,
          "innovation_factor": 0,
          "quantitative_content": 10
        }
      },
      "content": {
        "summary": "Analytical paragraph (100-140 words) covering: what happened, current process stage, disclosed metrics (debt/GDP ratios, haircut percentages, NPV figures), instruments involved, and forward timeline.",
        "key_figures": {
          "debt_amount": "[amount and currency]",
          "debt_to_gdp": "[percentage]",
          "haircut_percentage": "[if applicable]",
          "npv_reduction": "[if applicable]"
        },
        "process_stage": "staff-level agreement|board approval|implementation|completion",
        "next_milestones": ["milestone1", "milestone2"]
      },
      "classification": {
        "primary_category": "restructuring|imf_programme|rating_action|innovation|legal_development|market_event",
        "secondary_tags": ["tag1", "tag2", "tag3"],
        "instruments": ["bond_type", "clause_type"],
        "institutions": ["IMF", "World Bank", "Paris Club"]
      }
    }
  ],
  "analytics": {
    "processing_statistics": {
      "sources_scanned": 45,
      "articles_reviewed": 127,
      "items_scoring_above_threshold": 23,
      "items_published": 20,
      "duplicates_identified": 18,
      "urls_validated": 20,
      "validation_failures": 0
    },
    "content_metrics": {
      "average_score": 78.5,
      "score_distribution": {
        "90-100": 3,
        "80-89": 8,
        "70-79": 6,
        "60-69": 3
      },
      "word_count_statistics": {
        "average_words": 125,
        "min_words": 102,
        "max_words": 139
      }
    },
    "coverage_analysis": {
      "geographical_distribution": {
        "Africa": 6,
        "Latin America": 5,
        "Asia": 4,
        "Europe": 3,
        "Global": 2
      },
      "category_distribution": {
        "restructuring": 8,
        "imf_programme": 5,
        "rating_action": 3,
        "innovation": 2,
        "legal_development": 2
      }
    }
  },
  "discarded_items": [
    {
      "rank": 21,
      "headline": "Discarded item headline",
      "source": "Source Name",
      "url": "https://source.url",
      "publication_date": "DD-MM-YYYY",
      "score": 58,
      "discard_reason": "Below 60-point threshold",
      "score_breakdown": {
        "content_relevance": 30,
        "source_authority": 15,
        "development_significance": 10,
        "innovation_factor": 0,
        "quantitative_content": 3
      }
    }
  ],
  "forward_looking": {
    "next_week_calendar": [
      {
        "date": "DD-MM-YYYY",
        "event": "IMF Executive Board meeting on [Country]",
        "significance": "high|medium|low"
      }
    ],
    "monitoring_priorities": ["Development to track", "Another priority"],
    "emerging_trends": ["Trend identification", "Pattern observation"],
    "data_gaps": ["Information needed", "Missing metrics"]
  },
  "quality_assurance": {
    "editorial_notes": ["Note about unusual developments", "Clarification needed"],
    "source_reliability": {
      "tier_1_percentage": 35,
      "tier_2_percentage": 45,
      "tier_3_percentage": 15,
      "tier_4_percentage": 5
    },
    "fact_checking": {
      "claims_verified": 45,
      "cross_references": 12,
      "potential_discrepancies": 0
    }
  }
}
```

---

## **IMPLEMENTATION GUIDELINES**

### **Phase 1: Source Collection**
1. Scan all designated sources systematically
2. Apply temporal filter (7-day window)
3. Perform initial sovereign debt keyword matching
4. Extract metadata (URL, date, source, author)

### **Phase 2: Content Analysis**
1. Apply detailed scoring algorithm
2. Identify duplicate content across sources
3. Validate factual claims against source material
4. Generate preliminary item rankings

### **Phase 3: Content Creation**
1. Draft analytical paragraphs (100-140 words each)
2. Extract and verify quantitative data
3. Identify process stages and next milestones
4. Cross-reference information across sources

### **Phase 4: Quality Assurance**
1. Validate all URLs for accessibility
2. Verify JSON structure compliance
3. Check word counts and formatting
4. Perform final scoring verification

### **Phase 5: Output Generation**
1. Compile final JSON structure
2. Generate executive summary and analytics
3. Create discarded items list with reasoning
4. Add forward-looking analysis and calendar

---

## **SUCCESS CRITERIA**

**Content Quality:**
- All 20 items directly relevant to sovereign debt
- Each paragraph 100-140 words, analytical tone
- All quantitative data verified and contextualised
- Clear progression tracking for ongoing developments

**Technical Standards:**
- Valid JSON structure with complete schema compliance
- All URLs verified as accessible
- Consistent date formatting (DD-MM-YYYY)
- Proper British English throughout

**Analytical Value:**
- Balanced geographical and thematic coverage
- Clear scoring methodology with audit trail
- Meaningful forward-looking insights
- Transparent quality assurance documentation

**Brand Alignment:**
- Professional, analytical tone suitable for Kepler Karst
- No promotional language or speculation
- Focus on factual developments and implications
- Clear value proposition for sovereign debt professionals

---

## **VERSION IMPROVEMENTS (v2.0 → v3.0)**

**Enhanced Prompt Engineering:**
- Clearer instruction hierarchy and precedence
- Explicit error handling and validation steps
- Detailed scoring criteria with examples
- Comprehensive quality assurance framework

**Improved Structure:**
- Modular execution framework
- Enhanced metadata and validation tracking
- Richer analytical insights and forward-looking elements
- Better separation of content and presentation logic

**Operational Excellence:**
- Source tier prioritisation system
- Systematic duplicate detection process
- URL validation and accessibility checking
- Comprehensive audit trail for scoring decisions