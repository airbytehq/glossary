
---
title: "What is unstructured data?"
tags:
- data engineering
- concepts
---

Unstructured data is data that does not conform to a data model and has no easily identifiable structure. Unstructured data cannot be easily used by programs, and is difficult to analyze. Examples of unstructured data could be the contents of an email, contents of a word document, data from social media, photos, videos, survey results, etc.

## An example of unstructured data

An simple example of unstructured data is a string that contains interesting information inside of it, but that has not been formatted into a well defined schema. An example is given below:

|               |  **UnstructuredString**|
|---------| -----------|
|Record 1| "Bob is 29" |
|Record 2| "Mary just turned 30"|

## Unstructured vs structured data

In contrast with unstructured data, [structured data](term/structured%20data.md) refers to data that has been formatted into a well-defined schema. An example would be data that is stored with precisely defined columns in a relational database or excel spreadsheet. Examples of structured fields could be age, name, phone number, credit card numbers or address. Storing data in a structured format allows it to be easily understood and queried by machines and with tools such as  SQL.

## Structuring of unstructured data

Extracting structured data from unstructured data is often done during the [data transformation](term/data%20transformation.md) stage in an [ETL](term/etl.md) or [ELT](term/elt.md) process.  

For example, in order to efficiently make use of the unstructured data given in the previous example, it may desirable to transform it into structured data such as the following:

|               |  **name** | **age** |
|---------| -----------|---- |
|Record 1| "Bob" | 29 |
|Record 2| "Mary"| 30 |

Storing the data in a structured manner makes it much more efficient to query the data. For example, after structuring the example data it is possible to easily and efficientl execute queries by name or by age. 


  