---
title: "What is ELT?"
tags:
- data engineering
---
An ELT (extract load and transform) pipeline is used to move raw data from a source to a destination. If data enrichment and transformation are required, these operations occur inside the destination [Data Warehouse](term/data%20warehouse.md). This is in contrast to more traditional [ETL](term/etl.md) tools, which transform the data before it arrives at the destination. The shift from ETL tools to ELT tools has been made possible thanks to the plummeting cost of cloud-based computation and storage, and the appearance of cloud-based data warehouses like Redshift, BigQuery, or Snowflake.

The following image demonstrates the ELT approach to data integration:

![](images/elt-tool.png)

ELT is also related to [Reverse ETL](term/reverse%20etl.md) which you can find more information about at: [Reverse ETL Explained](https://airbyte.com/blog/reverse-etl#so-what-is-a-reverse-etl) or [Airbyte.com](https://airbyte.com). 