---
title: "Raw Tables"
tags:
- airbyte
---
Airbyte spits out tables with the prefix `_airbyte_raw_`. This is your replicated data, but the prefix indicates that it's not normalized. If you select basic [normalization](term/normalization.md), Airbyte will create renamed versions without the prefix.