---
title: "What is a Metrics Layer?"
tags:
- data engineering
aliases:
- Metrics Store
---
> [!info] Similarities to a Semantic Layer
> 
> The metrics layer is one component of a [Semantic Layer](term/semantic%20layer.md). A limited metrics layer is usually built into a [BI tool](term/business%20intelligence%20tools.md), translating its [metrics](term/metric.md) to only that BI tool. 

A metrics layer, sometimes also called a metrics store, includes a specification of metrics such as [measures](term/metric.md) and [dimensions](term/dimensions.md). Additionally, it can contain model parsing from files (mostly [YAML](term/yaml.md)) and APIs to create and execute metric logic; some include a cache layer. A metrics layer encourages us to enforce the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Do not repeat yourself) principle by defining metrics once before populating them to any BI tools used or integrating them into internal applications or processes.

Read more on [Semantic Layer](term/semantic%20layer.md) or [The Rise of the Semantic Layer](https://airbyte.com/blog/the-rise-of-the-semantic-layer-metrics-on-the-fly).
