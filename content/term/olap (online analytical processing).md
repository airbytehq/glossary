---
title: "What is OLAP (Online Analytical Processing)?"
tags:
- data engineering
---

OLAP is an acronym for **Online Analytical Processing**. OLAP performs multidimensional analysis of business data and provides the capability for complex calculations, trend analysis, and sophisticated [data modeling](term/data%20modeling.md). An **OLAP cube** is a multidimensional database that is optimized for [data warehouse](term/data%20warehouse.md) and online analytical processing (OLAP) applications. 

An OLAP cube is a method of storing data in a multidimensional form, generally for reporting purposes. In OLAP cubes, data ([Measures](term/metric.md)) are categorized by [dimensions](term/dimensions.md). 

In order to manage and perform processes with an OLAP cube, Microsoft developed a query language, known as [multidimensional expressions (MDX)](https://learn.microsoft.com/en-us/analysis-services/multidimensional-models/mdx/), in the late 1990s.  Many other vendors of multidimensional databases have adopted MDX for querying data, but with this specific language, management of the cube requires personnel with the skill set.

The opposite of OLAP is [OLTP](term/oltp%20(online%20transactional%20processing).md). Read more on [Wikipedia](https://en.wikipedia.org/wiki/Online_analytical_processing).