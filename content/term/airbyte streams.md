---
title: "What are Airbyte Streams?"
tags:
- airbyte
---
In order to understand **AirbyteStreams**, let’s first talk about the **AirbyteCatalog**. An **AirbyteCatalog** describes the structure of data in a data source. It has a single field called streams that contains a list of **AirbyteStreams**. Each **AirbyteStream** contains a _name_ and _json_schema_ field. The _json_schema_ field describes the structure of a stream. This data model is intentionally flexible.

If we are using a data source that is a traditional relational database, each table in that database would map to an **AirbyteStream**. Each column in the table would be a key in the _properties_ field of the _json_schema_ field.

If we are using a data source that wraps an API with multiple different resources (e.g. _api/customers_ and _api/products_) each route would correspond to a stream.