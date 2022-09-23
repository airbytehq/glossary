---
title: "What is Full Refresh Synchronization?"
tags:
- airbyte
---
A Full Refresh Sync will attempt to retrieve all data from the source every time a sync is run. Then there are two choices, *Overwrite* and *Append*. Overwrite deletes the data in the destination before running the sync and Append doesn't.

