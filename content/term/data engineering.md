---
title: "What is Data Engineering?"
tags:
- data engineering
---
The definition from the [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/), as it’s one of the most recent and complete: 
> Data engineering is the development, implementation, and maintenance of systems and processes that take in raw data and produce high-quality, consistent information that supports downstream use cases, such as analysis and machine learning. Data engineering intersects security, data management, DataOps, data architecture, orchestration, and software engineering.

A data engineer today oversees the whole data engineering process, from collecting data from various sources to making it available for downstream processes. The role requires familiarity with the multiple stages of the [Data Engineering Lifecycle](term/data%20engineering%20lifecycle.md) and an aptitude for evaluating data tools for optimal performance across several dimensions, including price, speed, flexibility, scalability, simplicity, reusability, and interoperability.

Data Engineering helps also overcome the bottlenecks of [Business Intelligence](term/business%20intelligence.md):
- More transparency as tools are open-source mostly
- More frequent data loads
- Supporting [Machine Learning](term/machine%20learning.md) capabilities 

Compared to existing roles it would be a **software engineering plus business intelligence engineer including big data abilities** as the [Hadoop](term/apache%20hadoop.md) ecosystem, streaming, and computation at scale. Business creates more reporting artifacts themselves but with more data that needs to be collected, cleaned, and updated near real-time and complexity is expanding every day.

With that said more programmatic skills are needed similar to software engineering. **The emerging language at the moment is [Python](term/python.md)** which is used in engineering with tools alike [[Apache Airflow]], [Dagster](Dagster), [[Prefect]] as well as data science with powerful libraries.

As a data engineer, you use mainly [SQL](term/sql.md) for almost everything except when using external data from an API. Here you'd use [ELT](term/elt.md) tools or write some [[data pipelines]] with the tools mentioned above.

Want to know more about [The Evolution of The Data Engineer: A Look at The Past, Present & Future](https://airbyte.com/blog/data-engineering-past-present-and-future), check out the linked article or watch the video form of it:
{{< youtube Si14Hgj4Lok >}}
