---
title: "ETL and ELT with Airbyte"
tags:
- airbyte
---
[ELT](term/elt.md) and [ETL](term/etl.md) specific to Airbyte mean:
- **Extract**: Retrieve data from a [source](https://docs.airbyte.com/integrations/#Sources), which can be an application, database, or anything really.
- **Load**: Move data to your [destination](https://docs.airbyte.com/integrations/#Destinations).
- **Transform**: Clean up the data. This is referred to as [normalization](term/normalization.md) in Airbyte and involves [incremental synchronization](term/incremental%20synchronization.md) and [deduplication](https://docs.airbyte.com/understanding-airbyte/connections/incremental-deduped-history), changing data types, formats, and more.