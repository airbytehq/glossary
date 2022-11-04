---
title: "What is a sync run?"
tags:
- airbyte
---
Airbyte replication can be thought of as a loop which periodically requests records from a data source and sends them to a destination. Each iteration of this loop is referred to as a sync run, which is discussed in more detail in [How we scale workflow orchestration with Temporal](https://airbyte.com/blog/scale-workflow-orchestration-with-temporal#triggering-a-sync-run).