---
title: "What is a Data Warehouse?"
tags:
- data engineering
---
A Data Warehouse, in short DWH, also known as an Enterprise Data Warehouse (EDW), is the traditional way of collecting data as we do [since 30+ years](https://tdwi.org/articles/2016/02/01/data-warehousing-30.aspx). The DWH serves to be the data integration from many different sources, the single point of truth and the data management, meaning cleaning, historizing, and data joined together. It provides greater executive insight into corporate performance with management Dashboards, Reports, or Ad-Hoc Analyses.

Various types of business data are analyzed with Data Warehouses. The need for it often becomes evident when analytic requirements run afoul of the ongoing performance of operational databases. Running a complex query on a database requires the database to enter a temporarily fixed state. It is often untenable for transactional databases. A data warehouse is employed to do the analytical work, leaving the transactional database free to focus on transactions.

The other characteristic is analyzing data from multiple origins (e.g., your Google Analytics with your CRM data). It is highly [transformed](term/data%20transformation.md) and structured due to the [ETL (Extract Transform Load)](term/etl.md) process.

If you wonder about the difference between a Data Warehouse, Data Lake, and a Lakehouse, read more on our [Data Lake and Lakehouse Guide](https://airbyte.com/blog/data-lake-lakehouse-guide-powered-by-table-formats-delta-lake-iceberg-hudi).