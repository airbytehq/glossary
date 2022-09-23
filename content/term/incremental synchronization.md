---
title: "What is Incremental Synchronization?"
tags:
- airbyte
---
Incremental synchronization is a process which efficiently copies data to a destination system by periodically executing queries on a source system for records that have been updated or inserted since the previous sync operation. Only those records that have been recently inserted or updated will be sent to the destination, which is much more efficient than copying an entire data set on each sync operation. Incremental synchronization makes use of a cursor field such as `updated_at` (or whatever you wish to call the field) to determine which records should be propagated, and only records with an `updated_at` value that is newer than the `updated_at` value of the most recent record sent in the previous sync should be replicated.

However, without special consideration, records that have been deleted in the source system will not be propagated to the destination as they will never appear in the results from such a query. This may be addressed by [Soft Deletes](term/soft%20delete.md) or by making use of [CDC replication](https://airbyte.com/blog/change-data-capture-definition-methods-and-benefits).

Read more on [Incremental data synchronization between Postgres databases](https://airbyte.com/tutorials/incremental-data-synchronization) or see related [Full Refresh Synchronization](term/full%20refresh%20synchronization.md).