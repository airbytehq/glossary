---
title: "What is ELT?"
tags:
- data engineering
---
Compared to [ETL](term/etl.md), in an ELT (extract load and transform) pipeline, data enrichment and transformation occur inside the [Data Warehouse](term/data%20warehouse.md), not in a processing server like in the case of ETL pipelines. The shift has been primarily made possible thanks to the appearance of cloud-based data warehouses like Redshift, BigQuery, or Snowflake.

It is also tightly connected with [Reverse ETL](term/reverse%20etl.md). And you can read more on [Reverse ETL Explained](https://airbyte.com/blog/reverse-etl#so-what-is-a-reverse-etl) or [Airbyte.com](https://airbyte.com).