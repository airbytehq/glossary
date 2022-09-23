---
title: "What is Data Virtualization?"
tags:
- data engineering
---
Data Virtualization helps you when you have many source systems from different technologies, but all of them are rather fast in response time, and if you don't run a lot of operational applications. In that way, you don't move and copy data around and pre-aggregate, but you have a [Semantic Layer](term/metrics%20layer.md) where you create your business models (like cubes), and only if you query this data virtualization layer does it query the data source. If you use, e.g. [Dremio](https://www.dremio.com/), there you use [Apache Arrow](term/apache%20arrow.md) technology which will cache and optimize a lot in-memory for you that you have as well as stonishing fast response times.

It's tightly connected to [Data Federation](term/data%20federation.md) and [Push-Downs](term/push-down.md).