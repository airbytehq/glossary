---
title: "What are Data Processing Techniques (row-based, columnar, vectorized)?"
tags:
- data engineering
---

A collection of concepts and technologies that encompass various methods and optimizations for storing, retrieving, and processing data in database systems. This glossary page includes definitions for **columnar storage, row-based storage, and vectorized engines**, which are all techniques that aim to improve the efficiency and performance of different types of workloads, such as transactional, analytical, and large-scale data processing tasks. 

By understanding these techniques, database users and developers can make informed decisions about which approach best fits their specific use cases and requirements.

## Columnar Storage
A database storage technique that stores data by columns rather than rows, allowing for more efficient compression and faster querying for analytical workloads. Columnar storage is particularly useful for read-heavy operations and large-scale data analytics, as it enables the retrieval of specific columns without the need to access the entire row. This contrasts with traditional row-based storage, where data is stored row by row, making it more suited for transactional workloads and operations that involve frequent updates and inserts.

## Row-based Storage
A traditional database storage technique where data is stored in consecutive rows, allows for efficient processing of operations that involve entire records, such as inserts, updates, and deletions. Row-based storage is well-suited for transactional systems (OLTP) that require fast access to individual records. However, it can be less efficient for analytical workloads and large-scale data processing, where columnar storage offers better performance due to its ability to selectively retrieve specific columns without accessing the entire row.

## Vectorized Engine
A modern database query execution engine designed to optimize data processing by leveraging vectorized operations and SIMD (Single Instruction, Multiple Data) capabilities of modern CPUs. Vectorized engines, such as Databricks' Photon Engine or [DuckDB](term/duckdb.md), process data in large blocks or batches, allowing for improved parallelism, cache locality, and reduced overhead compared to traditional row-at-a-time processing engines. This results in significantly faster query performance, particularly for [analytical](term/analytics.md) and large-scale data processing workloads, making vectorized engines a popular choice in the era of big data and real-time analytics.