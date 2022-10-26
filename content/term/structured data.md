---
title: "What is structured data?"
tags:
- data engineering
- concept
---

Structured data refers to data that has been formatted into a well-defined schema. An example would be data that is stored with precisely defined columns in a relational database or excel spreadsheet. Examples of structured fields could be age, name, phone number, credit card numbers or address. Storing data in a structured format allows it to be easily understood and queried by machines and with tools such as SQL.

## Example of structure data

Below is an example of structured data as it would appear in a database:

|         |  **age**| **name**| **phone**| 
|---------|-----|------|-----|
|Record 1| 29 | Bob | 123-456 |
|Record 2| 30 | Sue | 789-123 | 

It may seem that all data is structured, but this is not always the case -- data can be unstructured, or semi-structured. The differences are best understood by example, and are discussed in the following sections. 

## Structured data vs. unstructured data

Structured data can be contrasted with [unstructured data](term/unstructured%20data.md), which does not conform to a data model and has no easily identifiable structure. Unstructured data cannot be easily used by programs, and is difficult to analyze. Examples of unstructured data could be the contents of an email, contents of a word document, data from social media, photos, videos, survey results, etc.   

An simple example of unstructured data is a string that contains interesting information inside of it, but that has not been formatted into a well defined schema. An example is given below:

|               |  **UnstructuredString**|
|---------| -----------|
|Record 1| "Bob is 29" |
|Record 2| "Mary just turned 30"|

## Structuring of unstructured data

Converting unstructured data into structured data can be done during the [data transformation](term/data%20transformation.md) stage in an [ETL](term/etl.md) or [ELT](term/elt.md) process.  

For example, in order to efficiently make use of the unstructured data given in the previous example, it may desirable to transform it into structured data such as the following:

|               |  **name** | **age** |
|---------| -----------|---- |
|Record 1| "Bob" | 29 |
|Record 2| "Mary"| 30 |

Storing the data in a structured manner makes it much more efficient to query the data. For example, after structuring the data it is possible to easily and efficiently execute the following query on the structured data:
  
``` SQL
SELECT * FROM X where Age=29
```

A query such as this would be expensive and/or more difficult to execute on unstructured data.

## Structured data vs. semi-structured data

Structured data can also be contrasted with [semi-structured data](term/semi-structured%20data.md), which lacks a rigid structure and does not conform directly to a data model. However, semi-structured data has tags and elements that describe the data. 

Examples of semi-structured data are JSON or XML files. Semi-structured data often contains enough information that it can be relatively easily converted into structured data. 

JSON data embedded inside of a string, is an example of semi-structured data. The string contains all the information required to understand the structure of the data, but is still for the moment just a string -- it hasn't been structured yet. The Raw JSON stored by Airbyte during ELT is an example of semi-structured data. This looks as follows:  

|               |  **\_airbyte_data**|
|---------| -----------|
|Record 1| \"{'id': 1, 'name': 'Mary X'}\" |
|Record 2| \"{'id': 2, 'name': 'John D'}\"|

## Structuring of semi-structured data

It is often relatively straightforward to convert semi-structured data into structured data. For example, if normalization is enabled then Airbyte will automatically convert the JSON stored in the `_airbyte_data` field in the table above, into a table that looks as follows:  

|               |  **id** | **name** |
|---------| -----------|---- |
|Record 1| 1 | "Mary X" |
|Record 2|2| "John D" |
  
## A real-world example of converting semi-structured to structured data

If the semi-structured JSON data were stored in Postgres, then it could be converted  into structured data by making use of [JSON Functions and Operators]([https://www.postgresql.org/docs/9.4/functions-json.html](https://www.postgresql.org/docs/9.4/functions-json.html)). A real-world implementation of this is discussed the tutorial: [Explore Airbyte's full refresh data synchronization](https://airbyte.com/tutorials/full-data-synchronization)
