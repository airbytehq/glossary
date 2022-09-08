---
title: "What is a Data Lake File Format?"
tags:
- data engineering
---
Data lake file formats are the new CSVs on the cloud. They are more column-oriented and compress large files with added features. The main players here are [Apache Parquet](term/apache%20parquet.md), [Apache Avro](term/apache%20avro.md), and [Apache Arrow](term/apache%20arrow.md). It’s the physical store with the actual files distributed around different buckets on your [Object Store](term/storage%20layer%20object%20store.md).

You can build more features with [Data Lake Table Format](term/data%20lake%20table%20format.md) on top. Read more on our [Data Lake and Lakehouse Guide](https://airbyte.com/blog/data-lake-lakehouse-guide-powered-by-table-formats-delta-lake-iceberg-hudi).