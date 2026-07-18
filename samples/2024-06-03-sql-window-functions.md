---
layout: post
title: "SQL Window Functions Finally Make Sense"
date: 2024-06-03 13:00:00 -0400
categories: [sql, databases, backend]
---

Window functions were the SQL feature I avoided for years because the syntax looked intimidating. Then I actually learned them and realised I'd been writing unnecessarily convoluted subqueries for a decade.

Here's the core idea: a window function performs a calculation **across a set of rows related to the current row**, without collapsing those rows into a single result the way `GROUP BY` does.

The basic syntax:

```sql
function_name() OVER (
  PARTITION BY column
  ORDER BY column
  ROWS/RANGE frame_clause
)
```

## Useful Examples

**Running total:**
```sql
SELECT
  order_date,
  amount,
  SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

**Rank customers by spend within each region:**
```sql
SELECT
  customer_id,
  region,
  total_spend,
  RANK() OVER (PARTITION BY region ORDER BY total_spend DESC) AS rank_in_region
FROM customers;
```

**Previous row's value (lag):**
```sql
SELECT
  order_date,
  revenue,
  LAG(revenue, 1) OVER (ORDER BY order_date) AS prev_day_revenue
FROM daily_sales;
```

The functions I reach for most: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `SUM`, `AVG`. They work in PostgreSQL, MySQL 8+, SQLite 3.25+, and SQL Server.
