---
title: "What is ETL?"
tags:
- data engineering
---
ETL (Extract, [Transform](term/data%20transformation.md), and Load) is a paradigm for moving data from one system to another. It involves reading data (Extract) from one system, modifying the data (Transform), and then sending it (Load) to a destination system. The ETL paradigm emerged in the 1970s. 

A key feature of ETL is that data is transformed before being sent to the destination, as demonstrated in the following image:

![](images/etl-tool.png)

However in recent years, the preferred data movement paradigm has shifted to [ELT](term/elt.md) (Extract, Load, and Transform). The ELT philosophy dictates that data should be untouched – apart from minor cleaning and filtering – as it moves through the extraction and loading stages so that the raw data is always accessible in the destination [Data Warehouse](term/data%20warehouse.md). See [ETL vs ELT](term/etl%20vs%20elt.md) for a comparison of these approaches.


## ETL is Changing
The way we do ETL is changing. For a long time ETL was done with tools such as Informatica, IBM Datastage, Cognos, AbInitio, or Microsoft SSIS. Today we use more programmatic or configuration-driven platforms like [[Airflow]], [[Dagster]], and [Temporal](term/temporal.md). 

Historically **ETL was once preferred** over ELT for the following **no-longer-valid reasons**: 
- ETL could achieve cost savings by removing unwanted data before sending it to the destination –  however, with the plummeting cost of cloud-based computation and storage the value of this proposition is greatly reduced. 
- Because ETL transforms data before it is stored, it avoids the complexity of transforming data _after_ sending it to the destination – however, new tools such as [[dbt]] (data build tool) make it preferable and easy to transform data in the destination.

