---
title: "What is imperative?"
tags:
- data engineering
---

An **imperative** pipeline tells _how_ to proceed at each step in a procedural manner. In contrast, a **[declarative](term/declarative.md)** data pipeline does not tell the order it needs to be executed but instead allows each step/task to find the best time and way to run. 

The *how* should be taken care of by the tool, framework, or platform running on. For example, update an asset when upstream data has changed. Both approaches result in the same output. However, the declarative approach benefits from **leveraging compile-time query planners** and **considering runtime statistics** to choose the best way to compute and find patterns to reduce the amount of transformed data.

Read more on [Data Orchestration Trends: The Shift From Data Pipelines to Data Products](https://airbyte.com/blog/data-orchestration-trends).
