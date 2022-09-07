---
title: "What is ETL?"
tags:
- data engineering
---
ETL (extract transform and load) is loading data in a three-phase process and is a classic paradigm that emerged in the 1970s. Recently, it has shifted to [ELT](term/elt.md). The ELT philosophy dictates that data should be untouched – apart from minor cleaning and filtering – as it moves through the extraction and loading stages so that the raw data is always accessible in the [Data Warehouse](term/data%20warehouse.md).

## ETL is Changing
The way we do ETL is changing. For a long time it was done with ETL tools such as Informatica, IBM Datastage, Cognos, AbInitio, or Microsoft SSIS, today we use more programmatic or configuration-driven platforms like [[Airflow]], [[Dagster]], and [[Temporal]]. And with data needs grow, and the need for having data faster, the trend shifted to ELT.

## ETL vs ELT
ETL (Extract Transform and Load) and ELT (Extract Load and Transform). ETL was originally used for [Data Warehousing](term/data%20warehouse.md) and ELT for creating a [Data Lake](term/data%20lake.md). The key difference is that the data schema and the transformation need to be done before the data lands at the destination.

More on [Airbyte.com](https://airbyte.com) or [Reverse ETL Explained](https://airbyte.com/blog/reverse-etl#so-what-is-a-reverse-etl).