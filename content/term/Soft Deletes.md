---
title: "What is Soft Deletes"
tags:
- data engineering
---
In order to propagate records that have been deleted when using [Incremental Synchronization](term/Incremental%20Synchronization.md) modes, records in a database may include a field that indicates that a record should be treated as if it has been removed. This is necessary because incremental synchronization does not replicate documents that are fully deleted from a source system.  
  
For example, a boolean flag such as "is_deleted" could be used to indicate that a record should be treated as if it has been deleted. All queries would need to be written so as to exclude records/documents where "is_deleted" is set, and periodically executed background jobs can be used to remove all documents where "is_deleted" is set.

‍