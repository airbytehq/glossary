---
title: "What is DuckDB?"
tags:
- data engineering
---

[DuckDB](https://duckdb.org/) is an in-process SQL [OLAP](term/olap%20(online%20analytical%20processing).md) database management system. It has strong support for SQL. DuckDB is borrowing the SQLite shell implementation. Each database is a single file on disk. It's analogous to "[SQLite](https://www.sqlite.org) for **analytical (OLAP) workloads**" (direct comparison on the [SQLite vs DuckDB paper](https://simonwillison.net/2022/Sep/1/sqlite-duckdb-paper/) here), whereas SQLite is for OLTP ones. But it can handle vast amounts of data locally. It's the smaller, lighter version of [Apache Druid](Apache%20Druid) and other OLAP technologies.

It's designed to work as an embedded library, eliminating the network latency you usually get when talking to a database.

> [!note] Skip working with error-prone Excels or CSVs directly
>
> With DuckDB, we no longer need to use plain files (CSV, Excel, Parquet). DuckDB supports schema, types, and SQL interface and is super fast. 

## Use-Cases
- Ultra-fast analytical use-case locally. E.g., the Taxi example includes a 10 Year, 1.5 Billion row Taxi data example that still works on a laptop. See benchmarks below. 
- It can be used as an SQL wrapper with zero copies (on top of parquets in S3). 
- Bring your **data to the users** instead of having big roundtrips and latency by doing REST calls. Instead, you can put data inside the client. You can do 60 frames per second as data is where the query is.
- DuckDB on Kubernetes for a zero-copy layer to read S3 in the [Data Lake](https://glossary.airbyte.com/term/data-lake)! Inspired by [this](https://twitter.com/Ubunta/status/1584907743391272961) Tweet. The cheapest and fastest option to get started.

Check out [Rill Data](https://www.rilldata.com/), a [BI tool](term/business%20intelligence%20tools.md) that delivers sub-second interactivity because it’s backed by DuckDB (and [Druid](Apache%20Druid) for enterprise-grade cloud services).

[MotherDuck](https://motherduck.com/) is the managed service around DuckDB that lets you scale from a local DB to a cloud DB and hybrid—done by one of [Google BigQuery](Google%20BigQuery) creators or developers such as [[Jordan Tigani]]. Check his discussion on the [Analytics Engineering Podcast about The Personal Data Warehouse](https://open.spotify.com/episode/3CmeFOuIOg91xApdjbWqey?si=CmelGaxBTZ-Z-BR3fvMjmg&utm_source=copy-link&nd=1). The stimulating conversation around connected WebAssembly, e.g., Is an application compiled to C code, which is super fast. E.g., Figma is using that, which would otherwise never work in a browser. 

## Benchmarks
- [Fast Analysis With DuckDB + Pyarrow](https://tech.gerardbentley.com/python/data/intermediate/2022/04/26/holy-duck.html) - 2022
- [SQL on Python, part 1: The simplicity of DuckDB](https://www.orchest.io/blog/sql-on-python-part-1-the-simplicity-of-duckdb): How to use DuckDB to analyze 4.6+ million mentions of climate change on Reddit
- [Tweet](https://mobile.twitter.com/medriscoll/status/1554698141789614081): Impressively fast, collaborative exploratory data analytics over a 20+ million row data set, hosted in the cloud with Drifting’s Jamsocket + Rill Data + DuckDB - 2022
- [Taking DuckDB for a spin | Uwe’s Blog](https://uwekorn.com/2019/10/19/taking-duckdb-for-a-spin.html) - 2019
- [SQLite vs DuckDB paper](https://simonwillison.net/2022/Sep/1/sqlite-duckdb-paper/): 
  - SQLite out-performs DuckDB on a write transactions benchmark by 10x-500x on a powerful cloud server and 2x-60x on a Raspberry Pi, for small to large databases.
  - For analytical benchmarks using the SSB (Star Schema Benchmark) DuckDB out-performs SQLite by 30-50x at the highest margin and 3-8x at the lowest.

## Example Projects
- [Modern Data Stack in a Box with DuckDB](https://duckdb.org/2022/10/12/modern-data-stack-in-a-box.html): A fast, free, and open-source Modern Data Stack (MDS) can now be fully deployed on your laptop or to a single machine using the combination of DuckDB, Meltano, dbt, and Apache Superset. 
- [Fully Featured Project Example](https://github.com/dagster-io/dagster/blob/master/examples/project_fully_featured/) (s3, dbt, parquet, and snowflake) reading from Hackernews orchestrated with dagster.
- [Data Engineering in 2022: Exploring dbt with DuckDB](https://rmoff.net/2022/10/20/data-engineering-in-2022-exploring-dbt-with-duckdb/):  Step-by-step guide on using dbt and DuckDB.
- [Build a poor man’s data lake from scratch with DuckDB](https://dagster.io/blog/duckdb-data-lake): Full fleshed example by Dagster.

## Tech and Papers
It ships as an [amalgamation](https://www.sqlite.org/amalgamation.html) build - a single giant C++ file (SQLite is a single giant C file). And it's also backed up by some strong computer science. It's by the academic researchers behind MonetDB and includes implementations of a bunch of interesting papers:
-   [Data Management for Data Science - Towards Embedded Analytics](https://www.duckdb.org/pdf/CIDR2020-raasveldt-muehleisen-duckdb.pdf) (CIDR 2020)
-   [DuckDB: an Embeddable Analytical Database](https://www.duckdb.org/pdf/SIGMOD2019-demo-duckdb.pdf) (SIGMOD 2019 Demo)

From [Why DuckDB](https://duckdb.org/why_duckdb):
> DuckDB contains a **columnar-vectorized query execution engine**, where queries are still interpreted, but a large batch of values (a “vector”) is processed in one operation. This dramatically reduces overhead in traditional systems such as PostgreSQL, MySQL, or SQLite, which process each row sequentially. Vectorized query execution leads to far better performance in OLAP queries.


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

