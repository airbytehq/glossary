---
title: "ETL vs. ELT"
tags:
- data engineering
---
[ETL](term/etl.md) (Extract, Transform, and Load) and [ELT](term/elt.md) (Extract, Load, and Transform) are two paradigms for moving data from one system to another. The main difference between them is that when an ETL approach is used, data is transformed before it is loaded into a destination system. On the other hand, in the case of ELT, any required transformations are done after the data has been written to the destination and are _then_ done _inside_ the destination -- often by executing SQL commands. The difference between these approaches is easier to understand by a visual comparison of the two approaches. 

The image below demonstrates the ETL approach to [data integration](https://airbyte.com/blog/data-integration):

![](images/etl-tool.png)

While the following image demonstrates the ELT approach to data integration:

![](images/elt-tool.png)

ETL was originally used for [Data Warehousing](term/data%20warehouse.md) and ELT for creating a [Data Lake](term/data%20lake.md). 

## Disadvantages of ETL compared to ELT

**ETL** has several **disadvantages compared to ELT**, including the following:

- Generally, only transformed data is stored in the destination system, and so analysts must know beforehand every way they are going to use the data, and every report they are going to produce.  
- Modifications to requirements can be costly, and often require re-ingesting data from source systems.
- Every transformation that is performed on the data may obscure some of the underlying information, and analysts only see what was kept during the transformation phase. 
- Building an ETL-based data pipeline is often beyond the technical capabilities of analysts.

Find more on [An overview of Airbyte’s replication modes](https://airbyte.com/blog/understanding-data-replication-modes).

## ELT/ETL Tool Comparision
Need to find the best data integration tool for your business? Which platform integrates with hour data sources and destinations? Which one provides the features you’re looking for?  
  
We made it simple for you. Here’s a [spreadsheet](https://docs.google.com/spreadsheets/d/1QKrtBpg6PliPMpcndpmkZpDVIz_o6_Y-LWTTvQ6CfHA/edit?usp=sharing) with a comparison of all those actors. Or an extensive detailed comparison between the tools on [Top ETL tools compared in details](https://airbyte.com/etl-tools-comparison).

See also more on [Airbyte.com](https://airbyte.com) or [Reverse ETL Explained](https://airbyte.com/blog/reverse-etl#so-what-is-a-reverse-etl).
