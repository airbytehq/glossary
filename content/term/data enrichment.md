---
title: "What is data enrichment"
tags:
- data engineering
---

Data enrichment is a kind of [data transformation](term/data%20transformation.md) which adds additional information to the data in order to makes new kinds of queries possible and/or more efficient.

## Example of data enrichment
Imagine that you have a “System A” that contains an IP address to country mapping, and a “System B” that contains a data set with records that include an IP address (but no country). If you would like to execute queries on “System B” by country, it would be beneficial to transform records in “System B” to include a country field. This can be achieved by running a transformation job that reads the IP address from each record on “System B”, performs a lookup on “System A” to get the associated country name, and that writes the country name back into an “enriched” data set on “System B”. Future queries which break down the data by country can then be efficiently executed against this enriched data set on “System B”.