---
title: "What is a Software-Defined Asset?"
tags:
- data engineering
---
The software-defined asset was first [introduced](https://dagster.io/blog/software-defined-assets) by [Dagster](term/Dagster.md) with the following definition:
> A new, [declarative](term/declarative.md) approach to managing data and orchestrating its maintenance. 
> Declarative data management starts with using code to define the data assets that you want to exist. These asset definitions, version-controlled through git and inspectable via tooling, allow anyone in your organization to understand your canonical set of data assets, enable you to reproduce them at any time, and offer a foundation for asset-based orchestration.

The key to software-defined assets is to declare a data asset/product pre-runtime. The SW-defined function in Dagster is like a microservice or the code that defines the asset in a  [functional way](term/functional%20data%20engineering.md) (that can live independently). With the declarative approach, we have more information defined as code helping the [orchestrator](term/data%20orchestrator.md) to figure out the lineage, how to run, etc. 

The best thing, you get the actual data lineage of your physical assets, not an arbitrary lineage of tasks (that is interesting for engineers but not for data consumers).

In the future, more code will be written with SW-defined assets as it reduces the need for writing lots of boilerplate as it's declarative and describes what the asset is supposed to do and include rather than how that is handled and run by Dagster. See more on [Data Orchestration Trends](https://airbyte.com/blog/data-orchestration-trends), where the trends included in this shift from an [imperative](term/imperative.md) pipeline with ops, jobs, graphs, etc., to Assets with Software-defined assets are explained.

Much has been announced on the [Dagster Community Day](https://www.youtube.com/live/An78xLxM9zQ?feature=share), where Nick said, the founder of Dagster: "Think of an iPhone: It feels like this one device, but there is a lot of complexity, and heterogeneous. The same is true for orchestration which could be the future to bundle the [Open Data Stack](term/open%20data%20stack.md) into one coherent data stack. An alternative would be a vertical integration with one of the prominent vendors.


