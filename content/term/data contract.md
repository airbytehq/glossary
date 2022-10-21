---
title: "What is a Data Contract?"
tags:
- data engineering
---

Data Contracts are API-like agreements between software/data engineers who own services and data consumers that understand how the business works. The goal is to generate well-modeled, high-quality, trusted, real-time data.

It's an **abstraction** that allows engineers to decouple their databases and services from analytics and ML requirements. It will avoid production-breaking incidents when modifying the schema as they are validated and enforced.

![](images/data-contract.png)
Illustration by Chad Sanderson on [The Rise of Data Contracts - by Chad Sanderson](https://dataproducts.substack.com/p/the-rise-of-data-contracts)

[Chad Sanderson](https://www.linkedin.com/in/chad-sanderson/) said that at Convoy, they use [[Protobuf]] and [[Apache Kafka]] to abstract the CRUD transactions. They define the schema based on what they *need*, not what they get from the source. Same as [[Software-Defined Assets]] describe the [Data Asset](term/data%20asset.md) in a declarative manner and set [expectations](https://github.com/dagster-io/dagster/discussions/9543).

Confluent also built similar functions on top of Kafka with their [Schema Registry](https://docs.confluent.io/platform/current/schema-registry/), and terms such as [Semantic Layer](term/metrics%20layer.md) and [Analytics API](https://www.sspaeti.com/blog/analytics-api-with-graphql-the-next-level-of-data-engineering/#what-is-an-analytics-api) (with [[GraphQL]]) are trying to achieve similar things.

Data Contracts are not meant to replace data pipelines and [Modern Data Stack](term/modern%20data%20stack.md), a more batch approach. These are good for fast prototyping. You could start defining data contracts when you have some knowledge about data.

Interestingly, the differentiation to [Data Mesh](term/data%20mesh.md) is an organizational framework with a micro-service approach to data. Data Mesh doesn't inform which data should be emitted or validate the data being emitted from production is correct or conforms to a consumer's expectations.

Also, data contracts are a form of [Data Governance](term/data%20governance.md). This term is very vague and gets more concrete with explicit contracts. You can also use [Great Expectations](https://greatexpectations.io/) to set expectations for your data, which I believe is a great way to start.

## From the Discussion on YouTube w/ Chad Sanderson vs Ethan Aaron

Chad Sanderson says in [Data Contract Battle Royale w/ Chad Sanderson vs Ethan Aaron - YouTube](https://youtu.be/4BEpYAp3Qu4) :
- It's just a database version of a real-world contract. 
- A real-world contract is just an agreement between two parties where:
	- There's some mechanism for enforcing that it happens. 
	- A data contract is a similar agreement, but it's **between someone that produces data and consumes data** to vend a particular data set which usually includes a schema and some enforcement mechanism. 
- Differentiation between data contract and data product:
	- **Data contract**, which is *what* is the data and *how* do we enforce this quality 
	- **[Data Product](term/data%20product.md)** which is *why* do we need this data 

Ethan Aaron is saying his problem with data contracts is that you focus on defining the interface/contract too early. E.g., if you have a big task done by several teams or people, you have a contract to agree on an interface. I'd argue that's precisely what the data products are, and instead of agreeing on some artificial contract, decide on the product, so the tools and teams can be distinct.

## Summary Blog Posts
An excellent summary by [Mehdi Ouazza](https://www.linkedin.com/in/mehd-io) about data contracts [From Zero To Hero](https://towardsdatascience.com/data-contracts-from-zero-to-hero-343717ac4d5e). He is illustrating how [[Apache Kafka]] could also be the interface that defines the contract.

![](images/data-contract-example.png)
Illustration from [Data Contracts — From Zero To Hero](https://towardsdatascience.com/data-contracts-from-zero-to-hero-343717ac4d5e)

See also [Semantic Warehouse](term/semantic%20warehouse.md).
