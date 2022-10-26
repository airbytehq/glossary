---
title: "What is structured data?"
tags:
- data engineering
- concepts
---

Structured data refers to data that has been formatted into a well-defined schema. One example would be data that is stored with precisely defined columns in a relational database or excel spreadsheet. Examples of structured fields are age, name, phone number, credit card numbers or address. Storing data in a structured format allows it to be easily understood and queried with tools such as  SQL.

Structured data can be contrasted with unstructured data, which does not conform to a data model and has no easily identifiable structure. Unstructured data cannot be easily used by programs, and is difficult to analyze. Examples of unstructured data could be the contents of an email, a word document, data from social media, photos, videos, survey results, etc.   

Structured data can also be contrasted with semi-structured data, which lacks a rigid structure and does not conform directly to a data model. However, it has tags and elements that describe how the data is stored. Examples of semi-structured are JSON or XML files. Semi-structured data often contains enough information that it can be relatively easily converted into structured data. 

## Example of unstructured data

An simple example of unstructured data is a string that contains interesting information inside of it, but that has not been formatted into a well defined schema. An example is given below:

|               |  **UnstructuredString**|
|---------| -----------|
|Record 1| "Bob is 29" |
|Record 2| "Mary just turned 30"|


## An example of adding structure to unstructured data

Converting unstructured data into structured data can be done during the data transformation stage in an ETL or ELT process.  For example, in order to efficiently process the unstructured data given in the previous example, it may desirable to transform this data into additional/new fields, and store it as structured data such as the following:

|               |  **name** | **age** |
|---------| -----------|---- |
|Record 1| "Bob" | 29 |
|Record 2| "Mary"| 30 |

Storing the data in a structured manner makes it much more efficient to query the data. For example, after structuring the data it is possible to easily and efficiently execute the following query on the structured data:

  
``` SQL
SELECT * FROM X where Age=29
```

A query such as this would be expensive and/or more difficult to execute on unstructured data.

## An example of semi-structured data

A string containing a JSON representation such as the following is an example of semi-structured data. It has all the information required to structure, but is still contained in a string. The Raw JSON stored by Airbyte during ELT is an example of semi-structured data. This looks as follows:  

|               |  **\_airbyte_data**|
|---------| -----------|
|Record 1| **{"id": 1, "name": "Mary X"}** |
|Record 2|**{"id": 2, "name": "John D"}**|

## Adding structure to semi-structured data

It is often relatively straightforward to convert semi-structured data may into structure data. For example, if normalization is enabled then Airbyte will convert the JSON from the previous example into a table that looks as follows:  

|               |  **id** | **name** |
|---------| -----------|---- |
|Record 1| 1 | "Mary X" |
|Record 2|2| "John D" |
  
## A real-world example of converting semi-structured to structured data
If the semi-structured JSON data were stored in Postgres, then it could be converted  into structured data by making use of [JSON Functions and Operators]([https://www.postgresql.org/docs/9.4/functions-json.html](https://www.postgresql.org/docs/9.4/functions-json.html)). A real-world implementation of this is discussed the tutorial: [Explore Airbyte's full refresh data synchronization](https://airbyte.com/tutorials/full-data-synchronization)
