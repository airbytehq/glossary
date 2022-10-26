---
title: "What is semi-structured data?"
tags:
- data engineering
- concept
---

Semi-structured data is data that lacks a rigid structure and that does not conform directly to a data model, but that has tags, metadata, or elements that describe the data. Examples of semi-structured data are JSON or XML files. Semi-structured data often contains enough information that it can be relatively easily converted into structured data. 

JSON data embedded inside of a string, is an example of semi-structured data. The string contains all the information required to understand the structure of the data, but is still for the moment just a string -- it hasn't been structured yet. The Raw JSON stored by Airbyte during ELT is an example of semi-structured data. This looks as follows:  

|               |  **\_airbyte_data**|
|---------| -----------|
|Record 1| \"{'id': 1, 'name': 'Mary X'}\" |
|Record 2| \"{'id': 2, 'name': 'John D'}\"|

## Semi-structured vs structured data
In contrast to semi-structured data,  [structured data](term/structured%20data.md) refers to data that has been formatted into a well-defined schema. An example would be data that is stored with precisely defined columns in a relational database or excel spreadsheet. Examples of structured fields could be age, name, phone number, credit card numbers or address. 

## Structuring of semi-structured data

It is often relatively straightforward to convert semi-structured data into structured data. Converting semi-structured data into structured data is often done during the [data transformation](term/data%20transformation.md) stage in an [ETL](term/etl.md) or [ELT](term/elt.md) process.  

For example, if normalization is enabled then Airbyte will automatically convert the JSON stored in the `_airbyte_data` field in the table above,  into a table that looks as follows:  

|               |  **id** | **name** |
|---------| -----------|---- |
|Record 1| 1 | "Mary X" |
|Record 2|2| "John D" |
  
## A real-world example of converting semi-structured to structured data

If the semi-structured JSON data were stored in Postgres, then it could be converted  into structured data by making use of [JSON Functions and Operators]([https://www.postgresql.org/docs/9.4/functions-json.html](https://www.postgresql.org/docs/9.4/functions-json.html)). A real-world implementation of this is discussed the tutorial: [Explore Airbyte's full refresh data synchronization](https://airbyte.com/tutorials/full-data-synchronization)