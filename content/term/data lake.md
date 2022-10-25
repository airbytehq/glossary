---
title: "What is a Data Lake?"
tags:
- data engineering
---
A Data Lake is a storage system with vast amounts of unstructured and structured data, stored as-is, without a specific purpose in mind, that can be built on multiple technologies such as Hadoop, NoSQL, Amazon Simple Storage Service, a relational database, or various combinations and different formats (e.g. Excel, CSV, Text, Logs, etc.).

According to [Hortonworks Data Lake Whitepaper](http://hortonworks.com/wp-content/uploads/2014/05/TeradataHortonworks_Datalake_White-Paper_20140410.pdf), the data lake arose because new types of data needed to be captured and exploited by the enterprise. As this data became increasingly available, early adopters discovered that they could extract insight through new applications built to serve the business. The data lake supports the following capabilities:
-   To capture and store raw data at scale for a low cost
-   To store many types of data in the same repository
-   To perform [data transformation](term/data%20transformation.md) on the data where the purpose may not be defined
-   To perform new types of data processing
-   To perform single-subject analytics based on particular use cases

The initial concept was created by Databricks in the [CIDR Paper](http://cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) in 2021. Read more on our [Data Lake and Lakehouse Guide](https://airbyte.com/blog/data-lake-lakehouse-guide-powered-by-table-formats-delta-lake-iceberg-hudi).