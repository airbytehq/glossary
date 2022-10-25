---
title: "What is ELT?"
tags:
- data engineering
---
ELT (Extract, Load, and [Transform](term/data%20transformation.md)) is a [data integration](https://airbyte.com/blog/data-integration) approach that extracts (E) data from a source system, and loads (L) raw data into a destination system before it transforms (T) the data. In other words, in the ELT approach, transformation (T) of the data is done _within_ the destination [Data Warehouse](term/data%20warehouse.md) after data has been loaded. 

ELT is in contrast to the more traditional [ETL](term/etl.md) data integration approach, in which data is transformed before it arrives at the destination. See [ETL vs ELT](term/etl%20vs%20elt.md) for a more detailed comparision of these approaches.

The shift from the ETL paradigm to the ELT paradigm has been made possible thanks to the plummeting cost of cloud-based computation and storage, and the appearance of cloud-based data warehouses like Redshift, BigQuery, or Snowflake. 

The following image demonstrates the ELT approach to data integration -- in this diagram [dbt](https://docs.getdbt.com/docs/introduction) creates and manages the SQL that is used for transforming the data in the destination:

![](images/elt-tool.png)

ELT is also related to [Reverse ETL](term/reverse%20etl.md) which you can find more information about at: [Reverse ETL Explained](https://airbyte.com/blog/reverse-etl#so-what-is-a-reverse-etl) or [Airbyte.com](https://airbyte.com). 
