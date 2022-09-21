---
title: "What is a Cursor?"
tags:
- airbyte
---
At a conceptual level, a cursor is a tracker that is used during [incremental synchronization](term/incremental%20synchronization.md) to ensure that only newly updated or inserted records are sent from a data source to a destination in any given synchronization iteration.

Airbyte’s incremental synchronization can be conceptually thought of as a loop which periodically executes synchronization operations. Each iteration of this loop only replicates records that have been inserted or updated in the source system since the previous execution of this synchronization loop – in other words, each synchronization operation will copy only records that have not previously been replicated by previous synchronizations. This is much more efficient than copying an entire dataset on each iteration, which is the behavior of full refresh synchronization.

Sending only updated or newly inserted documents requires tracking which records have already been replicated in previous synchronizations. This is done by a cursor, which can be thought of as a pointer to the most recent record that has been replicated by a given synchronization. When selecting documents for synchronization, Airbyte includes the most recent cursor value as part of the query on the source system to ensure that only new/updated records will be replicated.

For example, a source database could contain records which include a field called `updated_at`, which stores the most recent time that a record is inserted or updated. If `updated_at` is selected as the cursor field, then after a given synchronization operation the cursor will remember the largest `updated_at` value that has been seen in the records that have been replicated to the destination in that synchronization. In the subsequent synchronization operation, records that have been inserted or updated on the source are retrieved by including the cursor value as part of the query, so that it only selects records where the `updated_at` value is greater than (and in some edge cases greater than or equal to) the largest `updated_at` value seen in the previous synchronization.

Note that while it is not strictly necessary to choose a time field for a cursor field, the field that is chosen should be monotonically increasing over time.

Read more on [Incremental data synchronization between Postgres databases](https://airbyte.com/tutorials/incremental-data-synchronization). 