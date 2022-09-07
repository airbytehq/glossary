---
title: "What is a Directed Acyclic Graph (DAG)?"
tags:
- data engineering
---
A DAG is a graph where information must travel along with a finite set of nodes connected by vertices. There is no particular start or node and also no way for data to travel through the graph in a loop that circles back to the starting point.

It's a popular way of building data pipelines in the data engineering community as it clearly defines the [Data Lineage](term/data%20lineage.md). As well, it's made for a functional approach where you have the [idempotency](term/idempotency.md) to restart pipelines without side-effects