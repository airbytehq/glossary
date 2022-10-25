---
title: "What is data transformation?"
tags:
- data engineering
---

## Definition
Data transformation is the process of converting data from one format into a different format. Reasons for doing this could be to optimize the data for a different use case than it was originally intended for, or to meet the requirements for storing data in a different system. Data transformation may involve steps such as cleansing, normalizing, structuring, validation, sorting, joining, or enriching data. 

## How is data transformation done
Data is often transformed using an [ETL (Extract, Transform, Load)](https://glossary.airbyte.com/term/etl/) or [ELT (Extract, Load, Transform)](https://glossary.airbyte.com/term/elt/) approach. See [ETL vs. ELT](https://glossary.airbyte.com/term/etl-vs-elt) for a comparison of these two approaches.  

Additionally, a hybrid approach has recently emerged which is known as [EtLT (Extract, “tweak”, Load, Transform)](https://glossary.airbyte.com/term/etlt). This combines aspects of both ETL and ELT. 

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

SELECT * FROM X where Age=29

### Enriching data
Data transformation can be used to add additional information to the data that makes new kinds of queries possible. Imagine that you have a “System A” that contains an IP address to country mapping, and a “System B” that contains a data set with records that include an IP address (but no country). If you would like to execute queries on “System B” by country, it would be beneficial to transform records in “System B” to include a country field. This can be achieved by running a transformation job that reads the IP address from each record on “System B”, performs a lookup on “System A” to get the associated country name, and that writes the country name back into an “enriched” data set on “System B”. Future queries which break down the data by country can then be efficiently executed against this enriched data set on “System B”. 
