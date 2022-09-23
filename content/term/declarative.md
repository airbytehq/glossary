---
title: "What is declarative?"
tags:
- data engineering
---
A **[declarative](term/declarative.md)** data pipeline does not tell the order it needs to be executed but instead allows each step/task to find the best time and way to run. The declarative approach describes *what* the program does without explicitly specifying its control flow. [Functional Data Engineering](term/functional%20data%20engineering.md) and [Functional Programming](term/functional%20programming.md) is a **declarative** programming paradigm, in contrast to **[imperative](term/imperative.md)** programming paradigms.

## Declarative vs Imperative
Declarative approaches appeal because they make systems easier to debug and automate. It's done by explicitly showing intention and offering a simple way to manage and apply changes. By explicitly declaring how the pipeline should look, for example, **defining the data products that should exist**, it becomes much easier to discover when it does not look like that, the reason why, and reconcile. It's the foundation layer for your entire platform's lineage, observability, and [data quality](https://airbyte.com/blog/data-quality-issues) monitoring.

![](images/declarative-vs-imperative.png)

Read more on [Data Orchestration Trends: The Shift From Data Pipelines to Data Products](https://airbyte.com/blog/data-orchestration-trends).