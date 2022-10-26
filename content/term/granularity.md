---
title: "What is Granularity"
tags:
- data engineering
---
Declaring the granularity (or _grain_) is the pivotal step in [Dimensional Modeling](term/dimensional%20modeling.md). The grain establishes exactly what a single fact table row represents. The grain declaration becomes a binding contract on the design. The grain must be declared before choosing [[dimensions]] or [[facts]] because every candidate dimension or fact must be consistent with the grain. This consistency enforces uniformity on all dimensional designs which is critical to [Business Intelligence](term/business%20intelligence.md) application performance and ease of use.

For example, in the **transformation layer**, you must balance low and high granularity. What level do you aggregate and store (e.g., [rollups](term/rollup.md) hourly data to daily to save storage), or what valuable dimensions to add. With each dimension and its column added, rows will [explode](https://www.ibm.com/docs/en/ida/9.1.1?topic=phase-step-identify-measures#c_dm_design_cycle_4__c_dm_4_step7) exponentially, and we can’t persist each of these representations to the filesystem.

A [Semantic Layer](term/semantic%20layer.md) is much more flexible and makes the most sense on top of [transformed data](term/data%20transformation.md) in a [Data Warehouse](term/data%20warehouse.md). Avoid extensive reshuffles or reprocesses of large amounts of data. Think of [OLAP](term/olap%20(online%20analytical%20processing).md) cubes where you can dice-and-slice ad-hoc on significant amounts of data without storing them ahead of time

Read more on [Kimball Dimensional Modeling Techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/). Also related is [Rollup](term/rollup.md).

