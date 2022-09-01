---
title: "What is a Data Lake File Format"
tags:
- data engineering
---
Data lake file formats are the new CSVs on the cloud. They are more column-oriented and compress large files with added features. The main players here are [[Apache Parquet]], [[Apache Avro]], and [[Apache Arrow]]. It’s the physical store with the actual files distributed around different buckets on your [Object Store](term/Storage%20Layer.md).

You can build more features with [Data Lake Table Format](term/Data%20Lake%20Table%20Format.md) on top. Read more on our [Data Lake and Lakehouse Guide](https://airbyte.com/blog/data-lake-lakehouse-guide-powered-by-table-formats-delta-lake-iceberg-hudi).