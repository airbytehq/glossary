---
title: "What is ETL?"
tags:
- data engineering
---
ETL (extract transform and load) is loading data in a three-phase process and is a classic paradigm that emerged in the 1970s. Recently, it has shifted to [ELT](term/elt.md). The ELT philosophy dictates that data should be untouched – apart from minor cleaning and filtering – as it moves through the extraction and loading stages so that the raw data is always accessible in the [Data Warehouse](term/data%20warehouse.md).

## ETL is Changing
The way we do ETL is changing. For a long time it was done with ETL tools such as Informatica, IBM Datastage, Cognos, AbInitio, or Microsoft SSIS, today we use more programmatic or configuration-driven platforms like [[Airflow]], [[Dagster]], and [Temporal](term/temporal.md). And with data needs growing, and the need for having data faster, the trend shifted to ELT.

See also [ETL vs ELT](term/etl%20vs%20elt.md).