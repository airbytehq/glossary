---
title: "What is a Data Lake Transaction Log"
tags:
- data engineering
---
The **data lake transaction log** is the ordered record of every transaction since its inception. A transaction log is a common component used through many of its above-mentioned features, including [ACID Transactions](term/ACID%20Transactions.md), scalable metadata handling, and [Time Travel](term/Time%20Travel.md). For example, [[Delta Lake]] creates a single [folder called `_delta_log`](https://airbyte.com/tutorials/load-data-into-delta-lake-on-databricks-lakehouse#step-5).