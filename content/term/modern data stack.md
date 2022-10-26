---
title: "What is the Modern Data Stack?"
tags:
- data engineering
---
The Modern Data Stack (MDS) is a heap of open-source tools to achieve end-to-end analytics from ingestion to [transformation](term/data%20transformation.md) to ML over to a columnar data warehouse or lake solution with an analytics BI dashboard backend. This stack is extendable like lego blocks. Usually, it consists of **data integration, a transformation tool, an [Orchestrator](term/data%20orchestrator.md), and a [Business Intelligence Tool](term/business%20intelligence%20tools.md)**. With growing data, you might add [Data Quality](term/data%20quality.md) and observability tools, [Data Catalog](term/data%20catalog.md), [Semantic Layer](term/semantic%20layer.md), and more.

In a way, it is [unbundling](https://blog.fal.ai/the-unbundling-of-airflow-2/) the data stack as Gorkem says:
> Products start small, in time, add adjacent verticals and functionality to their offerings, and become a platform. Once these **platforms** become big enough, people begin to figure out how to serve better-neglected verticals or abstract out functionality to break it down into purpose-built chunks, and the unbundling starts.

The goal of an MDS is to get data insight with the best suitable tools for each part. It's noteworthy that it's a relatively new term.

> [!note] New Terms popping up
>
> There is already a new term [ngods (new generation open-source data stack)](https://blog.devgenius.io/modern-data-stack-demo-5d75dcdfba50). Or *DataStack 2.0* in Dagster's recent [blog post](https://dagster.io/blog/evolution-iq-case-study).

## The Future of MDS
If we look a little in the future, Barr Moses illustrates in her article [What's In Store For The Future Of The Modern Data Stack?](https://www.montecarlodata.com/blog-the-future-of-the-modern-data-stack/) more features such as data sharing, universal [Data Governance](term/data%20governance.md), [Data Lake](term/data%20lake.md), and [Data Warehouse](term/data%20warehouse.md) equalized, and a newer evolution of predictive analysis:
![](images/future-modern-data-stack.png)