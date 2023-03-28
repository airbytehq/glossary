---
title: "What is Normalization?"
tags:
- data engineering
---

Normalization is used in relational database design to reduce data redundancy and improve data integrity. Developed by British computer scientist [Edgar F. Codd ](https://en.wikipedia.org/wiki/Edgar_F._Codd) in the 1970s as part of his relational model, normalization involves organizing the columns (attributes) and tables (relations) in a database to ensure proper enforcement of dependencies through database integrity constraints. 

This is achieved by applying formal rules during the synthesis (creation of a new database design) or decomposition (improvement of an existing database design) process.

1.  **First Normal Form (1NF)**:
    - Eliminate duplicate data by ensuring each attribute contains only atomic values and each table has a unique primary key.
2.  **Second Normal Form (2NF)**:
    - Meet all requirements of 1NF and remove partial dependencies by ensuring that every non-prime attribute (attribute not part of any candidate key) entirely depends on the primary key.
3.  **Third Normal Form (3NF)**:
    - Meet all requirements of 2NF and remove transitive dependencies by ensuring that no non-prime attribute is transitively dependent on the primary key.

## Denormalization
**Denormalization**, on the other hand, is the process of intentionally introducing redundancy into a database design by combining tables or adding redundant data, aiming to improve query performance or simplify the database structure. Denormalization is the **opposite of normalization**. Please consider the trade-offs between data integrity and query performance. This technique is used with [Dimensional Modeling](term/dimensional%20modeling.md) in [OLAP](term/olap%20(online%20analytical%20processing).md) cubes, for example.

