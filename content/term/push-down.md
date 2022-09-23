---
title: "What is a Push-Down?"
tags:
- data engineering
aliases:
- Query Pushdown
---
Query pushdown aims to execute as much work as possible in the source databases. 

Push-downs or query pushdowns push transformation logic to the source database. This reduces to store data physically and transfers them over the network. 

For example, a [semantic layer](term/semantic%20layer.md) or [data virtualization](term/data%20virtualization.md) translates the transformation logic into [SQL](term/sql.md) queries and sends the SQL queries to the database. The source database runs the SQL queries to process the transformations.

Pushdown optimization increases mapping performance when the source database can process transformation logic faster than the semantic layer itself. 
