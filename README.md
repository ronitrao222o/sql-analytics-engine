# SQL Analytics Engine

## Overview
This project implements a SQL-driven analytics engine that processes transactional
sales data and generates business insights using advanced SQL queries.

## Data Model
- Single fact table optimized for analytical queries
- Derived metrics computed directly in SQL
- Query performance optimized using indexes on frequently queried columns


## Analytics Supported
- Top customers by revenue
- Revenue by product and category
- Monthly revenue trends
- Running revenue totals using window functions
- Category-wise revenue analysis using SQL aggregations
- Repeat customer analysis to identify returning buyers


## How to Run
```bash
python src/main.py
