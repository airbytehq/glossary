---
title: "What is Schema Evolution"
tags:
- data engineering
---
Automatic Schema Evolution is a crucial feature in [Data Lake Table Format](term/Data%20Lake%20Table%20Format.md)s as changing formats is still a pain in today's data engineer work. Schema Evolution means adding new columns without breaking anything or even enlarging some types. You can even rename or reorder columns, although that might break backward compatibilities. Still, we can change one table, and the table format takes care of switching it on all distributed files. Best of all does not require e rewrite of your table and underlying files.

See also [ACID Transactions](term/ACID%20Transactions.md).