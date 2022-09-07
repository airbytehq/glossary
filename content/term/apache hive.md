---
title: "What is Apache Hive?"
tags:
- data engineering
---
Apache Hive is a [Data Warehouse](term/data%20warehouse.md) software project built on top of [Apache Hadoop](term/apache%20hadoop.md) for providing data queries and analysis. Hive gives an SQL-like interface to query data stored in various databases and file systems that integrate with Hadoop. Traditional SQL queries must be implemented in the [MapReduce](term/map%20reduce.md) Java API to execute SQL applications and queries over distributed data. Hive provides the necessary SQL abstraction to integrate SQL-like queries ([HiveQL](https://en.wikipedia.org/wiki/Apache_Hive#HiveQL)) into the underlying Java without the need to implement queries in the low-level Java API.