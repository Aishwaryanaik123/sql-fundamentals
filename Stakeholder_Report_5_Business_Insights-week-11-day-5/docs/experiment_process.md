# Experiment Process — Stakeholder Report

## 1. Business objective
Provide stakeholders with five understandable insights from sales performance data and recommend practical next actions.

## 2. Dataset
- Period: January 2024 to December 2025
- Rows: 288
- Dimensions: month, year, region, product category
- Measures: sales, profit, orders, average order value, profit margin
- Coverage: four regions and three product categories
- Data status: synthetic demonstration dataset

## 3. Preparation
1. Generated a consistent monthly dataset with one row per month-region-category combination.
2. Checked row count, missing values, and numeric fields.
3. Calculated annual, regional, category, monthly, and margin summaries.

## 4. Analysis
1. Compared total sales between 2024 and 2025.
2. Ranked regions by sales and calculated each region's share.
3. Ranked product categories by sales contribution.
4. Reviewed monthly sales and fourth-quarter contribution.
5. Compared profit margin across regions.

## 5. Insight communication
Each insight includes a headline, supporting evidence, business meaning, and recommended action. Charts are included to make patterns easier to understand.

## 6. Quality checks
- Dataset contains 288 rows, as expected (24 months × 4 regions × 3 categories).
- Checked that sales and orders are positive.
- Profit margins are calculated from aggregate profit divided by aggregate sales.
- Shares use total sales as the denominator.

## 7. Limitations
The dataset is synthetic and designed for demonstration. It does not represent a real organization, customer base, or market. No causal conclusions can be drawn. Findings should be recalculated using approved company data before operational decisions.

## 8. Deliverables
PDF stakeholder report, PowerPoint presentation, insight register CSV, five chart images, source CSV, SQL queries, and this process document.
