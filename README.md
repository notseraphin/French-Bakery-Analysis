# French-Bakery-Analysis
**ABC Revenue & Market Basket Analysis of Bakery Transactions**

***Overview***

This project analyzes bakery sales transaction data to identify high-value products, optimize inventory control, and uncover product bundling opportunities based on purchasing behavior.

The objectives are to transform raw transactional logs into actionable insights that describe:

- Revenue contributions of individual products and tiers (A/B/C)
- Revenue patterns by day of week and time of day
- Product co-occurrence and association for bundling strategies
- Identification of cannibalizing or substitutable items

The pipeline combines Python data processing, ABC revenue analysis, and Market Basket Analysis (MBA) with visualizations to produce reproducible and interpretable outputs.

***Data Source***

Bakery transactional dataset containing:

- 234,005 entries across ~136,000 transactions
- Variables:
  - date / time of order
  - ticket_number (transaction ID)
  - article (product name)
  - quantity
  - unit_price

Derived datasets and outputs:

- Revenue per SKU and ABC tiers
- Revenue by day and time segments
- Co-occurrence matrices and product pairings
- Visualizations saved in figures/

***Model / Analysis Description***
**ABC Revenue Analysis**

- Revenue computed per product: quantity × unit_price
- Cumulative revenue percentages used to classify SKUs into:
  - A-tier: Top ~20% of SKUs contributing ~75% of revenue
  - B-tier: Moderate contribution SKUs
  - C-tier: Low contribution SKUs

- Summary metrics include product tier, revenue, and cumulative contribution
- Tiered control and replenishment strategies informed by ABC classification

**Market Basket & Co-Occurrence Analysis**

- Transactions transformed into item sets to compute:
  - Co-occurrence counts and probabilities of products appearing together
  - High-confidence product pairings for A/B-tier items
  - Differential patterns across time-of-day and day-of-week

- Cannibalization analysis identifies substitutable products where sales may overlap, highlighting potential efficiency improvements

***Visualization Outputs***

Figures automatically saved to figures/ include:

- ABC Pareto chart and tiered product contributions
- Revenue contribution by day of week and time of day
- Market Basket Analysis network graphs and co-occurrence heatmaps
- Bundle recommendations and cannibalization insights

Project Structure
```bash
French-Bakery-Analysis/
│── data/
│   └── bakery_sales.csv
│
│── figures/
│   ├── abc_pareto.png
│   ├── abc_revenue.png
│   ├── abc_tiered_products.png
│   ├── bundle_network_graph.png
│   ├── co_occurrence_heatmap.png
│   ├── market_basket_network.png
│   ├── revenue_by_day.png
│   ├── revenue_by_time.png
│   └── sales_heatmap.png
│
│── notebooks/
│   └── analysis.ipynb
│
│── src/
│   ├── abc_analysis.py
│   ├── market_basket.py
│   └── preprocessing.py
│
│── .gitignore
│── README.md
```

***Results Interpretation***

- A-tier SKUs drive ~75% of total revenue despite being a small fraction of SKUs
- Revenue patterns vary across day-of-week and time-of-day, enabling more efficient staffing and stocking decisions
- Bundling opportunities identified through co-occurrence of A/B-tier products can improve cross-sell efficiency
  <img width="607" height="241" alt="image" src="https://github.com/user-attachments/assets/2f07759d-52c7-4fa2-a06c-34e1b84b5f32" />

- Cannibalization insights reveal substitutable C-tier items that may be candidates for reduction to simplify production
  <img width="558" height="232" alt="image" src="https://github.com/user-attachments/assets/71b6cf32-9221-447e-8845-70882e2cb653" />


***Technologies Used***

- Python
- pandas, numpy
- matplotlib, seaborn, networkx
- Jupyter Notebook
