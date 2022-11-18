---
title: "What is a Data Lake Transaction Log?"
tags:
- data engineering
---
The transaction log is the ordered record of every transaction, with a configurable duration that can optionally be set to retain all transactions (i.e. data infinite). A transaction log is a common component used through many of its above-mentioned features, including [ACID Transactions](term/acid%20transactions.md), scalable metadata handling, and [Time Travel](term/time%20travel.md). For example, [Delta Lake](term/delta%20lake.md) creates a single [folder called `_delta_log`](https://airbyte.com/tutorials/load-data-into-delta-lake-on-databricks-lakehouse#step-5).