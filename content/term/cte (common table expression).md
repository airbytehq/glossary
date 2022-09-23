---
title: "What is a CTE (Common Table Expression)?"
tags:
- data engineering
---

A Common Table Expression (CTE) is a temporary named result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement. The CTE can also be used in a View.

```sql
WITH cte_query AS
(SELECT … subquery ...)
SELECT main query ... FROM/JOIN with cte_query ...
```

## Types: Recursive and Non-Recursive
### Non-Recursive CTE
There are two types of CTEs: Recursive and Non-Recursive.

The non-recursive are simple where CTE is used to avoid SQL duplication by referencing a name instead of the actual SQL statement.

E.g.
```sql
WITH avg_per_store AS
  (SELECT store, AVG(amount) AS average_order
   FROM orders
   GROUP BY store)
SELECT o.id, o.store, o.amount, avg.average_order AS avg_for_store
FROM orders o
JOIN avg_per_store avg
ON o.store = avg.store;
```

### Recursive CTE

Recursive CTEs use repeated procedural loops therefore the recursion. The recursive query calls itself until the query satisfied the condition. In a recursive CTE, we should provide a where condition to terminate the recursion.

A recursive CTE is useful in querying hierarchical data such as organization charts where one employee reports to a manager or multi-level bill of materials when a product consists of many components, and each component itself also consists of many other components.

```sql
WITH levels AS (
  SELECT
    id,
    first_name,
    last_name,
    superior_id,
    1 AS level
  FROM employees
  WHERE superior_id IS NULL
  UNION ALL
  SELECT
    employees.id,
    employees.first_name,
    employees.last_name,
    employees.superior_id,
    levels.level + 1
  FROM employees, levels
  WHERE employees.superior_id = levels.id
)
 
SELECT *
FROM levels;
```

See more on[5 Practical SQL CTE Examples | LearnSQL.com](https://learnsql.com/blog/practical-sql-cte-examples/).