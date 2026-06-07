# Data Sources Evaluation – VentureScope AI (v1)

**Prepared for:** VentureScope AI engineering team
**Date:** 2026-06-07

---

## 1. Y Combinator (YC) Startup Directory
**Overview**: The Y Combinator batch database contains information on startups that have graduated from the accelerator, including company name, description, founder details, batch, and launch date.

**Data Available**
- Startup name, tagline, description
- Founders & bios
- Batch (e.g., W22)
- Funding snapshot (when disclosed)
- Website URL, demo links
- Demo Day videos (publicly hosted)

**Access Method**
- **Public API**: No official YC API; data is scraped from the public directory (https://www.ycombinator.com/companies).
- **Scraping**: Required; can be performed with `requests` + `BeautifulSoup` or headless browser for dynamic content.
- **RSS / Dataset**: No RSS; periodic datasets are published by third‑party aggregators (e.g., Crunchbase, Kaggle).

**Rate Limits**: Since scraping is used, we must respect robots.txt and throttle to ≤ 1 request per second. Excessive traffic may trigger IP bans.

**Legal / Terms Considerations**
- YC terms of service prohibit large‑scale automated scraping. Use a modest crawl schedule, cache results, and attribute YC as the source.
- For commercial use, consider licensing data via Crunchbase or a data‑partner agreement.

**Data Quality**
- Generally high for YC‑backed companies (accurate founders, up‑to‑date URLs).
- Coverage limited to YC alumni (~ 5 k entities).

**Fields Collectable**
`name`, `description`, `founders`, `batch`, `website`, `demo_day_video`, `funding_snapshot`.

**Suitability Score**: **8 / 10** – Strong relevance to early‑stage startups; limited breadth.

**Recommended Usage**
- Populate the core **startup** table.
- Use for founder network analysis and batch‑level trend insights.

---

## 2. Product Hunt
**Overview**: Community‑driven platform showcasing newly launched products, many of which are startups.

**Data Available**
- Product name, tagline, description
- Launch date, category, tags
- Up‑vote count, comment count, discussion thread
- Founder / company link, website URL
- Screenshots & media assets

**Access Method**
- **Public API**: Official API (requires API key) providing JSON endpoints for daily posts, product details, and comments.
- **RSS**: Product Hunt offers an RSS feed for daily launches.
- **Scraping**: Possible but discouraged; API preferred.

**Rate Limits**
- 10 requests per minute per API key; bursts up to 30 req/min for short periods.

**Legal / Terms Considerations**
- API terms require attribution and prohibit resale of raw data.
- Must store only data needed for internal analytics; do not expose raw Product Hunt data publicly.

**Data Quality**
- High‑quality, community‑vetted; however, not every product is a true startup (some are side‑projects).

**Fields Collectable**
`product_name`, `tagline`, `description`, `launch_date`, `category`, `upvotes`, `comments`, `founder_name`, `website`, `media_urls`.

**Suitability Score**: **7 / 10** – Valuable for recent product signals; coverage broader than YC but noisier.

**Recommended Usage**
- Enrich startup profiles with product launch signals.
- Feed into growth‑score calculations.

---

## 3. GitHub
**Overview**: The world’s largest code‑hosting platform; provides signals of engineering activity, popularity, and community engagement.

**Data Available**
- Repository metadata (stars, forks, issues, watchers)
- Commit history, contribution stats
- Release tags, release dates
- Language breakdown, license
- Dependency graphs (via GraphQL API)

**Access Method**
- **Public API**: GitHub REST and GraphQL APIs (rate‑limited, requires personal access token).
- **Scraping**: Not needed; APIs provide all needed endpoints.

**Rate Limits**
- Authenticated REST: 5 000 requests/hour per token.
- GraphQL: 5 000 points/hour (each query consumes points based on complexity).

**Legal / Terms Considerations**
- Must comply with GitHub’s Terms of Service and API License.
- Data must be used in accordance with the GitHub API Agreement; redistribution of raw data is prohibited without transformation.

**Data Quality**
- Excellent for technical signals; coverage limited to open‑source projects (≈ 300 M repos). Private repos are inaccessible.

**Fields Collectable**
`repo_name`, `owner`, `stars`, `forks`, `open_issues`, `watchers`, `primary_language`, `last_commit_date`, `release_tags`.

**Suitability Score**: **9 / 10** – Core engineering metric source; essential for growth & funding prediction models.

**Recommended Usage**
- Populate the **github_metrics** table.
- Combine with YC / Product Hunt to assess traction.

---

## 4. Crunchbase
**Overview**: Commercial database of startup companies, funding rounds, investors, and key personnel.

**Data Available**
- Company profile (name, description, website, headquarters)
- Funding history (rounds, amounts, investors)
- Founder & team details
- Acquisitions, exits, IPOs
- Market categories & tags

**Access Method**
- **Public API**: Requires a paid subscription (Free tier provides limited fields & rate limits).
- **Dataset**: Periodic CSV/JSON snapshots available for enterprise customers.
- **RSS**: Not applicable.

**Rate Limits**
- Free tier: 50 requests/day; paid tiers increase to > 10 000 requests/day.

**Legal / Terms Considerations**
- Strict licensing; raw data cannot be redistributed.
- Must display Crunchbase attribution on any public UI.
- Commercial use requires a paid plan.

**Data Quality**
- High‑quality, curated; however, some fields may be stale for early‑stage startups.

**Fields Collectable**
`company_name`, `description`, `website`, `headquarters`, `founded_on`, `funding_total`, `investors`, `status`, `categories`.

**Suitability Score**: **8 / 10** – Comprehensive business data; cost and licensing are the main constraints.

**Recommended Usage**
- Populate **startups**, **funding**, and **founders** tables.
- Use for MVP if a paid plan is approved; otherwise, rely on free tier for limited coverage.

---

## 5. AngelList / Wellfound
**Overview**: Platform for early‑stage startups to raise capital and recruit talent. Provides public company pages.

**Data Available**
- Startup name, tagline, description
- Team members & bios
- Funding status (seed, pre‑seed, etc.)
- Job listings
- Market segment tags

**Access Method**
- **Public API**: Deprecated; no official API as of 2025.
- **Scraping**: Required; can be done responsibly using the public HTML pages.
- **Dataset**: Some community‑maintained CSV dumps exist.

**Rate Limits**
- Since scraping, throttle to ≤ 1 req/sec; respect robots.txt.

**Legal / Terms Considerations**
- AngelList’s Terms of Service prohibit large‑scale automated scraping without prior consent. Obtain permission for commercial use or use publicly available datasets.

**Data Quality**
- Good for early‑stage, pre‑seed startups; coverage overlaps with YC but also includes many non‑YC founders.

**Fields Collectable**
`name`, `tagline`, `description`, `team`, `funding_stage`, `website`, `job_postings`.

**Suitability Score**: **6 / 10** – Useful niche data; legal constraints and lack of API reduce practicality.

**Recommended Usage**
- Optional supplement to YC data for broader early‑stage coverage.

---

## 6. Hacker News (HN)
**Overview**: Community news site where startup announcements, product launches, and fundraising news are frequently posted.

**Data Available**
- Post title, URL, timestamp
- Number of comments, points (popularity)
- Author username
- Discussion thread content

**Access Method**
- **Public API**: Official Firebase API provides JSON feeds for top, new, and best stories (no authentication required).
- **RSS**: No native RSS, but third‑party services generate feeds.

**Rate Limits**
- No explicit limits; best practice ≤ 10 requests per minute.

**Legal / Terms Considerations**
- Content is user‑generated and released under the site’s license; attribution required.
- Must not republish entire comment threads verbatim for commercial products.

**Data Quality**
- High‑signal for early‑stage buzz but noisy; many posts are unrelated or low‑quality.

**Fields Collectable**
`story_id`, `title`, `url`, `points`, `comments_count`, `author`, `timestamp`.

**Suitability Score**: **5 / 10** – Good for “buzz” detection; should be used as a supplementary signal.

**Recommended Usage**
- Feed into a **news sentiment** pipeline for early detection of funding announcements.

---

## 7. TechCrunch
**Overview**: Leading technology news outlet covering startup funding rounds, product launches, and market trends.

**Data Available**
- Article title, author, publication date
- Full article text (HTML)
- Tags / topics (e.g., “Funding”, “Enterprise”)
- Embedded media (images, videos)

**Access Method**
- **RSS**: Provides a feed of newest articles.
- **Scraping**: Required for full‑text extraction (paywall‑free articles only).
- **API**: No public API; third‑party news APIs (e.g., NewsAPI) aggregate TechCrunch content under license.

**Rate Limits**
- RSS feeds: No explicit limits; stay under 1 request per 30 seconds.
- Scraping: Must respect robots.txt; use polite crawling.

**Legal / Terms Considerations**
- Content is copyrighted; use for internal analytics only.
- Redistribution requires a license from TechCrunch or a news aggregation partner.

**Data Quality**
- Very high editorial quality; excellent for confirmed funding events.

**Fields Collectable**
`article_id`, `title`, `author`, `published_at`, `url`, `content`, `tags`.

**Suitability Score**: **7 / 10** – High‑value for verified events; licensing may be a hurdle for public products.

**Recommended Usage**
- Populate a **news_mentions** table for verified funding announcements.

---

## 8. Open Startup Datasets
**Overview**: Publicly released collections such as the Kaggle “Startups” dataset, CB Insights open‑source snapshots, and the OpenCorporates bulk dump.

**Data Available**
- Basic company metadata (name, industry, location)
- Funding amounts (historical, often outdated)
- Founder information (limited)
- URL links to company websites

**Access Method**
- **Dataset**: Direct download of CSV/JSON files (no API).
- **Public API**: Some datasets (e.g., OpenCorporates) provide a REST API for lookup.

**Rate Limits**
- Dataset download: One‑time operation (no limits).
- OpenCorporates API: Free tier 1 000 requests/day.

**Legal / Terms Considerations**
- Licenses vary: most are CC‑0 or CC‑BY‑4.0, requiring attribution.
- Ensure compliance with each dataset’s usage policy.

**Data Quality**
- Variable; some records are stale or incomplete.
- Good for bootstrapping the initial catalog.

**Fields Collectable**
`company_name`, `industry`, `location`, `website`, `founded_year`, `last_funding_amount`.

**Suitability Score**: **6 / 10** – Useful for seeding the database but requires enrichment from other sources.

**Recommended Usage**
- Load as a baseline “catalog” table; enrich later with YC, Crunchbase, and GitHub signals.

---

## Recommended MVP Data Sources (Sprint 1)
| Rank | Source | Reason for Priority |
|------|--------|----------------------|
| 1 | **GitHub** | Highest suitability (9/10), provides objective engineering metrics essential for growth & funding models. Free API with generous limits.
| 2 | **Y Combinator** | Strong early‑stage coverage (8/10) and high data quality; manageable scraping scope.
| 3 | **Product Hunt** | Offers recent product launch signals (7/10) via a clean public API; complements YC data.
| 4 | **Crunchbase (Free tier)** | Provides essential business & funding fields (8/10) despite rate limits; useful for validation of events.
| 5 | **Open Startup Datasets** | Low‑effort bulk import to seed the startup catalog.
| 6 | **TechCrunch (RSS)** | Verified news source for funding events; can be added after core signals are in place.
| 7 | **Hacker News** | Useful buzz indicator but noisy; secondary priority.
| 8 | **AngelList / Wellfound** | Legal constraints and lack of API lower its practicality for MVP.

**Implementation Note**: For Sprint 1, focus on integrating GitHub, YC, and Product Hunt pipelines. Store raw responses in the `collectors/` sub‑packages, normalise into the `startups`, `github_metrics`, and `product_hunt_metrics` tables, and run a nightly ETL job using a simple cron schedule.

---

*Prepared by the VentureScope AI research team.*
