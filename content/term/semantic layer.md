---
title: "What is a Semantic Layer"
tags:
- data engineering
aliases:
- Headless BI
---

> A semantic layer (sometimes also called Headless BI) calculates complex business [metrics](term/metric.md) at *query time*. It sits between your data sources/transformation layer and your analytics tools. You define a metric's aggregations (daily, weekly, monthly, and quarterly) and dimensions (region, customer, product). Examples of metrics could be "monthly active users", "weekly revenue", "number of paying customers", and so on.

You can think of a semantic layer as a translation layer between any data presentation layer ([business intelligence](term/business%20intelligence.md), [notebooks](term/notebooks.md), data apps) and the data sources. A translation layer includes many features, such as integrating data sources, modeling the metrics, and integrating with the data consumers by translating metrics into [SQL](term/sql.md), REST, or GraphQL.

Because everyone has different definitions of “active” users or “paying” customers, the semantic layer allows you to define these discrepancies once company-wide. Instead of having three different versions each presentation tool e.g. BI tool would show a different number than your Jupyter notebook or data app. And what if the metric changes to a new definition, with a semantic layer you change only one time. This powerful feature empowers domain experts and data practitioners to get a common understanding of business metrics.

A sub-layer of the semantic layer is the [Metrics Layer](term/metrics%20layer.md). 

Read more on [The Rise of the Semantic Layer](https://airbyte.com/blog/the-rise-of-the-semantic-layer-metrics-on-the-fly) or other fascinating reads on the topic:
-   [Down the Semantic Rabbit Hole](https://jpmonteiro.substack.com/p/down-the-semantic-rabbit-hole)
-   [The Missing Piece of the Modern Data Stack](https://benn.substack.com/p/metrics-layer) 
-   [Deep Dive: What The Heck Is the Metrics Layer](https://pedram.substack.com/p/what-is-the-metrics-layer)
-   [The Great Data Debate by Atlan](https://atlan.com/great-data-debate/)
-   [The Metrics Layer has Growing up to do](https://prakasha.substack.com/p/the-metrics-layer-has-growing-up)
-   [The Universal Semantic Layer, More Important Than Ever](https://www.atscale.com/blog/what-is-a-universal-semantic-layer-why-would-you-want-one/)
-   [Demystifying the Metrics Store and Semantic Layer](https://thenewstack.io/demystifying-the-metrics-store-and-semantic-layer/)