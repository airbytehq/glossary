---
title: "What is data transformation?"
tags:
- data engineering
---

Data transformation is the process of converting data from one format into a different format. Reasons for doing this could be to optimize the data for a different use case than it was originally intended for, or to meet the requirements for storing data in a different system. Data transformation may involve steps such as cleansing, normalizing, [structuring](term/structured%20data.md), validation, sorting, joining, or [enriching](term/data%20enrichment.md) data. 

## How is data transformation done
Data is often transformed as part of an [ETL (Extract, Transform, Load)](term/etl.md) or [ELT (Extract, Load, Transform)](term/elt.md) approach to [data integration](https://airbyte.com/blog/data-integration). 

See [ETL vs. ELT](term/etl%20vs%20elt.md) for a comparison of these two approaches.  

Additionally, a hybrid approach has recently emerged which is known as [EtLT (Extract, “tweak”, Load, Transform)](term/etlt.md). This combines aspects of both ETL and ELT. 

## Benefits of data transformation
When used correctly, data transformation can provide the following benefits:

- Improved query-time efficiency and speed. 
- Conversion of data into a format that is required by a target system.
- Enrichment of data with additional information that allows insights to be more easily extracted.
- Improved data quality by validating and fixing data, and removal of duplicates. 

## Examples of data transformation
Below are some examples of how data may be transformed to achieve some of the benefits mentioned above.

### Improved efficiency and speed
One kind of transformation could be the extraction of structured data from data that is stored in a string. Imagine data that looks as follows: 

```
input_string: "Bob is 29"
```

In order to efficiently process this data in the future, it may preferable to transform this data into additional/new fields, and store it as:

```
name: "Bob"
age: 29
```

Storing the data in this manner makes it much more efficient to analyze with operations such as:

```sql
SELECT * FROM X where Age=29
```

### Enriching data
[Data enrichment](data%20enrichment.md) is a data transformation that adds additional information to the data that makes new kinds of queries possible.  
