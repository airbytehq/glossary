---
title: "What is DuckDB?"
tags:
- data engineering
---

[DuckDB](https://duckdb.org/) is an in-process SQL [OLAP](term/olap%20(online%20analytical%20processing).md) database management system. It has strong support for SQL. DuckDB is borrowing the SQLite shell implementation. Each database is a single file on disk. It's [SQLite DB](https://www.sqlite.org) for **analytical (OLAP) workloads**, whereas SQLite is for a relational database. But it can handle vast amounts of data locally. It's the minor sister of [Apache Druid](Apache%20Druid) and other OLAP technologies.

It's designed to work as an embedded library, eliminating the network latency you usually get when talking to a database.
> [!note] Don't use plain files any longer
>
> Never use files (CSV, Excel, Parquet) anymore. Use DuckDB with schema, types, and SQL interface, and super fast. 

Use-Cases:
- Ulta fast analytical use-case locally. E.g., the Taxi example includes a 10 Year, 1.5 Billion row Taxi data example that still works on a laptop. See benchmarks below. 
- It can be used as an SQL wrapper with zero copies (on top of parquets in S3). 
- Bring your **data to the users** instead of having big roundtrips and latency by doing REST calls. Instead, you can put data inside the client. You can do 60 frames per second as data is where the query is. 

[MotherDB](https://motherduck.com/) is the managed service around DuckDB that lets you scale from a local DB to a cloud DB and hybrid—done by one of [Google BigQuery](Google%20BigQuery) creators or developers such as [[Jordan Tigani]]. Check his discussion on the [Analytics Engineering Podcast about The Personal Data Warehouse](https://open.spotify.com/episode/3CmeFOuIOg91xApdjbWqey?si=CmelGaxBTZ-Z-BR3fvMjmg&utm_source=copy-link&nd=1). The stimulating conversation around connected WebAssembly, e.g., Is an application compiled to C code, which is super fast. E.g., Figma is using that, which would otherwise never work in a browser. 

## Benchmarks
- [Fast Analysis With DuckDB + Pyarrow](https://tech.gerardbentley.com/python/data/intermediate/2022/04/26/holy-duck.html) - 2022
- [Tweet](https://mobile.twitter.com/medriscoll/status/1554698141789614081): Impressively fast, collaborative exploratory data analytics over a 20+ million row data set, hosted in the cloud with Drifting’s Jamsocket + Rill Data + DuckDB - 2022
- [Taking DuckDB for a spin | Uwe’s Blog](https://uwekorn.com/2019/10/19/taking-duckdb-for-a-spin.html) - 2019

## Technical 
It ships as an [amalgamation](https://www.sqlite.org/amalgamation.html) build - a single giant C++ file (SQLite is a single giant C file). And it's also backed up by some strong computer science. It's by the academic researchers behind MonetDB and includes implementations of a bunch of interesting papers:
-   [Data Management for Data Science - Towards Embedded Analytics](https://www.duckdb.org/pdf/CIDR2020-raasveldt-muehleisen-duckdb.pdf) (CIDR 2020)
-   [DuckDB: an Embeddable Analytical Database](https://www.duckdb.org/pdf/SIGMOD2019-demo-duckdb.pdf) (SIGMOD 2019 Demo)

From [Why DuckDB](https://duckdb.org/why_duckdb):
> DuckDB contains a **columnar-vectorized query execution engine**, where queries are still interpreted, but a large batch of values (a “vector”) is processed in one operation. This greatly reduces overhead present in traditional systems such as PostgreSQL, MySQL or SQLite which process each row sequentially. Vectorized query execution leads to far better performance in OLAP queries.


## Python API and Handling Data
From [DuckDB Docs - Python API](https://duckdb.org/docs/api/python)
### Fetching Data with SQL
```python
# fetch as pandas data frame
df = con.execute("SELECT * FROM items").fetchdf()
print(df)
#        item   value  count
# 0     jeans    20.0      1
# 1    hammer    42.2      2
# 2    laptop  2000.0      1
# 3  chainsaw   500.0     10
# 4    iphone   300.0      2

# fetch as dictionary of numpy arrays
arr = con.execute("SELECT * FROM items").fetchnumpy()
print(arr)
# {'item': masked_array(data=['jeans', 'hammer', 'laptop', 'chainsaw', 'iphone'],
#              mask=[False, False, False, False, False],
#        fill_value='?',
#             dtype=object), 'value': masked_array(data=[20.0, 42.2, 2000.0, 500.0, 300.0],
#              mask=[False, False, False, False, False],
#        fill_value=1e+20), 'count': masked_array(data=[1, 2, 1, 10, 2],
#              mask=[False, False, False, False, False],
#        fill_value=999999,
#             dtype=int32)}
```
### Create Table
```python
# create a table
con.execute("CREATE TABLE items(item VARCHAR, value DECIMAL(10,2), count INTEGER)")
# insert two items into the table
con.execute("INSERT INTO items VALUES ('jeans', 20.0, 1), ('hammer', 42.2, 2)")

# retrieve the items again
con.execute("SELECT * FROM items")
print(con.fetchall())
# [('jeans', 20.0, 1), ('hammer', 42.2, 2)]
```
### Insert Data
```python
# insert a row using prepared statements
con.execute("INSERT INTO items VALUES (?, ?, ?)", ['laptop', 2000, 1])

# insert several rows using prepared statements
con.executemany("INSERT INTO items VALUES (?, ?, ?)", [['chainsaw', 500, 10], ['iphone', 300, 2]] )

# query the database using a prepared statement
con.execute("SELECT item FROM items WHERE value > ?", [400])
print(con.fetchall())
# [('laptop',), ('chainsaw',)]
```
