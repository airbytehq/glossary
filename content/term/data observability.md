---
title: "What is Data Observability?"
tags:
- data engineering
---

Data observability, also known as monitoring, continuously collects metrics about your data. You can collect data about the number of rows, columns, and properties for each dataset. You can also manage metadata about the dataset, such as when it was last updated.

From the great article [Choosing a Data Quality Tool - by Sarah Krasnik](https://sarahsnewsletter.substack.com/p/choosing-a-data-quality-tool?s=r), there are also different categories for observability:
- **Auto-profiling data**
	- [Bigeye](https://www.bigeye.com/): unique in a wide range of ML-driven automatic threshold tests and alerts
	- [Datafold](https://www.datafold.com/): unique Github integration presenting Data Diff between environments with custom tests
	- [Monte Carlo](https://www.montecarlodata.com/): unique in being the most enterprise-ready enterprise-ready with many data lake integrations
	- [Lightup](https://www.lightup.ai/): unique self-hosted deployment option, appealing to highly regulated industries
	- [Metaplane](https://www.metaplane.dev/): unique in a high level of configuration for a hosted tool with both out-of-the-box and custom tests
- **Pipeline Testing**
	- [Great Expectations](https://greatexpectations.io/): unique in its data quality specific community and automatic documentation of tests
	- [Soda](https://www.soda.io/): unique in its self-hosted cloud option
	- [dbt tests](https://docs.getdbt.com/docs/building-a-dbt-project/tests): unique in integration with dbt core and dbt Cloud builds (naturally), but not as versatile outside of the dbt ecosystem
- **Infrastructure monitoring**
	- [DataDog](https://www.datadoghq.com/): unique agent implementation that can be deployed anywhere for monitoring, even at the container level, with custom Airflow metric reporting
	- [New Relic](https://newrelic.com/): unique one-step integration with the big three cloud 	
- **A little bit of everything**
	- [Databand](https://databand.ai/): unique integration with Airflow and specific Airflow metric monitoring
	- [Unravel](https://www.unraveldata.com/): unique support for other data sources like Spark, data lake, and NoSQL databases
	- [Data Catalogs](term/data%20catalog.md): Helping observe existing data

Related terms are [Data Governance](term/data%20governance.md) and [Data Quality](term/data%20quality.md).
